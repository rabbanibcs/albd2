from django.contrib import admin

from .models import Message, Email
from .forms import MessageForm


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    form = MessageForm
    list_display = ['subject', 'text', 'write_time']


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['subject', 'write_time']
