from django import forms

from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model = Webpage
        #fields = '__all__'  
        #inorder to inlcude specific fields we use list of columns we need to include or we can go for exclude
        fields = ['topic_name','name','name','url'] # same as exclude = ['email']
        help_texts ={'topic_name':'should not be integrs','name':'only Alphabets'}
        labels = {'topic_name':'Topic','name':'Name'} # label for input elements
        widgets = {'url':forms.PasswordInput,'name':forms.Textarea}

class AccessRecordForm(forms.ModelForm):
    class Meta:
        model = AccessRecord
        fields = '__all__'