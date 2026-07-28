from utils.ai_response_schema import build_ai_response_schema

response = build_ai_response_schema()

print("===== AI RESPONSE SCHEMA =====\n")

for key, value in response.items():
    print(f"{key}:")
    print(value)
    print()