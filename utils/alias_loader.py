import pandas as pd


def load_aliases(file_path):
    df = pd.read_csv(file_path)

    aliases = dict(
        zip(
            df["alias"],
            df["canonical_skill"]
        )
    )

    return aliases

def get_max_phrase_length(aliases):

    max_length = 1

    for alias in aliases:

        word_count = len(alias.split())

        if word_count > max_length:

            max_length = word_count

    return max_length
