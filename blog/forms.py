from django import forms

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model= Contact
#         fields = ['user_name','emial','message']
#         labels ={
#             'user_name':'Your Name',
#             'emial':'Email',
#             'message':'Message'
#         }
        
class ContactForm(forms.Form):
    user_name = forms.CharField(max_length=20)
    email = forms.CharField(max_length=30)
    message = forms.CharField(max_length=500)