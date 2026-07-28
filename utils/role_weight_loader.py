import csv
import os


def load_role_weights(role_name):
    """
    Load the weight profile for a given canonical role.

    Example:
        ai_engineer
            ↓
        data/role_weights/ai_engineer.csv

    Returns:
        Dictionary
        {
            "python": 10,
            "tensorflow": 9,
            "docker": 8
        }
    """

    file_path = os.path.join(
        "data",
        "role_weights",
        f"{role_name}.csv"
    )

    role_weights = {}

    with open(file_path, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            skill = row["skill"].strip().lower()

            weight = int(row["weight"])

            role_weights[skill] = weight

    return role_weights
