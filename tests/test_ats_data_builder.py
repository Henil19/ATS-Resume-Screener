from utils.ats_data_builder import build_ats_data

ats_data = build_ats_data(
    role="software_engineer",
    ats_score=95.5,
    status="STRONG MATCH",
    resume_skills={"python", "docker", "git"},
    job_skills={"python", "docker", "git", "aws"},
    matched_skills={"python", "docker", "git"},
    missing_skills={"aws"},
    extra_skills=set()
)

print("\n===== ATS DATA BUILDER TEST =====\n")

for key, value in ats_data.items():
    print(f"{key}: {value}")