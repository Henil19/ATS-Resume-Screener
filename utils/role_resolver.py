def resolve_role(detected_role, role_aliases):
    if detected_role is None:
        return "software_engineer"

    detected_role = detected_role.strip()

    detected_role = detected_role.lower()

    canonical_role = role_aliases.get(
        detected_role,
        "software_engineer"
    )

    return canonical_role