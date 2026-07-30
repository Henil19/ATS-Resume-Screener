import json


def load_role_recommendations(
    json_path="data/role_recommendations.json"
):
    """
    Load role recommendation mappings.
    """

    with open(
        json_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def generate_job_recommendations(
    detected_role,
    semantic_data,
    ats_score
):
    """
    Generate job recommendations.

    Parameters
    ----------
    detected_role : str

    semantic_data : dict

    ats_score : float

    Returns
    -------
    dict
    """

    recommendations = []

    overall_similarity = semantic_data[
        "overall_similarity"
    ]

    # ==========================================
    # Primary Recommendation
    # ==========================================

    if ats_score >= 85 and overall_similarity >= 85:

        confidence = "High"

        reason = (
            "Your resume strongly aligns with "
            "this role."
        )

    elif ats_score >= 65:

        confidence = "Moderate"

        reason = (
            "Your resume is a good fit with "
            "some improvements."
        )

    else:

        confidence = "Low"

        reason = (
            "Significant improvements are "
            "recommended before applying."
        )

    recommendations.append(

        {
            "role": detected_role,
            "confidence": confidence,
            "reason": reason
        }

    )

    # ==========================================
    # Related Roles
    # ==========================================

    role_database = load_role_recommendations()

    related_roles = role_database.get(
        detected_role,
        []
    )

    for role in related_roles:

        recommendations.append(

            {
                "role": role,
                "confidence": "Suggested",
                "reason":
                    "Closely related career path."
            }

        )

    # ==========================================
    # Recommendation Data Object
    # ==========================================

    return {

        "recommendations":
            recommendations

    }