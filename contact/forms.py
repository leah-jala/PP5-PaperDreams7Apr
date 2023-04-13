from django import forms
from .models import ContactForm

class ContactForm(forms.ModelForm):
    newsletter = forms.BooleanField(required=False, label='Subscribe to newsletter')

    class Meta:
        model = ContactForm
        fields = ['first_name', 'last_name', 'email', 'subject', 'message', 'newsletter']
        labels = {
            'first_name': 'First Name*',
            'last_name': 'Last Name',
            'email': 'Email*',
            'subject': 'Subject*',
            'message': 'Message*',
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }
