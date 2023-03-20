from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Famil(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/img/families/image', null=True, blank=True)
    about_fam = models.TextField(default='')
    whatsapp_url = models.URLField(null=True, blank=True)
    

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/img/charity_events/image', null=True, blank=True)

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/img/team/image', null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='static/img/post_images/', blank=True)
    slug = models.SlugField()
    def __str__(self):
        return self.title
    def get_content_as_html(self):
        return self.content.replace('\n', '<br>')

    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    description = models.TextField()
    profile = models.ImageField(upload_to='static/img/testimonial/profile')
    

    def __str__(self):
        return self.name

class Portfolio_Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    categories = models.ManyToManyField(Portfolio_Category)
    description = models.TextField()
    image = models.ImageField(upload_to='static/img/portfolio/images/')
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



