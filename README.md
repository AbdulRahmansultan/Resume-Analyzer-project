# 🚀 AI Resume Analyzer

An AI-powered Resume Analyzer built using Django and Gemini AI that evaluates resumes and provides ATS score, skill analysis, missing skills, strengths, weaknesses, improvement suggestions, and suitable job roles.

---

# 📌 Features

✅ Upload PDF & DOCX resumes  
✅ AI-based ATS Resume Score  
✅ Technical Skills Analysis  
✅ Missing Skills Detection  
✅ Resume Strengths & Weaknesses  
✅ Improvement Suggestions  
✅ Best Suitable Job Roles  
✅ Beautiful Modern UI  
✅ Responsive Dashboard  
✅ Docker Support  
✅ Gemini AI Integration  

---

# 🛠️ Tech Stack

- Python
- Django
- HTML5
- CSS3
- Bootstrap 5
- Google Gemini AI
- Docker

---

# 📂 Project Structure

```bash
resume_analyzer/
│
├── analyzer/
│   ├── migrations/
│   ├── templates/
│   │   └── analyzer/
│   │       ├── index.html
│   │       └── result.html
│   │
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   │
│   ├── forms.py
│   ├── views.py
│   ├── utils.py
│   └── urls.py
│
├── resume_analyzer/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/resume-analyzer.git
```

```bash
cd resume-analyzer
```

---

# 2️⃣ Create Virtual Environment

## Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

## Linux / Mac

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

# 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 4️⃣ Create .env File

Create a `.env` file in root directory.

```env
GEMINI_API_KEY=your_api_key
```

---

# 5️⃣ Run Migrations

```bash
python manage.py migrate
```

---

# 6️⃣ Run Server

```bash
python manage.py runserver
```

Open in browser:

```bash
http://127.0.0.1:8000
```

---

# 🐳 Docker Setup

## Build Docker Image

```bash
docker compose build
```

---

## Run Docker Container

```bash
docker compose up
```

Open:

```bash
http://127.0.0.1:8000
```

---

# 📦 requirements.txt

```txt
Django
google-generativeai
PyPDF2
python-docx
gunicorn
whitenoise
python-dotenv
```

---

# 🔐 Environment Variables

| Variable | Description |
|---|---|
| GEMINI_API_KEY | Google Gemini API Key |

---

# 🧠 Gemini AI Integration

This project uses:

- Google Gemini AI API

Get API Key from:

https://ai.google.dev/

---

# 📸 Screenshots

## 🏠 Home Page

- Modern AI Landing Page
- Resume Upload UI
- Responsive Design

## 📊 Result Dashboard

- ATS Score Circle
- Skills Analysis
- Missing Skills
- Suggestions
- Job Recommendations

---

# 🚀 Deployment

This project can be deployed on:

- Render
- Railway
- Fly.io
- Docker
- VPS Servers

---

# 🔒 Security Notes

❌ Never upload `.env` file to GitHub  
❌ Never expose API keys publicly  

Add `.env` inside `.gitignore`

---

# 🌟 Future Improvements

- Resume vs Job Description Matching
- Authentication System
- Resume History
- Resume PDF Export
- AI Cover Letter Generator
- AI Interview Preparation
- Multi-language Resume Support

---

# 👨‍💻 Author

## Mohammad Abdul Rahman

Python Developer | AI Enthusiast

---

# 📄 License

This project is licensed under the MIT License.
