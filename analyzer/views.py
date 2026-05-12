from django.shortcuts import render

# Create your views here.

from .forms import ResumeUploadForm

from.utils import (
    extract_pdf_text,
    extract_docx_text,
    analyze_resume
)

def home(request):

    result = None

    if request.method == "POST":
        
        form = ResumeUploadForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            resume_file = request.FILES["resume"]

            file_name = resume_file.name.lower()

            #PDF File

            if file_name.endswith(".pdf"):

                resume_text = extract_pdf_text(
                    resume_file
                )

            #Docx File
            elif file_name.endswith(".docx"):

                resume_text = extract_docx_text(
                    resume_file
                )
            else:
                result = "Unsupported File Format"

                return render(
                    request,"analyzer/result.html", {"result":result}
                )
            #AI Analysis
            result = analyze_resume(
                resume_text
            )

            return render(
                request,"analyzer/result.html",
                {"result": result}
     
           )
    else:    
        form = ResumeUploadForm()

    return render(request,"analyzer/index.html",{"form": form})