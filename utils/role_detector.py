def detect_role(job_text):
    """
    Detect the job role from the job description.

    Strategy:
    1. Look for labels like:
       - Job Title:
       - Position:
       - Role:
       - Designation:

    2. If none are found, use the first meaningful line
       that is not a common heading.

    Returns:
        str : Detected role (lowercase)
        None : If no role could be detected
    """

    # Convert to lowercase for easier matching
    job_text = job_text.lower()

    # Split into individual lines
    lines = job_text.splitlines()

    # Remove empty lines
    meaningful_lines = []

    for line in lines:
        line = line.strip()

        if line:
            meaningful_lines.append(line)

    # Common labels used in job descriptions
    labels = [
        "job title:",
        "position:",
        "role:",
        "designation:"
    ]

    # Search only the first 10 meaningful lines
    for line in meaningful_lines[:10]:

        for label in labels:

            if line.startswith(label):

                detected_role = line.replace(label, "").strip()

                return detected_role

    # Ignore common headings
    ignored = {
        "responsibilities",
        "requirements",
        "qualifications",
        "about us",
        "overview",
        "job description",
        "skills",
        "required skills",
        "preferred skills"
    }

    # If no labels were found, use the first meaningful line
    for line in meaningful_lines[:10]:

        if line not in ignored:

            return line

    return None

if __name__ == "__main__":

    sample_1 = """
    Job Title: AI Engineer

    Responsibilities
    Build AI systems...
    """

    sample_2 = """
    Backend Developer

    Requirements
    Python
    Docker
    """

    sample_3 = """
    Position: Data Scientist

    Qualifications
    Machine Learning
    SQL
    """

    print(detect_role(sample_1))
    print(detect_role(sample_2))
    print(detect_role(sample_3))