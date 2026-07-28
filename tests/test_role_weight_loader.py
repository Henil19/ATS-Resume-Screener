from utils.role_weight_loader import load_role_weights

weights = load_role_weights("ai_engineer")

print("===== AI ENGINEER WEIGHTS =====")

for skill, weight in weights.items():
    print(f"{skill} : {weight}")