from django import forms
from .models import Topic,Entry

class TopicForm(forms.ModelForm): # TopicForm extends forms.ModelForm
    class Meta: # django-specific
        model = Topic # base form on Topic
        fields = ['text'] # form only takes one field called 'text'
        labels = {'text': ''} # not generate lable for 'text'

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # widget is html form
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} # tells django to override default col size of 40 to 80