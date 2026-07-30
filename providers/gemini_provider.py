import os

from dotenv import load_dotenv

from google import genai


class GeminiProvider:
    """
    Gemini AI Provider.
    """

    def __init__(self):
        """
        Initialize Gemini provider.
        """

        load_dotenv()

        api_key = os.getenv(
            "GEMINI_API_KEY"
        )

        if not api_key:

            raise ValueError(
                "GEMINI_API_KEY not found. Please check your .env file."
            )

        self.model = os.getenv(
            "GEMINI_MODEL",
            "gemini-2.5-flash"
        )

        self.client = genai.Client(
            api_key=api_key
        )

    def generate_response(
        self,
        prompt
    ):
        """
        Generate a response from Gemini.
        """

        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )

            return response.text

        except Exception as error:

            raise RuntimeError(
                f"Failed to generate response from Gemini.\nReason: {error}"
            )