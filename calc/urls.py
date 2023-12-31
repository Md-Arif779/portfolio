
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('resume/', views.resume, name="resume"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolio/<int:pk>/', views.portfolio_detail, name='portfolio_detail'),
    path('service/', views.service, name="service"),
    path('contact/', views.contact, name="contact"),
    path('contact/success/', views.contact_success, name='contact_success'),
   ]
