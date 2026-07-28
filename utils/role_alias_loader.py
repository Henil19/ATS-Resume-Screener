import csv


def load_role_aliases(csv_path):

    role_aliases = {}

    with open(csv_path, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            alias = row["alias"].strip().lower()

            canonical_role = row["canonical_role"].strip().lower()

            role_aliases[alias] = canonical_role

    return role_aliases

