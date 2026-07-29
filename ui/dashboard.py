import streamlit as st


def render_dashboard(results):
    """
    Render ATS dashboard metrics.
    """

    st.divider()

    st.header("📊 ATS Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "ATS Score",
            f"{results['ats_score']}%"
        )

    with col2:
        st.metric(
            "Status",
            results["status"]
        )

    with col3:
        st.metric(
            "Detected Role",
            results["role"]
        )

    st.progress(
        results["ats_score"] / 100
    )