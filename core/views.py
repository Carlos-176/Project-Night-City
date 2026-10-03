from functools import wraps
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView

from .forms import AdminLoginForm, ProjectForm, TechStackForm, InquiryForm, TestimonyForm
from .models import Project, TechStack, PersonalInformation, Testimony


def superuser_required(view_func):
    """Restricts access to superusers only; redirects to admin_login otherwise."""
    @wraps(view_func)
    @login_required(login_url='admin_login')
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied("Access restricted to admin/superuser accounts.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def admin_login_view(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AdminLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AdminLoginForm()

    return render(request, 'core/login.html', {'form': form})


def admin_logout_view(request):
    logout(request)
    return redirect('admin_login')


# Dashboard Views (Admin/Superuser only)
@superuser_required
def dashboard_view(request):
    projects = Project.objects.prefetch_related('tech_stacks').all()
    tech_stacks = TechStack.objects.prefetch_related('projects').all()
    return render(request, 'core/dashboard.html', {
        'projects': projects,
        'tech_stacks': tech_stacks,
    })


@superuser_required
def dashboard_project_list(request):
    projects = Project.objects.prefetch_related('tech_stacks').all()
    return render(request, 'core/dashboard_projects.html', {'projects': projects})


@superuser_required
def dashboard_tech_stack_list(request):
    tech_stacks = TechStack.objects.prefetch_related('projects').all()
    return render(request, 'core/dashboard_tech_stacks.html', {'tech_stacks': tech_stacks})


@superuser_required
def project_create_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_projects')
    else:
        form = ProjectForm()

    return render(request, 'core/project_create.html', {'form': form})


@superuser_required
def tech_stack_create_view(request):
    if request.method == 'POST':
        form = TechStackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_tech_stacks')
    else:
        form = TechStackForm()

    return render(request, 'core/tech_stack_create.html', {'form': form})


# Public Portfolio Views
def home(request):
    personal_info = PersonalInformation.objects.first()
    return render(request, 'core/home.html', {'personal_info': personal_info})


def skills(request):
    tech_stacks = TechStack.objects.all()
    return render(request, 'core/skills.html', {'tech_stacks': tech_stacks})


def project_list(request):
    projects = Project.objects.prefetch_related('tech_stacks').all()
    return render(request, 'core/project_list.html', {'projects': projects})


def project_detail(request, project_id):
    project = get_object_or_404(Project.objects.prefetch_related('tech_stacks'), id=project_id)
    return render(request, 'core/project_detail.html', {'project': project})


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
    return render(request, 'core/testimony_detail.html', {'testimony': testimony})
