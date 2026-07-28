import os

from dotenv import load_dotenv

from google import genai


class GeminiProvider:
    """
    Gemini AI Provider
    """

    def __init__(self):

        # Load environment variables
        if not load_dotenv():
            raise FileNotFoundError(
                ".env file not found in the project root."
            )

        # Read API Key
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found. Please check your .env file."
            )

        # Read Model Name
        model_name = os.getenv("GEMINI_MODEL")

        if not model_name:
            raise ValueError(
                "GEMINI_MODEL not found. Please check your .env file."
            )

        # Create Gemini Client
        self.client = genai.Client(
            api_key=api_key
        )

        self.model = model_name

    def generate_response(
        self,
        prompt
    ):

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