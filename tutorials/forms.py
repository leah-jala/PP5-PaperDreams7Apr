from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Tutorial

class TutorialForm(forms.ModelForm):
    """
    Form to create a Tutorial
    """
    class Meta:
        model = Tutorial
        fields = [
            'title',
            'category',
            'difficulty_level',
            'duration',
            'summary',
            'equipment_list',
            'image',
            'image_alt',
        ]

        equipment_list = forms.CharField(widget=RichTextWidget())

        widget = {
            "summary": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            'title': 'Tutorial Title',
            'category': 'Select a category',
            'difficulty_level': 'Select a difficulty level',
            'duration': "Indicate the total time needed for this course",
            'summary': 'Provide a brief description of the coarse goals',
            'equipment_list': "List the equipment needed for the overall course",
            'image': "Upload an image of the finished artwork",
            'image_alt': "Describe the uploaded image"
        }


