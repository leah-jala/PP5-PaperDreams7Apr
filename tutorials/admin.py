from django.contrib import admin
from .models import TutorialCategory, Tutorial, TutorialPost


@admin.register(TutorialCategory)
class TutorialCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name')


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    """
    Customize the display of TutorialCategory instances
    in the Django admin panel.
    """
    list_display = (
        'title',
        'instructor',
        'category',
        'difficulty_level',
        'duration',
        'created_date')
    list_filter = ('category', 'difficulty_level')
    search_fields = ('title', 'instructor__username')


@admin.register(TutorialPost)
class TutorialPostAdmin(admin.ModelAdmin):
    """
    Customize the display of Tutorial instances in
    the Django admin interface.
    """
    list_display = (
        'title',
        'instructor',
        'tutorial',
        'week_number',
        'posted_date')
    list_filter = ('tutorial', 'week_number')
    search_fields = ('title', 'instructor__username')
