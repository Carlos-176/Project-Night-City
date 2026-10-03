from django.contrib import admin
from .models import Project, PersonalInformation, Testimony, Inquiry, TechStack

admin.site.register(TechStack)
admin.site.register(Project)
admin.site.register(PersonalInformation)
admin.site.register(Testimony)
admin.site.register(Inquiry)