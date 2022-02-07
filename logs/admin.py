from django.contrib import admin

from .models import Error


@admin.register(Error)
class ErrorAdmin(admin.ModelAdmin):
    list_display = 'id', 'user', 'category', 'url', 'error', 'ip', 'date'
    list_filter = 'category',
    list_per_page = 10
    readonly_fields = 'user', 'category', 'url', 'error', 'ip', 'date'
    search_fields = '=user',
    show_full_result_count = False

