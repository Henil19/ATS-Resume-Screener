from utils.role_alias_loader import load_role_aliases
from utils.role_resolver import resolve_role


role_aliases = load_role_aliases(
    "data/role_aliases.csv"
)

print(resolve_role("AI Engineer", role_aliases))

print(resolve_role("ML Engineer", role_aliases))

print(resolve_role("Backend Software Engineer", role_aliases))

print(resolve_role("Cloud Architect", role_aliases))

print(resolve_role("Some Random Role", role_aliases))