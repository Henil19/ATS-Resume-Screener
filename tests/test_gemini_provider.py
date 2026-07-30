from providers.gemini_provider import (
    GeminiProvider
)


def test_gemini_provider():
    """
    Test Gemini API connectivity.
    """

    provider = GeminiProvider()

    response = provider.generate_response(
        "Reply with exactly the words: Gemini Connection Successful"
    )

    assert isinstance(
        response,
        str
    )

    assert len(
        response.strip()
    ) > 0

    print(
        "[PASS] Gemini Provider"
    )


def main():

    print("=" * 50)

    print(
        "Gemini Provider Test"
    )

    print("=" * 50)

    test_gemini_provider()

    print()

    print(
        "Gemini Provider Passed"
    )


if __name__ == "__main__":

    main()