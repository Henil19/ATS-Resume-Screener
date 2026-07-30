import streamlit as st


def render_semantic_analysis(results):
    """
    Render Semantic Analysis.
    """

    semantic = results["semantic_data"]

    explainability = results[
        "explainability_data"
    ]

    st.divider()

    st.header("🧠 Semantic Analysis")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Overall Similarity",
            f"{semantic['overall_similarity']}%"
        )

    with col2:

        st.metric(
            "Semantic Matches",
            len(
                semantic["semantic_matches"]
            )
        )

    st.markdown(
        "### 📋 Overall Summary"
    )

    st.info(
        explainability[
            "overall_summary"
        ]
    )

    st.markdown(
        "### ✅ Semantic Matches"
    )

    if explainability[
        "matched_explanations"
    ]:

        for match in explainability[
            "matched_explanations"
        ]:

            st.success(
                match["explanation"]
            )

    else:

        st.write(
            "No semantic matches."
        )

    st.markdown(
        "### ❌ Missing Concepts"
    )

    if explainability[
        "missing_explanations"
    ]:

        for concept in explainability[
            "missing_explanations"
        ]:

            st.warning(
                concept["explanation"]
            )

    else:

        st.success(
            "No missing concepts."
        )