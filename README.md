# 🤖 ATS Resume Screener

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red)
![Gemini](https://img.shields.io/badge/Google-Gemini_AI-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

An AI-powered Applicant Tracking System (ATS) Resume Screener that evaluates resumes against job descriptions using intelligent skill extraction, weighted ATS scoring, role detection, and Gemini-powered resume feedback.

Built with **Python**, **Streamlit**, **Google Gemini**, and **Plotly**, this project transforms a traditional terminal-based ATS checker into a professional interactive web application.

---

## ✨ Features

### 📄 Resume Processing
- Upload PDF resumes
- Upload TXT job descriptions
- Automatic text extraction
- Text cleaning and normalization

### 🎯 Intelligent Skill Matching
- Alias-based skill extraction
- Phrase matching
- Resume vs Job skill comparison
- Matched skills
- Missing skills
- Additional skills

### 🧠 Role Detection
- Automatic job role detection
- Role alias resolution
- Role-specific skill weighting
- Weighted ATS score calculation

### 🤖 AI Resume Assistant (Gemini)
- Professional resume summary
- Resume strengths
- Resume weaknesses
- Missing technologies
- Improvement suggestions
- Project recommendations
- Hiring recommendation

### 📊 Analytics Dashboard
- ATS score gauge
- Skill distribution charts
- Interactive Plotly visualizations

### 🌐 Professional Web Application
- Streamlit interface
- Progress tracking
- Error handling
- Session state management
- Download reports
- Responsive layout

---

# 🏗 Architecture

```
                Resume PDF
                     │
                     ▼
              PDF Text Extractor
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
        Weighted ATS Score Engine
                     │
                     ▼
          ATS Data Construction
                     │
                     ▼
          Gemini AI Resume Assistant
                     │
                     ▼
            Streamlit Dashboard
```

---

# 📁 Project Structure

```
Resume_Screener/
│
├── app.py
├── streamlit_app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── role_aliases.csv
│   ├── skill_aliases.csv
│   └── role_weights/
│
├── job_descriptions/
│
├── outputs/
│
├── prompts/
│
├── providers/
│   └── gemini_provider.py
│
├── resumes/
│
├── tests/
│   └── test_ats_engine.py
│
├── ui/
│   ├── dashboard.py
│   ├── skill_analysis.py
│   ├── ai_assistant.py
│   ├── analytics.py
│   └── download.py
│
└── utils/
    ├── ai_resume_assistant.py
    ├── ats_data_builder.py
    ├── ats_engine.py
    ├── alias_loader.py
    ├── job_reader.py
    ├── matcher.py
    ├── pdf_reader.py
    ├── report_generator.py
    ├── role_detector.py
    ├── role_resolver.py
    ├── role_weight_loader.py
    ├── skill_extractor.py
    ├── text_cleaner.py
    ├── tokenizer.py
    └── weighted_score_calculator.py
```

---

# ⚙ Installation

Clone the repository.

```bash
git clone https://github.com/Henil19/ATS-Resume-Screener.git
```

Go into the project.

```bash
cd ATS-Resume-Screener
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your Google Gemini API key.

---

# 🚀 Running the Application

Launch the Streamlit application.

```bash
streamlit run streamlit_app.py
```

The application will automatically open in your browser.

---

# 📋 Workflow

1. Upload Resume (PDF)
2. Upload Job Description (TXT)
3. Click **Analyze Resume**
4. ATS Engine processes both documents
5. Role is detected automatically
6. Weighted ATS score is calculated
7. Gemini AI generates resume feedback
8. Interactive dashboard displays results
9. Download the ATS report

---

# 📊 Outputs

The application generates:

- ATS Score
- Matching Status
- Detected Role
- Matched Skills
- Missing Skills
- Additional Skills
- AI Resume Summary
- Strengths
- Weaknesses
- Improvement Suggestions
- Recommended Projects
- Hiring Recommendation

---

# 🛠 Tech Stack

### Languages
- Python

### Frontend
- Streamlit

### AI
- Google Gemini

### Data Processing
- Pandas
- NumPy

### PDF Processing
- pdfplumber
- pdfminer.six

### Visualization
- Plotly

### Environment Management
- python-dotenv

---

# 🧪 Testing

The project has been tested for:

- ✅ Valid resume analysis
- ✅ Missing resume upload
- ✅ Missing job description
- ✅ Invalid PDF handling
- ✅ Empty job description
- ✅ Strong resume matching
- ✅ Weak resume matching
- ✅ Report downloads
- ✅ Analytics rendering
- ✅ AI feedback generation
- ✅ Temporary file cleanup
- ✅ Responsive Streamlit interface

---

# 🗺 Roadmap

## ✅ Phase 1
Core ATS Pipeline

## ✅ Phase 2
Professional ATS Scoring Engine

## ✅ Phase 3
Intelligent Skill Extraction

## ✅ Phase 4
Weighted ATS Scoring & Role Detection

## ✅ Phase 5
AI Resume Assistant (Gemini)

## ✅ Phase 6
Professional Streamlit Web Application

## 🚧 Phase 7
Advanced Resume Intelligence

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

# 📜 License

This project is licensed under the MIT License.

---