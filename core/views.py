from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from .models import Resume
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse

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




def Educations(request):
    context = {
        'render_type': 'webpage',
    }
    return render(request, 'educations.html', context)


# Contact Us Pages View
def ContactPage(request):
    context = {'render_type': 'webpage'}
    
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        mobile = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('value1')
        message = request.POST.get('message')
        
        email_content = f"First Name: {firstname} \n\nLast Name: {lastname} \n\nEmail: {email} \n\nPhone No.: {mobile} \n\n{message}"
        
        try:
            send_mail(
                subject,
                email_content,
                settings.EMAIL_HOST_USER,
                ['priteshrao3@gmail.com'],
                fail_silently=False,
            )
            return JsonResponse({'message': 'Message sent successfully!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return render(request, 'contact.html', context)