from django.contrib import admin
from .models import ContactForm


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = [
        'sent_date',
        'last_name',
        'first_name',
        'email',
        'subject',
        'newsletter',
    ]
    list_filter = ['newsletter', 'sent_date']
    search_fields = ['first_name', 'last_name', 'email', 'subject']
