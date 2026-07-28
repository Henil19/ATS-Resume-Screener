from providers.gemini_provider import GeminiProvider

provider = GeminiProvider()

response = provider.generate_response(
    "Reply with exactly one sentence saying the Gemini connection is working."
)

print("\n===== GEMINI PROVIDER TEST =====\n")

print(response)