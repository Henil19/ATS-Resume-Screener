from utils.ats_engine import run_ats_pipeline


results = run_ats_pipeline(
    "resumes/sample_resume.pdf",
    "job_descriptions/sample_job.txt"
)

print("\n===== ATS ENGINE TEST =====\n")

print(results["report"])