from celery import shared_task
from .models import Post


@shared_task
def clean_posts_with_status_true():
    Post.objects.filter(status=True).delete()
    print("Posts with status=True are deleted")
