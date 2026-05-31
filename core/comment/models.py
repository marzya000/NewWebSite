from django.db import models
from accounts.models import Profile
from blog.models import Post
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.
User = get_user_model()

class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name="comments")
    subject = models.CharField(max_length=255)
    message = models.TextField(null=False,blank=False)
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.created_date
    

    def get_snippet(self):
        return self.message[0:5]
    
    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post-detail", kwargs={"pk": self.pk})


# class ReplyTo(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="replies")
#     comment = models.ForeignKey(Comment,on_delete=models.CASCADE, related_name="replies")
#     message = models.TextField(null=False,blank=False)
#     approved = models.BooleanField(default=False)
#     created_date = models.DateTimeField(default=timezone.now)
#     



    
