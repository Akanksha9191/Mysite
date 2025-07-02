from django.db import models

# Create your models here.
# class Contact(models.Model):
#     user_name = models.CharField(max_length=20)
#     email = models.CharField(max_length=30)
#     message = models.CharField(max_length=500)
    
#     def __str__(self):
#         return f'{self.user_name} and {self.emial} and {self.message}'

# # class Post(models.Model):
# #     pass

class Contact(models.Model):
    user_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    message = models.CharField(max_length=250)