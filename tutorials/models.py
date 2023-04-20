from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField


class TutorialCategory(models.Model):
    """
    A model to enable adding tutorial categories
    in the admin panel.
    """

    class Meta:
        verbose_name_plural = 'Tutorial categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """
        Returns the name of the category.
        """
        return self.name

    def get_friendly_name(self):
        """
        Returns the friendly name of the category.
        """
        return self.friendly_name


class Tutorial(models.Model):
    """
    A model to create tutorial content
    """

    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    instructor = models.ForeignKey(
        User,
        related_name='tutorials',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100, null=False, blank=False)
    category = models.ForeignKey(
        TutorialCategory,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    difficulty_level = models.CharField(
        max_length=100,
        choices=DIFFICULTY_CHOICES,
        default='beginner'
    )
    duration = models.CharField(max_length=50, null=False, blank=False)
    summary = models.CharField(max_length=100, null=False, blank=False)
    equipment_list = RichTextField(max_length=2000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to='tutorials/',
        force_format='WEBP',
        blank=False,
        null=False
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    created_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        """
        Returns the title of the tutorial.
        """
        return self.title


class TutorialPost(models.Model):
    """
    A model to create tutorial posts
    """

    tutorial = models.ForeignKey(
        Tutorial,
        related_name='posts',
        on_delete=models.CASCADE
    )
    instructor = models.ForeignKey(
        User,
        related_name='tutorial_posts',
        on_delete=models.CASCADE
    )
    week_number = models.IntegerField()
    title = models.CharField(max_length=100, null=False, blank=False)
    instructions = RichTextField(max_length=10000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to='tutorials/posts/',
        force_format='WEBP',
        blank=True,
        null=True
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    posted_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['week_number']
        unique_together = ('tutorial', 'week_number')

    def __str__(self):
        return f"Week {self.week_number}: {self.title}"
