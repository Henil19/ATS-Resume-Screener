from utils.weighted_score_calculator import calculate_weighted_score

matched_skills = {
    "python",
    "docker",
    "git"
}

job_skills = {
    "python",
    "docker",
    "git",
    "tensorflow"
}

role_weights = {
    "python": 10,
    "docker": 8,
    "git": 6,
    "tensorflow": 9
}

score = calculate_weighted_score(
    matched_skills,
    job_skills,
    role_weights
)

print("Weighted Score:")
print(score)