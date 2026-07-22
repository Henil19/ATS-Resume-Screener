# ATS Resume Screener

Version: 1.0 (Initial Stable Release)

A modular Python-based Applicant Tracking System (ATS) that analyzes resumes against job descriptions, extracts technical skills, calculates an ATS compatibility score, and generates a professional screening report.

---

## Features

- Read resume content from PDF files
- Read job descriptions from text files
- Clean and normalize extracted text
- Load skills from a customizable skills database
- Extract technical skills from resumes and job descriptions
- Compare resume skills against job requirements
- Calculate an ATS compatibility score
- Classify candidates as:
  - Strong Match
  - Moderate Match
  - Low Match
- Generate a professional ATS report
- Save reports automatically to the outputs folder
- Debug mode for development and testing

---

## Project Structure

```
Resume_Screener/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── raw_skills.csv
│
├── resumes/
│   └── sample_resume.pdf
│
├── job_descriptions/
│   └── sample_job.txt
│
├── outputs/
│
└── utils/
    ├── pdf_reader.py
    ├── job_reader.py
    ├── text_cleaner.py
    ├── skill_loader.py
    ├── skill_extractor.py
    ├── matcher.py
    ├── score_calculator.py
    └── report_generator.py
```

---

## Technologies Used

- Python 3
- pdfplumber
- pandas
- Regular Expressions (re)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ATS-Resume-Screener.git
```

Navigate to the project:

```bash
cd ATS-Resume-Screener
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python app.py
```

---

## Current Workflow

Resume PDF

↓

Extract Resume Text

↓

Read Job Description

↓

Clean Text

↓

Load Skills Database

↓

Extract Skills

↓

Compare Skills

↓

Calculate ATS Score

↓

Generate ATS Report

↓

Save Report

---

## Sample Output

The application generates:

- ATS Compatibility Score
- Candidate Status
- Matched Skills
- Missing Skills
- Additional Skills

and automatically saves the report inside the `outputs` folder.

---

## Current Version

**Version 1.0**

Completed:

- Phase 1 – Core ATS Engine
- Phase 2 – ATS Scoring Engine

---

## Planned Improvements

- Intelligent skill extraction
- Skill synonym matching
- Weighted ATS scoring
- Resume feedback and suggestions
- Streamlit web interface
- AI-powered semantic matching
- Resume ranking for multiple candidates
- Support for DOCX resumes
- Job description import from online platforms

---

## Author

Henil Patel

---

## License

This project is intended for educational and portfolio purposes.