from utils.ai_resume_assistant import generate_ai_feedback


class MockProvider:
    """
    Fake LLM provider used for testing.
    """

    def generate_response(self, prompt):

        return """
{
    "summary": "Excellent resume.",
    "strengths": [
        "Strong Python skills",
        "Good Machine Learning background"
    ],
    "weaknesses": [
        "Needs Docker"
    ],
    "missing_technologies": [
        "Docker"
    ],
    "improvement_suggestions": [
        "Learn Docker",
        "Build deployment projects"
    ],
    "recommended_projects": [
        "Resume Screening System"
    ],
    "hiring_recommendation": "Recommended for Interview"
}
"""


ats_data = {
    "role": "software_engineer",
    "ats_score": 82.5,
    "status": "STRONG MATCH",
    "resume_skills": [],
    "job_skills": [],
    "matched_skills": [],
    "missing_skills": [],
    "extra_skills": []
}

system_prompt = "You are an AI Resume Assistant."

provider = MockProvider()

feedback = generate_ai_feedback(
    ats_data,
    system_prompt,
    provider
)

print("\n===== AI FEEDBACK TEST =====\n")

for key, value in feedback.items():
    print(f"{key}:")
    print(value)
    print()