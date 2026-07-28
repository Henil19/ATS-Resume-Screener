import re

def clean_text(text):

    text = text.lower()

    text = text.replace("-", " ")

    text = re.sub(r"[^\w\s]", "", text)

    text = re.sub(r"\s+", " ", text)

    text = text.strip()

    return text