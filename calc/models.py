from django.db import models

# Create your models here.
# In your app's models.py (e.g., calc/models.py)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images/')
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    discord_url = models.URLField(blank=True)
    stack_overflow_url = models.URLField(blank=True)
    # Add more fields as needed

    def __str__(self):
        return self.full_name
    
# models.py
from django.db import models

class About(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images/')
    birthday = models.DateField()
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=100, blank=True)
    age = models.IntegerField()
    degree = models.CharField(max_length=100)
    email = models.EmailField()
    freelance = models.BooleanField(default=False)
    bio = models.TextField()

    def __str__(self):
        return self.title
    

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()
    icon_image = models.ImageField(upload_to='skill_icons/', blank=True, null=True)

    def __str__(self):
        return self.name


