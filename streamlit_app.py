import tempfile
import os

import streamlit as st

from utils.ats_engine import run_ats_pipeline
from ui.dashboard import render_dashboard
from ui.skill_analysis import render_skill_analysis
from ui.ai_assistant import render_ai_assistant
from ui.analytics import render_analytics
from ui.download import render_download


def main():
    """
    Streamlit Web Application
    """

    st.set_page_config(
        page_title="ATS Resume Screener",
        page_icon="📄",
        layout="wide"
    )

    if "results" not in st.session_state:
        st.session_state["results"] = None

    st.title("🤖 ATS Resume Screener")

    st.caption(
        "AI-powered resume analysis with ATS scoring, skill matching, role detection, and intelligent feedback."
    )

    st.divider()

    st.subheader("📂 Upload Documents")

    st.caption(
        "Upload a resume in PDF format and a job description in TXT format."
    )

    resume_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

    job_file = st.file_uploader(
        "Upload Job Description (TXT)",
        type=["txt"]
    )

    analyze_button = st.button(
        "🚀 Analyze Resume",
        type="primary",
        use_container_width=True
    )

    if analyze_button:

        if resume_file is None:
            st.error("Please upload a resume PDF.")
            return

        if job_file is None:
            st.error("Please upload a job description.")
            return

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_resume:

            temp_resume.write(
                resume_file.getbuffer()
            )

            resume_path = temp_resume.name

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".txt"
        ) as temp_job:

            temp_job.write(
                job_file.getbuffer()
            )

            job_path = temp_job.name

        try:

            with st.status(
                "Starting analysis...",
                expanded=True
            ) as status:

                def update_progress(message):

                    status.write(message)

                st.session_state["results"] = run_ats_pipeline(
                    resume_path,
                    job_path,
                    progress_callback=update_progress
                )

                status.update(
                    label="✅ Analysis Complete",
                    state="complete"
                )

        except Exception as error:

            st.error(
                f"Analysis failed.\n\n{error}"
            )

            return

        finally:

            for path in [resume_path, job_path]:

                if os.path.exists(path):

                    os.remove(path)

        results = st.session_state["results"]
        
        render_dashboard(results)

        render_skill_analysis(results)

        render_ai_assistant(results)

        render_analytics(results)

        render_download(results)

        st.divider()

        st.caption(
            "ATS Resume Screener • Powered by Gemini AI • Built with Streamlit"
        )


if __name__ == "__main__":
    main()