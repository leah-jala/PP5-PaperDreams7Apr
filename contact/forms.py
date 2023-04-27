from django import forms
from .models import ContactForm


class ContactForm(forms.ModelForm):
    """
    Customizes the display and functionality of
    the ContactForm model.
    """
    class Meta:
        model = ContactForm
        fields = [
            'first_name',
            'last_name',
            'email',
            'subject',
            'message',
            'newsletter']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Message',
            'newsletter': 'Subscribe to newsletter',
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }
        crispy = {
            'helper': 'helper-form',
            'form_method': 'post',
            'form_class': 'contact-form',
            'label_class': 'form-label',
            'field_class': 'form-input',
            'button_class': 'btn btn-primary',
            'helper_class': 'form-text',
            'error_class': 'form-error',
            'success_class': 'form-success',
        }
