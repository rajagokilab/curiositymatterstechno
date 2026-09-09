from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        # Add 'phone_number' to the fields list
        fields = ['name', 'email', 'phone_number', 'project_type', 'message']