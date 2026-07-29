from utils.ats_engine import run_ats_pipeline
from utils.report_generator import save_report


def main():

    results = run_ats_pipeline(
        "resumes/sample_resume.pdf",
        "job_descriptions/sample_job.txt"
    )

    print(results["report"])

    save_report(
        results["report"],
        "outputs/ats_report.txt"
    )


if __name__ == "__main__":
    main()