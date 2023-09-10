from django.db import models
from .utils import extract_dataframes_from_pdf
from django.shortcuts import render, redirect
from .models import PDF
from .forms import PDFUploadForm


def home(request):
    return render(request, 'pdfapp/home.html')


def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_files')
    else:
        form = PDFUploadForm()
    return render(request, 'pdfapp/upload.html', {'form': form})


def view_files(request):
    pdfs = PDF.objects.all()
    return render(request, 'pdfapp/view_files.html', {'pdfs': pdfs})


def view_pdf(request, pdf_id):
    pdf = PDF.objects.get(id=pdf_id)
    # Here you can add more logic to select and process the PDF.
    return render(request, 'pdfapp/some_template.html', {'pdf': pdf})


def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.save()

            # After saving the uploaded PDF, you can run your function
            dfs = extract_dataframes_from_pdf(pdf_file.file.path)

            # Handle the dataframes as needed

            return redirect('some_view_name')
    else:
        form = PDFUploadForm()

    return render(request, 'pdfapp/upload.html', {'form': form})