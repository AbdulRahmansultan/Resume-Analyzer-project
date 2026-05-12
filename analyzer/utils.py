import google.generativeai as genai
import PyPDF2
import docx
import json

genai.configure(
    api_key="Your-API-KEY"
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def extract_pdf_text(file):

    text = ""

    pdf_reader = PyPDF2.PdfReader(file)

    for page in pdf_reader.pages:

        extracted = page.extract_text()

        if extracted:
            text += extracted

    return text


def extract_docx_text(file):

    doc = docx.Document(file)

    text = ""

    for para in doc.paragraphs:

        text += para.text + "\n"

    return text


def analyze_resume(resume_text):

    prompt = f"""
    Analyze the resume and return ONLY valid JSON.

    Format:

    {{
        "resume_score": 85,

        "technical_skills": [
            {{
                "skill": "Python",
                "percentage": 90
            }},
            {{
                "skill": "Django",
                "percentage": 80
            }}
        ],

        "missing_skills": [
            {{
                "skill": "Docker",
                "percentage": 40
            }}
        ],

        "strengths": [],

        "weaknesses": [],

        "suggestions": [],

        "job_roles": []
    }}

    Resume:
    {resume_text}
    """

    response = model.generate_content(prompt)

    cleaned_response = response.text.strip()

    cleaned_response = cleaned_response.replace(
        "```json",
        ""
    )

    cleaned_response = cleaned_response.replace(
        "```",
        ""
    )

    data = json.loads(cleaned_response)

    return data