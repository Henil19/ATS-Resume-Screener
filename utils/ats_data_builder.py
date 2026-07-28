def build_ats_data(
    role,
    ats_score,
    status,
    resume_skills,
    job_skills,
    matched_skills,
    missing_skills,
    extra_skills
):
    """
    Build a standardized ATS data object.

    This object is sent to the AI Resume Assistant.
    """

    ats_data = {
        "role": role,
        "ats_score": ats_score,
        "status": status,
        "resume_skills": sorted(list(resume_skills)),
        "job_skills": sorted(list(job_skills)),
        "matched_skills": sorted(list(matched_skills)),
        "missing_skills": sorted(list(missing_skills)),
        "extra_skills": sorted(list(extra_skills))
    }

    return ats_data