from django import forms
from .models import Contact, Post


class ContactForm(forms.ModelForm):
    class Meta:
        model= Contact
        fields = ['user_name','email','message']
        labels ={
            'user_name':'Your Name',
            'email':'Email',
            'message':'Message'
        }
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
       
        