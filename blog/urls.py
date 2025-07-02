from django.urls import path
from .import views

urlpatterns = [
    path('', views.blog_content.as_view()),
    path('all-post', views.blog_allpost.as_view(), name='all-post'),
    path('post-details', views.blog_postdetails.as_view(), name='post-details'),
    path('contactform', views.contact_view.as_view(), name='contact-form'),
    path('thank-you', views.thankyou.as_view())
]
