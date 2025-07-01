from django.urls import path
from .import views

urlpatterns = [
    path('', views.blog_content),
    path('all-post', views.blog_allpost, name='all-post'),
    path('post-details', views.blog_postdetails, name='post-details'),
    path('contactform', views.contact_view, name='contact-form'),
    # path('contactform', views.contact_view, name='contact-form'),
    # path('contactform/thank-you', views.thankyou)
]
