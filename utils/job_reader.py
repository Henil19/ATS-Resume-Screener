def extract_text_from_job(job_path):
    """
    Reads a text job description and returns its contents.
    """

    with open(job_path, "r", encoding="utf-8") as file:
        return file.read()