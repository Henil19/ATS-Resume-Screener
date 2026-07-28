def build_ai_response_schema():
    """
    Build the default AI response schema.

    Every AI response must follow this structure.
    """

    ai_response = {
        "summary": "",

        "strengths": [],

        "weaknesses": [],

        "missing_technologies": [],

        "improvement_suggestions": [],

        "recommended_projects": [],

        "hiring_recommendation": ""
    }

    return ai_response