from django import forms

from .models import Message


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        widgets = {
            'mobile': forms.Textarea(attrs={'cols':100, 'rows': 5}),
            'text': forms.Textarea(attrs={'cols': 500, 'rows': 20}),
        }
        fields = '__all__'


