from django.db import models
from django.utils.text import slugify

class Contact(models.Model):
    user_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    message = models.CharField(max_length=250)
    
    def __str__(self):
        return f'{self.user_name} and {self.email} and {self.message}'


    
class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='images')
    summary = models.TextField()
    content = models.TextField()
    date = models.DateField(null=True, blank=True)
    # slug = models.SlugField(default='', null=False, db_index=True, editable=False)
    
    # def save(self, *args, **kwargs):
    #    self.slug = slugify(self.title)
    #    super().save(*args, **kwargs) # Call the real save() method
    
    
    def __str__(self):
        return f'{self.title}'
    