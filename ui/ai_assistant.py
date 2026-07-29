import streamlit as st


def render_ai_assistant(results):
    """
    Render AI Resume Assistant.
    """

    ai = results["ai_feedback"]

    with st.expander("🤖 AI Resume Assistant", expanded=True):

        st.markdown("### 📝 Professional Summary")
        st.info(ai["summary"])

        st.markdown("### ✅ Resume Strengths")

        if ai["strengths"]:
            for strength in ai["strengths"]:
                st.write(f"• {strength}")
        else:
            st.write("No strengths identified.")

        st.markdown("### ⚠ Resume Weaknesses")

        if ai["weaknesses"]:
            for weakness in ai["weaknesses"]:
                st.write(f"• {weakness}")
        else:
            st.write("No weaknesses identified.")

        st.markdown("### ❌ Missing Technologies")

        if ai["missing_technologies"]:
            for technology in ai["missing_technologies"]:
                st.write(f"• {technology}")
        else:
            st.success("No missing technologies.")

        st.markdown("### 💡 Improvement Suggestions")

        if ai["improvement_suggestions"]:
            for suggestion in ai["improvement_suggestions"]:
                st.write(f"• {suggestion}")
        else:
            st.write("No suggestions available.")

        st.markdown("### 🚀 Recommended Projects")

        if ai["recommended_projects"]:
            for project in ai["recommended_projects"]:
                st.write(f"• {project}")
        else:
            st.write("No project recommendations available.")

        st.markdown("### 🎯 Hiring Recommendation")

        st.success(ai["hiring_recommendation"])