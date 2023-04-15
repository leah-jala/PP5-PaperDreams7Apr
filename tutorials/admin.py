from django.contrib import admin
from .models import TutorialCategory, Tutorial, TutorialPost


@admin.register(TutorialCategory)
class TutorialCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name')


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
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
    list_display = (
        'title',
        'instructor',
        'tutorial',
        'week_number',
        'posted_date')
    list_filter = ('tutorial', 'week_number')
    search_fields = ('title', 'instructor__username')
