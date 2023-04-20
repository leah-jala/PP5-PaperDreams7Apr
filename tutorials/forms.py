from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Tutorial, TutorialPost


class TutorialForm(forms.ModelForm):
    """
    Form to create a Tutorial.

    Attributes:
        - Meta (class): A class that contains metadata
            about the form, including the model it uses,
            the fields to include, labels for the fields,
            and any widgets to use.
        - equipment_list (CharField): A field that uses the
            RichTextWidget to allow the user to input a rich
            text field.
        - widgets (dict): A dictionary that specifies any
            custom widgets to use for the fields.
        - labels (dict): A dictionary that provides
            labels for the fields.
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
            'equipment_list': "Equipment needed for the overall course",
            'image': "Upload an image of the finished artwork",
            'image_alt': "Describe the uploaded image"
        }


class TutorialPostForm(forms.ModelForm):
    """
    Form to create a step in a Tutorial.

    Attributes:
        - Meta (class): A class that contains metadata
            about the form, including the model it uses,
            the fields to include,labels for the fields,
            and any widgets to use.
        - widgets (dict): A dictionary that specifies
            any custom widgets to use for the fields.
        - labels (dict): A dictionary that provides
            labels for the fields.
    """

    class Meta:
        model = TutorialPost
        fields = [
            'tutorial',
            'week_number',
            'title',
            'instructions',
            'image',
            'image_alt',
        ]

        widgets = {
            "instructions": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            'week_number': 'Week Number',
            'title': 'Title',
            'instructions': 'Instructions',
            'image': 'Upload an image related to a step',
            'image_alt': "Describe the uploaded image.",
        }

    def __init__(self, *args, **kwargs):
        tutorial_pk = kwargs.pop('tutorial_pk', None)
        super(TutorialPostForm, self).__init__(*args, **kwargs)
        if tutorial_pk:
            self.fields['tutorial'].initial = tutorial_pk
