# 🤖 ATS Resume Screener with AI Resume Assistant

An intelligent Applicant Tracking System (ATS) built in Python that analyzes resumes against job descriptions using weighted skill matching and AI-powered career feedback.

Version 5 introduces an AI Resume Assistant powered by Google's Gemini API, providing professional resume analysis, improvement suggestions, and hiring recommendations.

---

# 🚀 Features

## ATS Engine

- Resume PDF parsing
- Job description parsing
- Text preprocessing
- Skill extraction using aliases
- Role detection
- Role-based weighted ATS scoring
- Matched skills analysis
- Missing skills analysis
- Additional skills detection
- Professional ATS report generation

---

## AI Resume Assistant

Powered by **Google Gemini 3.6 Flash**

Generates:

- Professional Summary
- Resume Strengths
- Resume Weaknesses
- Missing Technologies
- Improvement Suggestions
- Project Recommendations
- Hiring Recommendation

---

# 🏗 Project Architecture

```
Resume PDF
      │
      ▼
PDF Reader
      │
      ▼
Text Cleaner
      │
      ▼
Skill Extractor
      │
      ▼
Role Detection
      │
      ▼
Role Weight Loader
      │
      ▼
Weighted ATS Engine
      │
      ▼
ATS Data Builder
      │
      ▼
AI Resume Assistant
      │
      ▼
Gemini API
      │
      ▼
Structured AI JSON
      │
      ▼
Report Generator
      │
      ▼
Professional ATS Report
```

---

# 📂 Project Structure

```
Resume_Screener/

├── app.py
│
├── providers/
│   ├── __init__.py
│   └── gemini_provider.py
│
├── prompts/
│   └── resume_assistant_prompt.txt
│
├── resumes/
│
├── job_descriptions/
│
├── outputs/
│
├── tests/
│
├── utils/
│
├── data/
│   ├── role_weights/
│   ├── raw_skills.csv
│   ├── role_aliases.csv
│   └── skill_aliases.csv
│
├── requirements.txt
│
└── README.md
```

---

# ⚙ Technologies Used

- Python
- Google Gemini API
- pdfplumber
- Pandas
- NumPy
- Regular Expressions
- JSON
- python-dotenv

---

# 📊 Example Output

```
ATS SCORE : 100%

STATUS : STRONG MATCH

Matched Skills

✓ Python
✓ Docker
✓ Git
✓ AWS

...

AI Resume Assistant

Professional Summary

The candidate is an ideal match...

Resume Strengths

✓ Strong cloud knowledge
✓ Excellent ML background

Hiring Recommendation

Strong Interview Recommendation
```

---

# 🧪 Testing

Dedicated test files are included for:

- ATS Data Builder
- Gemini Provider
- AI Resume Assistant

Run tests using:

```bash
python -m tests.test_ats_data_builder

python -m tests.test_gemini_provider

python -m tests.test_ai_resume_assistant
```

---

# 🔧 Installation

Clone the repository:

```bash
git clone <repository-url>

cd Resume_Screener
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY

GEMINI_MODEL=gemini-3.6-flash
```

Run the project:

```bash
python app.py
```

---

# 📈 Development Timeline

### ✅ Phase 1

Resume Parsing

### ✅ Phase 2

ATS Scoring Engine

### ✅ Phase 3

Intelligent Skill Extraction

### ✅ Phase 4

Role-Based Weighted ATS

### ✅ Phase 5

AI Resume Assistant

---

# 🔮 Planned Features

- Experience Scoring
- Education Scoring
- Certification Scoring
- Semantic Skill Matching
- Resume Rewriting
- Cover Letter Generation
- Web Dashboard
- Multi-LLM Support
- REST API
- Docker Deployment

---

# 👨‍💻 Author

Henil Patel

# 📄 License

This project is intended for educational, research, and portfolio purposes.