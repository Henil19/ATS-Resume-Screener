DEFAULT_SKILL_WEIGHT = 1


def calculate_weighted_score(matched_skills, job_skills, role_weights):
    matched_weight = 0
    total_weight = 0

    for skill in job_skills:
        total_weight += role_weights.get(skill, DEFAULT_SKILL_WEIGHT)

    for skill in matched_skills:
        matched_weight += role_weights.get(skill, DEFAULT_SKILL_WEIGHT)

    if total_weight == 0:
        return 0.0

    score = (matched_weight / total_weight) * 100

    return round(score, 2)