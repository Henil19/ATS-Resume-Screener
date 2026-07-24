from utils.tokenizer import tokenize
from utils.phrase_builder import build_phrases
from utils.alias_loader import get_max_phrase_length

def extract_skills(text, aliases):

    found_skills = set()

    tokens = tokenize(text)

    max_phrase_length = get_max_phrase_length(aliases)

    candidates = build_phrases(
        tokens,
        max_phrase_length
    )

    for candidate in candidates:

        if candidate in aliases:

            canonical_skill = aliases[candidate]

            found_skills.add(canonical_skill)

    return found_skills