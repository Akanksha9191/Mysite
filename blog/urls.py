from django.urls import path
from .import views

urlpatterns = [
    path('', views.blog_content.as_view()),
    path('allpost', views.all_post.as_view(), name='all-post'),
    path('<int:id>', views.blog_postdetails, name='post-details'),
    path('contactform', views.contact_view.as_view(), name='contact-form'),
    path('thankyou', views.thankyou.as_view()),
    path('uploadform', views.post_upload_form.as_view(), name='upload-form'),
    
]
