import streamlit as st


def render_recommendations(results):
    """
    Render job role recommendations.
    """

    recommendation_data = results[
        "recommendation_data"
    ]

    st.divider()

    st.header("🎯 Career Recommendations")

    recommendations = recommendation_data[
        "recommendations"
    ]

    if not recommendations:

        st.info(
            "No recommendations available."
        )

        return

    for recommendation in recommendations:

        with st.container():

            st.subheader(
                recommendation["role"]
            )

            st.write(
                f"**Confidence:** {recommendation['confidence']}"
            )

            st.write(
                recommendation["reason"]
            )

            st.divider()