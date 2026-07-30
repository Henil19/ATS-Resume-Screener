import streamlit as st


def render_resume_rewrite(results):
    """
    Render AI Resume Rewrite Suggestions.
    """

    rewrite = results["rewrite_feedback"]

    with st.expander(
        "✍ AI Resume Rewrite",
        expanded=False
    ):

        sections = {

            "Professional Summary":
                "professional_summary",

            "Experience":
                "experience",

            "Projects":
                "projects",

            "Technical Skills":
                "technical_skills",

            "ATS Keywords":
                "ats_keywords",

            "Formatting":
                "formatting"

        }

        for title, key in sections.items():

            st.markdown(
                f"### {title}"
            )

            suggestions = rewrite.get(
                key,
                []
            )

            if suggestions:

                for suggestion in suggestions:

                    st.write(
                        f"• {suggestion}"
                    )

            else:

                st.write(
                    "No suggestions."
                )