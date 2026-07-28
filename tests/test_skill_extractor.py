from utils.alias_loader import load_aliases
from utils.skill_extractor import extract_skills

aliases = load_aliases("data/skill_aliases.csv")

text = """
Python
TensorFlow
Machine Learning
Docker
AWS
GitHub
React
"""

skills = extract_skills(text.lower(), aliases)

print("===== EXTRACTED SKILLS =====")

for skill in sorted(skills):
    print(skill)
