from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def skills(request):
    return render(request, 'core/skills.html')