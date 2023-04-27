from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """
    Display a contact form and handle form submissions.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Thank you for your message!'
                ' We will be in touch soon.'
                )
            return redirect('contact')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    return render(request, template, {'form': form})
