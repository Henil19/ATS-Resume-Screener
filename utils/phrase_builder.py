def build_phrases(tokens, max_phrase_length=3):
    """
    Generate candidate phrases from tokens.

    Example:
    max_phrase_length = 3

    Generates:
    - Single words
    - Two-word phrases
    - Three-word phrases
    """

    phrases = []

    # Single-word phrases
    phrases.extend(tokens)

    # Multi-word phrases
    for length in range(2, max_phrase_length + 1):

        for i in range(len(tokens) - length + 1):

            phrase = " ".join(tokens[i:i + length])

            phrases.append(phrase)

    return phrases