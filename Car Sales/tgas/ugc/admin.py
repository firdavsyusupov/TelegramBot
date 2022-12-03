from django.contrib import admin
from .forms import ProfileForm, MessageForm
from .models import Profile, Message, Category


@admin.register(Profile)  # List of users
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'name')
    form = ProfileForm


@admin.register(Message)  # List of requests from users
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'text',  'cat', 'created_at')
    search_fields = ('pk', 'text', 'cat__name')
    list_filter = ('created_at', 'cat__name')
    form = MessageForm


@admin.register(Category)  # Categories for the status in the application
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
