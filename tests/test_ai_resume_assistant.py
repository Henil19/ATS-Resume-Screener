from utils.ai_resume_assistant import (
    generate_ai_feedback
)


class MockProvider:
    """
    Fake LLM provider used for testing.
    """

    def generate_response(
        self,
        prompt
    ):

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


def test_ai_resume_assistant():
    """
    Test AI Resume Assistant.
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

    system_prompt = (
        "You are an AI Resume Assistant."
    )

    provider = MockProvider()

    feedback = generate_ai_feedback(

        ats_data,

        system_prompt,

        provider

    )

    assert isinstance(
        feedback,
        dict
    )

    required_keys = [

        "summary",

        "strengths",

        "weaknesses",

        "missing_technologies",

        "improvement_suggestions",

        "recommended_projects",

        "hiring_recommendation"

    ]

    for key in required_keys:

        assert key in feedback

    assert (
        feedback["summary"]
        ==
        "Excellent resume."
    )

    assert (
        feedback[
            "hiring_recommendation"
        ]
        ==
        "Recommended for Interview"
    )

    print(
        "[PASS] AI Resume Assistant"
    )


def main():

    print("=" * 50)

    print(
        "AI Resume Assistant Test"
    )

    print("=" * 50)

    test_ai_resume_assistant()

    print()

    print(
        "AI Resume Assistant Passed"
    )


if __name__ == "__main__":

    main()