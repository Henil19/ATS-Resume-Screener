import traceback

from tests.test_embedding_engine import (
    test_single_embedding,
    test_batch_embeddings
)

from tests.test_ai_resume_assistant import (
    test_ai_resume_assistant
)

from tests.test_gemini_provider import (
    test_gemini_provider
)

from tests.test_ats_engine import (
    test_ats_pipeline
)


def run_test(
    name,
    test_function
):
    """
    Execute a single test.
    """

    try:

        test_function()

        print(
            f"[PASS] {name}"
        )

        return True

    except Exception:

        print(
            f"[FAIL] {name}"
        )

        traceback.print_exc()

        return False


def main():

    print()

    print("=" * 60)

    print(
        "ATS Resume Screener v3.0 Test Suite"
    )

    print("=" * 60)

    passed = 0

    failed = 0

    tests = [

        (
            "Embedding Engine",
            test_single_embedding
        ),

        (
            "Batch Embeddings",
            test_batch_embeddings
        ),

        (
            "AI Resume Assistant",
            test_ai_resume_assistant
        ),

        (
            "Gemini Provider",
            test_gemini_provider
        ),

        (
            "ATS Pipeline",
            test_ats_pipeline
        )

    ]

    for name, test in tests:

        print()

        if run_test(
            name,
            test
        ):

            passed += 1

        else:

            failed += 1

    print()

    print("=" * 60)

    print(
        f"Tests Passed : {passed}"
    )

    print(
        f"Tests Failed : {failed}"
    )

    if failed == 0:

        print()

        print(
            "Overall Status : PASS"
        )

    else:

        print()

        print(
            "Overall Status : FAIL"
        )

    print("=" * 60)


if __name__ == "__main__":

    main()