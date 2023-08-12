from distutils.command.upload import upload
from django.db import models 
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
from ckeditor.fields import RichTextField





class Post(models.Model):
    title = models.CharField(max_length=250)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    #body = models.TextField()
    body = RichTextField (blank= True, null=True)
    snippet = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering =['-date_posted']

    

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    
