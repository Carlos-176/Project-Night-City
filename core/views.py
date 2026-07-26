from django.shortcuts import render, get_object_or_404
from .models import Project, PersonalInformation


def home(request):
    personal_info = PersonalInformation.objects.first()
    return render(request, 'core/home.html', {'personal_info': personal_info})


def skills(request):
    return render(request, 'core/skills.html')


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'core/project_list.html', {'projects': projects})


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'core/project_detail.html', {'project': project})


def personal_information(request):
    personal_info = PersonalInformation.objects.first()
    return render(request, 'core/personal_information.html', {'personal_info': personal_info})