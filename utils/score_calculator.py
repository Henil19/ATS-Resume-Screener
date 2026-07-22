def calculate_score(matched_skills, job_skills):
    """
    Calculates the ATS score based on matched job skills.
    """

    if len(job_skills) == 0:
        return 0

    score = (len(matched_skills) / len(job_skills)) * 100

    return round(score, 2)