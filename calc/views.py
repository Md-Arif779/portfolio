from django.shortcuts import render, redirect
from .models import Profile, About, Skill
from .forms import ContactForm
# Create your views here.


def home(request):
    profile_data = Profile.objects.first()
    skills_data = Skill.objects.all()

    context = {
        'profile_data': profile_data,
        'skills_data': skills_data,
    }
    return render(request, 'home.html', context)

def about(request):
    about_data = About.objects.first()
    profile_data = Profile.objects.first()
    skills_data = Skill.objects.all()
    context = {
        'about_data': about_data,
        'skills_data': skills_data,
        'profile_data': profile_data,
    }
    return render(request, 'about.html', context)
    

def resume(request):

    return render(request, 'resume.html')

def portfolio(request):

    return render(request, 'portfolio.html')

def service(request):

    return render(request, 'service.html')







def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def contact_success(request, success_message=None):
    return render(request, 'contact_success.html')
