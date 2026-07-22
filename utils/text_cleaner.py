import re

def clean_text(text):
    
    # Convert to lowercase
    text = text.lower()

    # Replace hyphens with spaces
    text = text.replace("-", " ")

    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove leading/trailing spaces
    text = text.strip()

    return text