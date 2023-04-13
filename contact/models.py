from django.db import models
from datetime import date

class ContactForm(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First Name*")
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Last Name")
    email = models.EmailField(max_length=254, verbose_name="Email*")
    subject = models.CharField(max_length=100, verbose_name="Subject*")
    message = models.TextField(verbose_name="Message*")
    newsletter = models.BooleanField(default=False, verbose_name="Subscribe to newsletter")
    sent_date = models.DateField(auto_now_add=True, verbose_name="Sent Date")

    class Meta:
        ordering = ['-sent_date']

    def __str__(self):
        return f"{self.first_name} {self.last_name}" if self.last_name else self.first_name
