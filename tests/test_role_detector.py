from utils.role_detector import detect_role

job_description = """
We are hiring an AI Engineer.

Requirements:
Python
TensorFlow
Machine Learning
Docker
"""

role = detect_role(job_description)

print("Detected Role:")
print(role)