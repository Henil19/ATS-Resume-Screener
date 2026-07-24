from utils.pdf_reader import extract_text_from_pdf
from utils.job_reader import extract_text_from_job
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills
from utils.matcher import compare_skills
from utils.skill_loader import load_skills
from utils.score_calculator import calculate_score
from utils.report_generator import generate_report,save_report
from utils.alias_loader import load_aliases

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

    if DEBUG:
        print("\n===== CLEAN RESUME DESCRIPTION =====\n")
        print(clean_resume)

    if DEBUG:
        print("\n===== CLEAN JOB DESCRIPTION =====\n")
        print(clean_job)

    skills_database = load_skills("data/raw_skills.csv")
    aliases = load_aliases("data/skill_aliases.csv")
    resume_skills = extract_skills(clean_resume,aliases)
    job_skills = extract_skills(clean_job,aliases)

    if DEBUG:
        print("\n===== RESUME SKILLS =====\n")
        print(resume_skills)

        print("\n===== JOB SKILLS =====\n")
        print(job_skills)

    matched, missing, extra = compare_skills(
    resume_skills,
    job_skills
    )

    ats_score = calculate_score(
    matched,
    job_skills
    )

    if ats_score >= 70:
        status = "STRONG MATCH"

    elif ats_score >= 40:
        status = "MODERATE MATCH"

    else:
        status = "LOW MATCH"

    report = generate_report(
    ats_score,
    status,
    matched,
    missing,
    extra
    )

    print(report)

    save_report(
    report,
    "outputs/ats_report.txt"
    )

if __name__ == "__main__":
    main()