from django.urls import path
from . import views
from .views import generate_resume_pdf


urlpatterns = [
    path('', views.HomePage, name='home'),
    path('education', views.Educations, name='education'),
    path('contact', views.ContactPage, name='contact'),
    path('generate_resume_pdf/', generate_resume_pdf, name='generate_resume_pdf'),
    ]
