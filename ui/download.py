import streamlit as st
import json


def render_download(results):
    """
    Render Download Section.
    """

    with st.expander("📥 Download Report", expanded=False):

        st.download_button(
            label="📄 Download ATS Report",
            data=results["report"],
            file_name="ats_report.txt",
            mime="text/plain",
            use_container_width=True
        )

        st.download_button(
            label="📦 Download Analysis (JSON)",
            data=json.dumps(results, indent=4, default=list),
            file_name="ats_analysis.json",
            mime="application/json",
            use_container_width=True
        )