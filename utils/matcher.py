def compare_skills(resume_skills, job_skills):

    matched = resume_skills.intersection(job_skills)

    missing = job_skills.difference(resume_skills)

    extra = resume_skills.difference(job_skills)

    return matched, missing, extra