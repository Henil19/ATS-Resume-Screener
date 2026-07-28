from utils.role_alias_loader import load_role_aliases

role_aliases = load_role_aliases("data/role_aliases.csv")

print("===== ROLE ALIASES =====")

for alias, canonical in role_aliases.items():
    print(f"{alias} -> {canonical}")