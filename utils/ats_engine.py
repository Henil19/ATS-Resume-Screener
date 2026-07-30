from utils.pdf_reader import extract_text_from_pdf
from utils.job_reader import extract_text_from_job
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills
from utils.matcher import compare_skills
from utils.alias_loader import load_aliases
from utils.role_detector import detect_role
from utils.role_alias_loader import load_role_aliases
from utils.role_resolver import resolve_role
from utils.role_weight_loader import load_role_weights
from utils.weighted_score_calculator import calculate_weighted_score
from utils.ats_data_builder import build_ats_data
from utils.ai_resume_assistant import generate_ai_feedback
from utils.report_generator import generate_report
from providers.gemini_provider import GeminiProvider
from utils.semantic_engine import build_semantic_data
from utils.explainability import generate_explanations
from utils.rewrite_engine import build_rewrite_prompt
from utils.recommendation_engine import generate_job_recommendations
from utils.prompt_loader import load_prompt
from utils.ai_rewrite_assistant import generate_resume_rewrite


def run_ats_pipeline(
    resume_path,
    job_path,
    progress_callback=None
):
    """
    Runs the complete ATS + AI pipeline.
    Returns all results in a single dictionary.
    """

    def update_progress(message):

        if progress_callback:

            progress_callback(message)

    # -----------------------------
    # Read Files
    # -----------------------------
    update_progress("Reading Resume...")

    resume_text = extract_text_from_pdf(
        resume_path
    )

    update_progress("Reading Job Description...")

    job_text = extract_text_from_job(
        job_path
    )

    # -----------------------------
    # Clean Text
    # -----------------------------
    update_progress("Cleaning Text...")

    clean_resume = clean_text(
        resume_text
    )

    clean_job = clean_text(
        job_text
    )

    # -----------------------------
    # Detect Role
    # -----------------------------
    update_progress("Detecting Role...")

    detected_role = detect_role(
        job_text
    )

    # -----------------------------
    # Load Data
    # -----------------------------

    aliases = load_aliases(
        "data/skill_aliases.csv"
    )

    role_aliases = load_role_aliases(
        "data/role_aliases.csv"
    )

    # -----------------------------
    # Extract Skills
    # -----------------------------
    update_progress("Extracting Skills...")

    resume_skills = extract_skills(
        clean_resume,
        aliases
    )

    job_skills = extract_skills(
        clean_job,
        aliases
    )

    # -----------------------------
    # Compare Skills
    # -----------------------------

    matched, missing, extra = compare_skills(
        resume_skills,
        job_skills
    )

    # -----------------------------
    # Resolve Role
    # -----------------------------

    canonical_role = resolve_role(
        detected_role,
        role_aliases
    )

    role_weights = load_role_weights(
        canonical_role
    )

    # -----------------------------
    # Calculate Score
    # -----------------------------
    update_progress("Calculating ATS Score...")

    ats_score = calculate_weighted_score(
        matched,
        job_skills,
        role_weights
    )

    if ats_score >= 70:
        status = "STRONG MATCH"

    elif ats_score >= 40:
        status = "MODERATE MATCH"

    else:
        status = "LOW MATCH"

    # -----------------------------
    # Build ATS JSON
    # -----------------------------

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

        # -----------------------------
    # Semantic Analysis
    # -----------------------------
    update_progress(
        "Running Semantic Analysis..."
    )

    semantic_data = build_semantic_data(
        clean_resume,
        clean_job,
        resume_skills,
        job_skills
    )

    # -----------------------------
    # Explainability
    # -----------------------------
    update_progress(
        "Generating Explainability..."
    )

    explainability_data = (
        generate_explanations(
            semantic_data
        )
    )

    # -----------------------------
    # Rewrite Prompt
    # -----------------------------
    update_progress(
        "Preparing Resume Rewrite..."
    )

    rewrite_prompt = (
        build_rewrite_prompt(
            resume_text,
            ats_data,
            semantic_data,
            explainability_data
        )
    )

    # -----------------------------
    # Load Prompt
    # -----------------------------

    system_prompt = load_prompt(
    "prompts/resume_assistant_prompt.txt"
    )

    # -----------------------------
    # AI Feedback
    # -----------------------------

    provider = GeminiProvider()
    update_progress(
    "Generating Resume Rewrite..."
    )

    rewrite_feedback = (
        generate_resume_rewrite(
            rewrite_prompt,
            provider
        )
    )
    update_progress("Generating AI Feedback...")

    ai_feedback = generate_ai_feedback(
        ats_data,
        system_prompt,
        provider
    )

        # -----------------------------
    # Job Recommendations
    # -----------------------------
    update_progress(
        "Generating Recommendations..."
    )

    recommendation_data = (
        generate_job_recommendations(
            canonical_role,
            semantic_data,
            ats_score
        )
    )

    # -----------------------------
    # Generate Report
    # -----------------------------
    update_progress("Generating Report...")

    report = generate_report(
        ats_score,
        status,
        matched,
        missing,
        extra,
        ai_feedback
    )

    # -----------------------------
    # Return Everything
    # -----------------------------

    return {
    "role": canonical_role,
    "ats_score": ats_score,
    "status": status,
    "matched": matched,
    "missing": missing,
    "extra": extra,
    "ats_data": ats_data,
    "semantic_data": semantic_data,
    "explainability_data": explainability_data,
    "rewrite_prompt": rewrite_prompt,
    "recommendation_data": recommendation_data,
    "ai_feedback": ai_feedback,
    "report": report,
    "rewrite_feedback": rewrite_feedback,
    }