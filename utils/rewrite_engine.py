import json
from utils.prompt_loader import load_prompt

def build_rewrite_prompt(
    resume_text,
    ats_data,
    semantic_data,
    explainability_data
):
    """
    Build the prompt used for AI-powered
    resume rewriting.
    """

    system_prompt = load_prompt(
        "prompts/rewrite_prompt.txt"
    )

    prompt = f"""
    {system_prompt}

    Resume

    {resume_text}

    ATS Analysis

    {json.dumps(ats_data, indent=4)}

    Semantic Analysis

    {json.dumps(semantic_data, indent=4)}

    Explainability

    {json.dumps(explainability_data, indent=4)}
    """

    return prompt