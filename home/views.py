

# Create your views here.
from django.shortcuts import render, redirect
from home.forms import ContactForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def skills(request):
    return render(request, 'skills.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'thank_you.html', {'form':form})  # Optional: Thank-you page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def resume_view(request):
    return render(request, 'resume.html')

def project(request):
    return render(request, 'projects.html')