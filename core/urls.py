from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('skills/', views.skills, name='skills'),

    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('projects/add/', views.project_create, name='project_create'),

    path('personal-info/', views.personal_information, name='personal_information'),

    path('contact/', views.inquiry_create, name='inquiry_create'),
    path('contact/success/', views.inquiry_success, name='inquiry_success'),

    path('testimonies/', views.TestimonyListView.as_view(), name='testimony_list'),
    path('testimonies/add/', views.testimony_create, name='testimony_create'),
    path('testimonies/<int:testimony_id>/', views.testimony_detail, name='testimony_detail'),
]