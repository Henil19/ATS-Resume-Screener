def generate_report(
    ats_score,
    status,
    matched,
    missing,
    extra,
    ai_feedback
):
    """
    Generates a formatted ATS + AI report.
    """

    report = ""

    # ==========================
    # ATS REPORT
    # ==========================

    report += "=" * 50 + "\n"
    report += "         ATS RESUME SCREENING REPORT\n"
    report += "=" * 50 + "\n\n"

    report += f"ATS SCORE : {ats_score}%\n"
    report += f"STATUS    : {status}\n\n"

    report += "=" * 50 + "\n"
    report += f"MATCHED SKILLS ({len(matched)})\n"
    report += "=" * 50 + "\n"

    if matched:
        for skill in sorted(matched):
            report += f"✓ {skill.title()}\n"
    else:
        report += "No matched skills found.\n"

    report += "\n"

    report += "=" * 50 + "\n"
    report += f"MISSING SKILLS ({len(missing)})\n"
    report += "=" * 50 + "\n"

    if missing:
        for skill in sorted(missing):
            report += f"✗ {skill.title()}\n"
    else:
        report += "No missing skills.\n"

    report += "\n"

    report += "=" * 50 + "\n"
    report += f"ADDITIONAL SKILLS ({len(extra)})\n"
    report += "=" * 50 + "\n"

    if extra:
        for skill in sorted(extra):
            report += f"• {skill.title()}\n"
    else:
        report += "No additional skills.\n"

    report += "\n"

    # ==========================
    # AI REPORT
    # ==========================

    report += "=" * 50 + "\n"
    report += "          AI RESUME ASSISTANT\n"
    report += "=" * 50 + "\n\n"

    report += "PROFESSIONAL SUMMARY\n"
    report += "-" * 50 + "\n"
    report += ai_feedback.get("summary","No summary available.") + "\n\n"

    report += "RESUME STRENGTHS\n"
    report += "-" * 50 + "\n"

    if ai_feedback.get("strengths", []):
        for strength in ai_feedback.get("strengths", []):
            report += f"✓ {strength}\n"
    else:
        report += "No strengths identified.\n"

    report += "\n"

    report += "RESUME WEAKNESSES\n"
    report += "-" * 50 + "\n"

    if ai_feedback.get("weaknesses", []):
        for weakness in ai_feedback.get("weaknesses", []):
            report += f"• {weakness}\n"
    else:
        report += "No weaknesses identified.\n"

    report += "\n"

    report += "MISSING TECHNOLOGIES\n"
    report += "-" * 50 + "\n"

    if ai_feedback.get("missing_technologies", []):
        for technology in ai_feedback.get("missing_technologies", []):
            report += f"✗ {technology}\n"
    else:
        report += "No missing technologies.\n"

    report += "\n"

    report += "IMPROVEMENT SUGGESTIONS\n"
    report += "-" * 50 + "\n"

    if ai_feedback.get("improvement_suggestions", []):
        for suggestion in ai_feedback.get("improvement_suggestions", []):
            report += f"→ {suggestion}\n"
    else:
        report += "No suggestions available.\n"

    report += "\n"

    report += "PROJECT RECOMMENDATIONS\n"
    report += "-" * 50 + "\n"

    if ai_feedback.get("recommended_projects", []):
        for project in ai_feedback.get("recommended_projects", []):
            report += f"★ {project}\n"
    else:
        report += "No project recommendations.\n"

    report += "\n"

    report += "HIRING RECOMMENDATION\n"
    report += "-" * 50 + "\n"
    report += ai_feedback.get("hiring_recommendation","No recommendation available.") + "\n\n"

    return report


def save_report(report, output_path):
    """
    Saves the ATS report to a text file.
    """

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report)