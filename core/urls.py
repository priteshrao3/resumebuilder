from django.urls import path
from . import views
from .views import generate_resume_pdf


urlpatterns = [
    path('', views.HomePage, name='home'),
    path('services', views.Services, name='services'),
    path('education', views.Educations, name='education'),
    path('contact', views.Contact, name='contact'),
    path('generate_resume_pdf/', generate_resume_pdf, name='generate_resume_pdf'),
    ]
