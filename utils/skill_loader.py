import pandas as pd

def load_skills(file_path):
    df = pd.read_csv(file_path, sep="\t")

    # Keep only the skill names
    skills = df["name:String"].dropna().str.lower().tolist()

    return skills