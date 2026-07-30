# 🤖 ATS Resume Screener

> An AI-powered resume analysis platform that evaluates resumes against job descriptions using ATS scoring, semantic matching, explainable AI, and intelligent resume recommendations.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![Google Gemini](https://img.shields.io/badge/Google-Gemini%20AI-orange?logo=google)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📌 Overview

ATS Resume Screener is an AI-powered web application that analyzes resumes against job descriptions using both traditional ATS techniques and modern AI.

The project combines keyword-based ATS scoring with semantic similarity, explainable AI, resume rewriting suggestions, and career recommendations to provide meaningful insights for job seekers.

Unlike traditional ATS tools that rely only on keyword matching, this project uses sentence embeddings and Large Language Models (LLMs) to better understand resume quality and provide actionable feedback.

---

# ✨ Features

## 📊 ATS Analysis

- ATS Score Calculation
- Role Detection
- Role-Based Weighted Scoring
- Skill Matching
- Missing Skills Detection
- Additional Skills Detection

---

## 🧠 Semantic Analysis

- Sentence Embeddings
- Resume vs Job Description Similarity
- Semantic Skill Matching
- Missing Concept Detection

---

## 🤖 AI Resume Assistant

Powered by Google Gemini.

Provides:

- Professional Summary
- Resume Strengths
- Resume Weaknesses
- Missing Technologies
- Improvement Suggestions
- Recommended Projects
- Hiring Recommendation

---

## ✍ AI Resume Rewrite

Automatically generates suggestions for improving:

- Professional Summary
- Experience
- Projects
- Technical Skills
- ATS Keywords
- Resume Formatting

---

## 🎯 Career Recommendations

Suggests suitable job roles based on:

- Resume Skills
- ATS Score
- Semantic Similarity
- Role Confidence

---

## 📈 Analytics Dashboard

Interactive dashboard displaying:

- ATS Score
- Resume Status
- Skill Distribution
- Semantic Analysis
- Career Recommendations

---

## 📥 Download Report

Generate a complete ATS report containing:

- ATS Analysis
- Skill Analysis
- AI Feedback
- Resume Rewrite Suggestions
- Career Recommendations

---

# 🏗 System Architecture

```
                Resume PDF
                     │
                     ▼
              PDF Text Extraction
                     │
                     ▼
               Text Cleaning
                     │
                     ▼
             Skill Extraction
                     │
                     ▼
              Role Detection
                     │
                     ▼
          Weighted ATS Scoring
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
 Semantic Analysis      Explainability
          │                     │
          └──────────┬──────────┘
                     ▼
              Gemini AI Assistant
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
 Resume Rewrite  AI Feedback  Career Advice
                     │
                     ▼
             Streamlit Dashboard
```

---

# ⚙ Technology Stack

### Programming Language

- Python

### Frontend

- Streamlit

### AI

- Google Gemini API

### NLP

- Sentence Transformers

### Data Processing

- NumPy
- Pandas

### PDF Processing

- pdfplumber
- pdfminer.six

### Visualization

- Plotly

### Environment

- python-dotenv

---

# 📂 Project Structure

```
Resume_Screener/

├── data/
├── job_descriptions/
├── outputs/
├── prompts/
├── providers/
├── resumes/
├── tests/
├── ui/
├── utils/
├── app.py
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Henil19/ATS-Resume-Screener.git
```

Move into the project directory

```bash
cd ATS-Resume-Screener
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
GEMINI_MODEL=gemini-2.5-flash
```

---

# ▶ Running the Application

Launch the Streamlit application

```bash
streamlit run streamlit_app.py
```

---

# 🧪 Running Tests

Execute the complete test suite

```bash
python -m tests.run_phase7_tests
```

---

# 📈 Development Journey

The project was developed in multiple phases:

- ✅ Phase 1 – ATS Resume Parsing
- ✅ Phase 2 – ATS Scoring Engine
- ✅ Phase 3 – Intelligent Skill Extraction
- ✅ Phase 4 – Role Detection
- ✅ Phase 5 – AI Resume Assistant
- ✅ Phase 6 – Streamlit Web Application
- ✅ Phase 7 – Semantic Analysis & AI Resume Rewrite

---

# 🛣 Future Roadmap

Planned improvements include:

- Embedding Cache
- Recruiter Dashboard
- Multi Resume Comparison
- Batch Resume Processing
- Cover Letter Generator
- Interview Preparation Assistant
- LinkedIn Profile Optimizer
- Job Recommendation APIs

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Henil Patel**

---

## ⭐ If you found this project useful, consider giving it a star!