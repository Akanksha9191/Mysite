from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.views.generic import View, TemplateView

class blog_content(TemplateView):
    template_name = "blog/introduction.html"

class blog_allpost(TemplateView):
    template_name = "blog/allpost.html"
    
class blog_postdetails(TemplateView):
    template_name ="blog/postdetails.html"

class contact_view(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'blog/contactform.html',{
            'form':form
        })

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('thank-you')
    
        return render(request, 'blog/contactform.html',{
            'form':form
        })
        
class thankyou(TemplateView):
    template_name = "blog/thankyou.html"


