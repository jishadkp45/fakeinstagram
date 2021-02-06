from django.db import models
from accounts.models import UserAccounts
from django.db.models.signals import post_delete

from django.contrib.auth import get_user_model
from django.dispatch import receiver

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    caption = models.TextField()
    image = models.ImageField(upload_to="posts")
    # create_at = models.DateTimeField(auto_now_add=True)
    # modified_at = models.DateTimeField(auto_now=True)


@receiver(post_delete, sender=Post)
def delete_post_image(sender, instance, *args, **kwargs):
    instance.image.delete(False)


class Like(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="user_likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_likes")

    class Meta:
        unique_together = ["user", "post"]


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="user_comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")
    comment = models.TextField(default='no comment')
    # create_at = models.DateTimeField(auto_now_add=True)
    # modified_at = models.DateTimeField(auto_now=True)


class HashTag(models.Model):
    tag = models.CharField(max_length=40)
    post = models.ManyToManyField(Post)