from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    company_name = forms.CharField(max_length=50, required=True)
    contact_number = forms.CharField(max_length=10, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'company_name', 'contact_number']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.company_name = self.cleaned_data['company_name']
        user.contact_number = self.cleaned_data['contact_number']
        if commit:
            user.save()
