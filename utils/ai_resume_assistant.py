import json


from utils.ai_response_schema import build_ai_response_schema


def generate_ai_feedback(
    ats_data,
    system_prompt,
    llm_provider
):
    """
    Generate AI feedback using the selected LLM provider.
    """

    prompt = f"""
{system_prompt}

ATS DATA

{json.dumps(ats_data, indent=4)}
"""

    response = llm_provider.generate_response(
        prompt
    )

    try:

        ai_feedback = json.loads(
            response
        )

    except json.JSONDecodeError:

        ai_feedback = build_ai_response_schema()

    return ai_feedback