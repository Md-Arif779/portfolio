from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .models import Profile, About, Skill, PortfolioItem
from .forms import ContactForm
# Create your views here.


def home(request):
    profile_data = Profile.objects.first()
    skills_data = Skill.objects.all()
    about_data = About.objects.first()
    

    categories = ["Web", "App", "Card", "Software"]  
    selected_category = request.GET.get("category", "All")

    if selected_category == "All":
        portfolio_items = PortfolioItem.objects.all()
    else:
        portfolio_items = PortfolioItem.objects.filter(category__iexact=selected_category)

    context = {
        'profile_data': profile_data,
        'skills_data': skills_data,
        'about_data': about_data,
        'portfolio_items': portfolio_items,
        'categories': categories,
        'selected_category': selected_category,
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
    profile_data = Profile.objects.first()

    context = {
        'profile_data': profile_data,
    }

    return render(request, 'resume.html', context)


def portfolio(request):
    profile_data = Profile.objects.first()
    categories = ["Web", "App", "Card", "Software"]
    selected_category = request.GET.get("category", "All")
    

    if selected_category == "All":
        portfolio_items = PortfolioItem.objects.all()
    else:
        portfolio_items = PortfolioItem.objects.filter(category__iexact=selected_category)

    context = {
        'portfolio_items': portfolio_items,
        'categories': categories,
        'selected_category': selected_category,
        'profile_data': profile_data,
    }

    return render(request, 'portfolio.html', context)

def portfolio_detail(request, pk):
    portfolio_item = get_object_or_404(PortfolioItem, pk=pk)
    profile_data = Profile.objects.first()

    context = {
        'portfolio_item': portfolio_item,
        'profile_data': profile_data,
        
    }

    return render(request, 'portfolio_details.html', context)


def service(request):
    profile_data = Profile.objects.first()

    context = {
       'profile_data': profile_data, 
    }
    return render(request, 'service.html', context)


def contact(request):
    profile_data = Profile.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('contact_success')
    else:
        form = ContactForm()

    context = {
        'form': form,
        'profile_data': profile_data,
    }
    return render(request, 'contact.html', context)

def contact_success(request, success_message=None):
    profile_data = Profile.objects.first()
    context = {
        'profile_data': profile_data,
    }
    return render(request, 'contact_success.html', context)
