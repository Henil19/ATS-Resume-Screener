from utils.pdf_reader import extract_text_from_pdf
from utils.job_reader import extract_text_from_job
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills
from utils.matcher import compare_skills
from utils.report_generator import generate_report,save_report
from utils.alias_loader import load_aliases
from utils.role_detector import detect_role
from utils.role_alias_loader import load_role_aliases
from utils.role_resolver import resolve_role
from utils.role_weight_loader import load_role_weights
from utils.weighted_score_calculator import calculate_weighted_score
from utils.ats_data_builder import build_ats_data
from utils.ai_resume_assistant import generate_ai_feedback
from providers.gemini_provider import GeminiProvider

DEBUG = False

def main():
    resume_path = "resumes/sample_resume.pdf"
    resume_text = extract_text_from_pdf(resume_path)
    if DEBUG:
        print("\n===== RAW RESUME =====\n")
        print(resume_text)

    job_path = "job_descriptions/sample_job.txt"

    job_text = extract_text_from_job(job_path)

    if DEBUG:
        print("\n===== RAW JOB DESCRIPTION =====\n")
        print(job_text)

    clean_resume = clean_text(resume_text)
    clean_job = clean_text(job_text)
    detected_role = detect_role(job_text)

    if DEBUG:
        print("\n===== CLEAN RESUME DESCRIPTION =====\n")
        print(clean_resume)

    if DEBUG:
        print("\n===== CLEAN JOB DESCRIPTION =====\n")
        print(clean_job)

    aliases = load_aliases("data/skill_aliases.csv")
    role_aliases = load_role_aliases("data/role_aliases.csv")
    resume_skills = extract_skills(clean_resume,aliases)
    job_skills = extract_skills(clean_job,aliases)

    if DEBUG:
        print("\n===== RESUME SKILLS =====\n")
        print(resume_skills)

        print("\n===== JOB SKILLS =====\n")
        print(job_skills)

    matched, missing, extra = compare_skills(resume_skills,job_skills)

    canonical_role = resolve_role(detected_role,role_aliases)
    role_weights = load_role_weights(canonical_role)

    ats_score = calculate_weighted_score(matched,job_skills,role_weights)

    if ats_score >= 70:
        status = "STRONG MATCH"

    elif ats_score >= 40:
        status = "MODERATE MATCH"

    else:
        status = "LOW MATCH"

    if DEBUG:
        print("\n===== DETECTED ROLE =====")
        print(detected_role)

        print("\n===== CANONICAL ROLE =====")
        print(canonical_role)

        print("\n===== ROLE WEIGHTS =====")
        print(role_weights)

    ats_data = build_ats_data(
    canonical_role,
    ats_score,
    status,
    resume_skills,
    job_skills,
    matched,
    missing,
    extra
    )

    with open(
    "prompts/resume_assistant_prompt.txt",
    "r",
    encoding="utf-8"
    ) as file:
        system_prompt = file.read()

    provider = GeminiProvider()

    ai_feedback = generate_ai_feedback(
    ats_data,
    system_prompt,
    provider
    )

    report = generate_report(ats_score,status,matched,missing,extra,ai_feedback)
    print(report)
    
    save_report(report,"outputs/ats_report.txt")


if __name__ == "__main__":
    main()