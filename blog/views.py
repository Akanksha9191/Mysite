from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .forms import ContactForm, PostForm
from .models import Post, Contact
from django.views.generic import View, TemplateView, ListView


            

    
# all post
# class blog_allpost(TemplateView):
#     template_name = "blog/allpost.html"




# contact form
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
            return HttpResponseRedirect('thankyou')

        form = ContactForm()
        return render(request, 'blog/contactform.html',{
            'form':form
        })


# upload details
class post_upload_form(View):
    def get(self, request):
        uploadform = PostForm()
        return render(request, 'blog/upload_post.html',{
            'uploadform':uploadform
        })

    def post(self, request):
        uploadform = PostForm(request.POST, request.FILES)
        if uploadform.is_valid():
            uploadform.save()
            return HttpResponseRedirect('allpost')
        
        uploadform = PostForm()
        return render(request, 'blog/upload_post.html',{
            'uploadform':uploadform
        })

class all_post(ListView):
    model = Post
    context_object_name = 'details'
    template_name='blog/allpost.html'
    
# thank you 
class thankyou(TemplateView):
    template_name = "blog/thankyou.html"
# def thankyou(request, id):
#     contact = Contact.objects.get(pk=id)
#     print(contact)
#     return render(request, 'blog/postdetails.html',{
#         'user_name':contact.user_name
#     })


# introduction 
class blog_content(ListView):
    model = Post
    context_object_name = 'details'
    template_name = "blog/introduction.html"
    
    def get_queryset(self):
        return Post.objects.all()[:3]
    
# def blog_content(request):
#     details = Post.objects.all()[:3]
#     return render(request, 'blog/introduction.html',
#                   {
#                       'details':details
#                   })

 
# post details 
# class blog_postdetails(ListView):
#     model = Post
#     context_object_name = 'details'
#     template_name ="blog/postdetails.html"

def blog_postdetails(request, id):
    try:
        post=Post.objects.get(pk=id)
        print(post)
        return render(request, 'blog/postdetails.html',{
            'title':post.title,
            'summary':post.summary,
            'image':post.image,
            'content':post.content,
            'date':post.date
        })
    except:
        raise Http404()