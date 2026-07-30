from utils.ats_engine import (
    run_ats_pipeline
)


def test_ats_pipeline():
    """
    Test the complete ATS pipeline.
    """

    results = run_ats_pipeline(
        "resumes/sample_resume.pdf",
        "job_descriptions/sample_job.txt"
    )

    assert isinstance(
        results,
        dict
    )

    required_keys = [

        "role",

        "ats_score",

        "status",

        "matched",

        "missing",

        "extra",

        "ats_data",

        "semantic_data",

        "explainability_data",

        "rewrite_prompt",

        "recommendation_data",

        "rewrite_feedback",

        "ai_feedback",

        "report"

    ]

    for key in required_keys:

        assert key in results, (
            f"Missing key: {key}"
        )

    assert (
        0 <= results["ats_score"] <= 100
    )

    assert isinstance(
        results["matched"],
        set
    )

    assert isinstance(
        results["missing"],
        set
    )

    assert isinstance(
        results["extra"],
        set
    )

    assert isinstance(
        results["semantic_data"],
        dict
    )

    assert isinstance(
        results["recommendation_data"],
        dict
    )

    assert isinstance(
        results["rewrite_feedback"],
        dict
    )

    assert isinstance(
        results["ai_feedback"],
        dict
    )

    assert isinstance(
        results["report"],
        str
    )

    print(
        "[PASS] ATS Pipeline"
    )


def main():

    print("=" * 50)

    print(
        "ATS Pipeline Test"
    )

    print("=" * 50)

    test_ats_pipeline()

    print()

    print(
        "ATS Pipeline Passed"
    )


if __name__ == "__main__":

    main()