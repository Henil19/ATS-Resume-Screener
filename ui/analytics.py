import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


def render_analytics(results):
    """
    Render ATS Analytics Dashboard.
    """

    with st.expander("📈 Analytics", expanded=False):

        # -------------------------
        # ATS Score Gauge
        # -------------------------

        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=results["ats_score"],
                title={"text": "ATS Score"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"thickness": 0.3},
                    "steps": [
                        {"range": [0, 40], "color": "#ffb3b3"},
                        {"range": [40, 70], "color": "#ffe699"},
                        {"range": [70, 100], "color": "#b6f0c2"},
                    ],
                },
            )
        )

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

        # -------------------------
        # Skill Distribution
        # -------------------------

        chart_data = pd.DataFrame(
            {
                "Category": [
                    "Matched",
                    "Missing",
                    "Additional"
                ],
                "Count": [
                    len(results["matched"]),
                    len(results["missing"]),
                    len(results["extra"])
                ]
            }
        )

        col1, col2 = st.columns(2)

        with col1:

            pie = px.pie(
                chart_data,
                names="Category",
                values="Count",
                title="Skill Distribution"
            )

            st.plotly_chart(
                pie,
                use_container_width=True
            )

        with col2:

            bar = px.bar(
                chart_data,
                x="Category",
                y="Count",
                text="Count",
                title="Skill Comparison"
            )

            st.plotly_chart(
                bar,
                use_container_width=True
            )