def generate_explanations(semantic_data):
    """
    Generate explainable insights from
    semantic matching results.

    Parameters
    ----------
    semantic_data : dict

    Returns
    -------
    dict
    """

    overall_similarity = semantic_data[
        "overall_similarity"
    ]

    # ==========================================
    # Overall Summary
    # ==========================================

    if overall_similarity >= 90:

        overall_summary = (
            "The resume is semantically very similar "
            "to the job description."
        )

    elif overall_similarity >= 75:

        overall_summary = (
            "The resume aligns well with most "
            "job requirements."
        )

    elif overall_similarity >= 60:

        overall_summary = (
            "The resume has moderate semantic "
            "alignment with the job."
        )

    else:

        overall_summary = (
            "The resume is semantically quite "
            "different from the job description."
        )

    # ==========================================
    # Matched Explanations
    # ==========================================

    matched_explanations = []

    for match in semantic_data[
        "semantic_matches"
    ]:

        matched_explanations.append(

            {
                "resume_skill":
                    match["resume_skill"],

                "job_skill":
                    match["job_skill"],

                "similarity":
                    match["similarity"],

                "explanation":
                    (
                        f"{match['resume_skill']} "
                        f"strongly aligns with "
                        f"{match['job_skill']} "
                        f"({match['similarity']}%)."
                    )
            }

        )

    # ==========================================
    # Missing Explanations
    # ==========================================

    missing_explanations = []

    for concept in semantic_data[
        "missing_concepts"
    ]:

        missing_explanations.append(

            {
                "concept": concept,

                "explanation":
                    (
                        f"The resume does not "
                        f"demonstrate sufficient "
                        f"evidence of '{concept}'."
                    )
            }

        )

    # ==========================================
    # Explainability Data Object
    # ==========================================

    return {

        "overall_summary":
            overall_summary,

        "matched_explanations":
            matched_explanations,

        "missing_explanations":
            missing_explanations

    }