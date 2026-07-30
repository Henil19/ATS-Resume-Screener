import json


def generate_resume_rewrite(
    rewrite_prompt,
    provider
):
    """
    Generate AI-powered resume rewrite suggestions.

    Parameters
    ----------
    rewrite_prompt : str

    provider : GeminiProvider

    Returns
    -------
    dict
    """

    response = provider.generate_response(
        rewrite_prompt
    )

    try:

        return json.loads(
            response
        )

    except Exception:

        return {

            "professional_summary": [],

            "experience": [],

            "projects": [],

            "technical_skills": [],

            "ats_keywords": [],

            "formatting": []

        }