from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from .models import Resume

def HomePage(request):
    try:
        resumedata = Resume.objects.latest('created_at')
    except Resume.DoesNotExist:
        resumedata = None

    context = {
        'render_type': 'webpage',
        'resumedata': resumedata,
    }
    return render(request, 'home.html', context)

def generate_resume_pdf(request):
    try:
        resumedata = Resume.objects.latest('created_at')
    except Resume.DoesNotExist:
        resumeddata = None

    context = {
        'render_type': 'pdf',
        'resumedata': resumedata,
    }
    template = get_template('home.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

    HTML(string=html).write_pdf(response)

    return response




def Services(request):
    return render(request, 'services.html')



def Educations(request):
    return render(request, 'educations.html')



def Contact(request):
    return render(request, 'contact.html')
