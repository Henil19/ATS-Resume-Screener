import re


def extract_skills(text, skills_database):
    """
    Extract recognized skills using whole-word matching.
    """

    found_skills = set()

    for skill in skills_database:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found_skills.add(skill)

    return found_skills