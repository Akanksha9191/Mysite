from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
from .models import Contact
from django.views.generic import View

# Create your views here.
def blog_content(request):
    return render(request, 'blog/introduction.html')

def blog_allpost(request):
    return render(request, 'blog/allpost.html')
def blog_postdetails(request):
    return render(request, 'blog/postdetails.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            formdata = Contact(
                user_name =form.cleaned_data['user_name'],
                email = form.cleaned_data['email'],
                message= form.cleaned_data['message']
            )
            formdata.save()
            return HttpResponseRedirect('/thank-you')
        
    form = ContactForm()  
    return render(request, 'blog/contactform.html',
                  {
                    'form':form
                  }
                 )
    
# class contact_view(View):
#     def get(self, request):
#         form = ContactForm()
#         return render(request, 'blog/contactform.html',{
#             'form':form
#         })

#     def post(self, request):
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/thank-you')
    
#         return render(request, 'blog/contactform.html',{
#             'form':form
#         })
        
# def thankyou(request):
#     return render(request, 'blog/thankyou.html')

