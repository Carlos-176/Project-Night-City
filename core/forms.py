from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from .models import Project, TechStack, Inquiry, Testimony


class AdminLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        # Requirement: Superuser/admin only. Deny regular users even if their account exists.
        if not user.is_superuser:
            raise ValidationError(
                "Access restricted to admin/superuser accounts only.",
                code="not_superuser",
            )


class TechStackForm(forms.ModelForm):
    class Meta:
        model = TechStack
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Python'}),
        }


class ProjectForm(forms.ModelForm):
    # Requirement: Tech Stacks must use radio buttons and fetch all tech stack objects
    tech_stacks = forms.ModelMultipleChoiceField(
        queryset=TechStack.objects.all(),
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        required=True,
    )

    class Meta:
        model = Project
        fields = ['project_name', 'description', 'tech_stacks', 'link']
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
        }


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = "__all__"


class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = "__all__"
