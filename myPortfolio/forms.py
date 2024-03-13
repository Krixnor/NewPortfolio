from django import forms
from .models import Message

class MessageForm(forms.ModelForm):

    email = forms.CharField(widget = forms.TextInput(
        attrs={'type':'email',
               'placeholder': 'Enter your email',
               'name':'email'}))
    message = forms.CharField(widget = forms.Textarea(
        attrs={'type':'text',
               'placeholder': 'Write me a message',
               'cols':30,
               'rows':10}))
    
    class Meta:
        model = Message
        fields = ['email','message']
