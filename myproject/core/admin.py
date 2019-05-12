from django.contrib import admin
from .models import Repo


@admin.register(Repo)
class RepoAdmin(admin.ModelAdmin):
    list_display = (
        'slug',
        'name',
        'full_name',
        'html_url',
        'stargazers_count',
    )
    search_fields = ('name', 'full_name')
