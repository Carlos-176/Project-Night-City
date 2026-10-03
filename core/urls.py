from django.urls import path
from . import views

urlpatterns = [
    # Public views
    path('', views.home, name='home'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('personal-info/', views.personal_information, name='personal_information'),
    path('contact/', views.inquiry_create, name='inquiry_create'),
    path('contact/success/', views.inquiry_success, name='inquiry_success'),
    path('testimonies/', views.TestimonyListView.as_view(), name='testimony_list'),
    path('testimonies/add/', views.testimony_create, name='testimony_create'),
    path('testimonies/<int:testimony_id>/', views.testimony_detail, name='testimony_detail'),

    # Superuser authentication
    path('login/', views.admin_login_view, name='admin_login'),
    path('logout/', views.admin_logout_view, name='admin_logout'),

    # Dashboard routes
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/projects/', views.dashboard_project_list, name='dashboard_projects'),
    path('dashboard/projects/create/', views.project_create_view, name='project_create'),
    path('dashboard/tech-stacks/', views.dashboard_tech_stack_list, name='dashboard_tech_stacks'),
    path('dashboard/tech-stacks/create/', views.tech_stack_create_view, name='tech_stack_create'),
]
