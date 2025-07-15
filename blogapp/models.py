from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings  

# Create your models here.

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(TimeStampModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(TimeStampModel):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('in_active','Inactive'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    featured_image = models.ImageField(upload_to='post_images/%Y/%m/%d', blank=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ✅ FIXED
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    published_at = models.DateTimeField(null=True, blank=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(TimeStampModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_images/%Y/%m/%d', blank=False)
    comment = models.TextField()

    def __str__(self):
        return f"{self.comment[:7]}"


class Contact(TimeStampModel):
    message = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Newletter(TimeStampModel):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
