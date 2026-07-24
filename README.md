# ATS Resume Screener

Version: 1.1

A Python-based ATS (Applicant Tracking System) Resume Screener that analyzes resumes against job descriptions, extracts technical skills, calculates an ATS compatibility score, and generates a professional screening report.

---

## Features

- PDF Resume Parsing
- Job Description Parsing
- Text Cleaning & Preprocessing
- Intelligent Skill Extraction
- Alias & Synonym Recognition
- Dynamic N-word Phrase Generation
- Canonical Skill Normalization
- Skill Matching Engine
- ATS Score Calculation
- Professional ATS Report Generation
- Report Export to Text File

---

## New in Version 1.1

Version 1.1 introduces an intelligent knowledge-based skill extraction engine.

### Improvements

- Alias Recognition
  - ML → Machine Learning
  - AWS → Amazon Web Services
  - Python3 → Python
  - Github → Git
  - Tensor Flow → TensorFlow

- Knowledge Base
  - Separate canonical skill database
  - Dedicated alias database

- Dynamic Phrase Generation
  - Single-word phrases
  - Multi-word phrases
  - Automatically adapts to the longest skill in the database

- Improved Skill Extraction
  - Tokenization
  - Phrase generation
  - Alias lookup
  - Canonical skill mapping

This significantly improves extraction accuracy compared to simple keyword matching.

---

## Project Structure

```
Resume_Screener/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── raw_skills.csv
│   └── skill_aliases.csv
│
├── resumes/
│   └── sample_resume.pdf
│
├── job_descriptions/
│   └── sample_job.txt
│
├── outputs/
│   └── ats_report.txt
│
└── utils/
    ├── pdf_reader.py
    ├── job_reader.py
    ├── text_cleaner.py
    ├── tokenizer.py
    ├── phrase_builder.py
    ├── alias_loader.py
    ├── skill_loader.py
    ├── skill_extractor.py
    ├── matcher.py
    ├── score_calculator.py
    └── report_generator.py
```

---

## Workflow

```
PDF Resume
        │
        ▼
Resume Extraction
        │
        ▼
Text Cleaning
        │
        ▼
Tokenization
        │
        ▼
Phrase Generation
        │
        ▼
Alias Lookup
        │
        ▼
Canonical Skill Extraction
        │
        ▼
Skill Matching
        │
        ▼
ATS Score Calculation
        │
        ▼
Professional ATS Report
```

---

## Technologies Used

- Python
- Regular Expressions
- pdfplumber
- Pandas
- NumPy

---

## Current Capabilities

- Resume Parsing
- Job Description Parsing
- Intelligent Skill Extraction
- Alias Recognition
- Synonym Matching
- ATS Compatibility Scoring
- Missing Skill Detection
- Additional Skill Detection
- Professional Report Generation

---

## Future Improvements

- Weighted ATS Scoring
- Experience-Based Skill Weighting
- Education Matching
- Semantic Skill Matching
- NLP-Based Resume Analysis
- Machine Learning-Based Candidate Ranking
- Resume Recommendations
- Web Interface

---

## Installation

Clone the repository

```
git clone https://github.com/Henil19/ATS-Resume-Screener.git
```

Move into the project

```
cd ATS-Resume-Screener
```

Install dependencies

```
pip install -r requirements.txt
```

Run the project

```
python app.py
```

---

## Version History

### Version 1.1

- Intelligent Skill Extraction
- Alias Recognition
- Knowledge-Based Matching
- Dynamic Phrase Generation
- Canonical Skill Mapping

### Version 1.0

- PDF Resume Reader
- Job Description Reader
- Skill Extraction
- ATS Scoring
- Professional Report Generation

---

Developed as part of an AI and Software Engineering learning project.