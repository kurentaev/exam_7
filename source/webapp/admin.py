from django.contrib import admin

from webapp.models import GuestsList


class GuestsListAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'email', 'content', 'created_at', 'status']
    list_filter = ['author', 'email']
    search_fields = ['author', 'email']
    fields = ['author', 'email', 'content', 'created_at', 'status']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(GuestsList, GuestsListAdmin)
