from django.db import models
# ye nokte inja hast.
# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name="comments")
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class ReplyTo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="replies")
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE, related_name="replies")
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)



    
