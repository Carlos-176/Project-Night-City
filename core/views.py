from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .forms import ProjectForm, InquiryForm, TestimonyForm
from .models import Project, PersonalInformation, Testimony


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


def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()

    return render(request, 'core/project_form.html', {'form': form})


def personal_information(request):
    personal_info = PersonalInformation.objects.first()
    return render(
        request,
        'core/personal_information.html',
        {'personal_info': personal_info}
    )


def inquiry_create(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('inquiry_success')
    else:
        form = InquiryForm()

    return render(request, 'core/inquiry_form.html', {'form': form})


def inquiry_success(request):
    return render(request, 'core/inquiry_success.html')


def testimony_create(request):
    if request.method == 'POST':
        form = TestimonyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('testimony_list')
    else:
        form = TestimonyForm()

    return render(request, 'core/testimony_form.html', {'form': form})


class TestimonyListView(ListView):
    model = Testimony
    template_name = 'core/testimony_list.html'
    context_object_name = 'testimonies'


def testimony_detail(request, testimony_id):
    testimony = get_object_or_404(Testimony, id=testimony_id)

    return render(
        request,
        'core/testimony_detail.html',
        {'testimony': testimony}
    )