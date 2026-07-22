def generate_report(
    ats_score,
    status,
    matched,
    missing,
    extra
):
    """
    Generates a formatted ATS report.
    """

    report = ""

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

    return report

def save_report(report, output_path):
    """
    Saves the ATS report to a text file.
    """

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report)