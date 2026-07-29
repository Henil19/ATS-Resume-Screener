import streamlit as st


def render_skill_analysis(results):
    """
    Render matched, missing and additional skills.
    """

    with st.expander("🛠 Skill Analysis", expanded=True):

        col1, col2, col3 = st.columns(3)

        # -------------------------
        # Matched Skills
        # -------------------------

        with col1:

            st.success("✅ Matched Skills")

            if results["matched"]:

                for skill in sorted(results["matched"]):
                    st.write(f"• {skill.title()}")

            else:

                st.write("No matched skills found.")

        # -------------------------
        # Missing Skills
        # -------------------------

        with col2:

            st.error("❌ Missing Skills")

            if results["missing"]:

                for skill in sorted(results["missing"]):
                    st.write(f"• {skill.title()}")

            else:

                st.write("No missing skills found.")

        # -------------------------
        # Additional Skills
        # -------------------------

        with col3:

            st.info("➕ Additional Skills")

            if results["extra"]:

                for skill in sorted(results["extra"]):
                    st.write(f"• {skill.title()}")

            else:

                st.write("No additional skills found.")