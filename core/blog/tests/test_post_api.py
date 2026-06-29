from rest_framework.test import APIClient
from datetime import datetime
from django.urls import reverse
import pytest
from accounts.models import User
from blog.models import Post


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def other_user(db):
    user = User.objects.create_user(
        email="user2@user2.com", password="@#1234567", is_verified=True
    )
    return user


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email="admin@admin.com", password="@#123456", is_verified=True
    )
    return user


@pytest.fixture
def post(db, common_user):
    return Post.objects.create(
        author=common_user,
        title="Existing Post",
        status=True,
        published_date=datetime.now(),
    )


@pytest.mark.django_db
class TestPostApi:
    def test_get_post_response_401_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        response = api_client.get(url)
        assert response.status_code == 401

    def test_get_post_response_200_status(self, api_client, common_user):
        url = reverse("blog:api-v1:post-list")
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "published_date": datetime.now(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_post_response_201_status(self, api_client, common_user):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "published_date": datetime.now(),
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    #
    def test_create_post_invalid_data_response_400_status(
        self, api_client, common_user
    ):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400

    def test_update_post_response_401_status(self, api_client, post):
        url = reverse("blog:api-v1:post-detail", kwargs={"pk": post.id})
        data = {
            "title": "update-post",
            "content": "update-description",
            "status": True,
            "published_date": datetime.now(),
        }
        response = api_client.put(url, data, format="json")
        assert response.status_code == 401

    def test_update_post_response_200_status(self, api_client, common_user, post):
        url = reverse("blog:api-v1:post-detail", kwargs={"pk": post.id})
        data = {
            "title": "update-post",
            "content": "update-description",
            "status": True,
            "published_date": datetime.now(),
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.put(url, data, format="json")
        assert response.status_code == 200
        post.refresh_from_db()
        assert post.title == "update-post"
        assert post.status is True

    def test_partial_update_post_response_401_status(self, api_client, post):
        url = reverse("blog:api-v1:post-detail", kwargs={"pk": post.id})
        data = {
            "title": "partial-update-post",
        }
        response = api_client.patch(url, data, format="json")
        assert response.status_code == 401

    def test_partial_update_post_response_200_status(
        self, api_client, common_user, post
    ):
        url = reverse("blog:api-v1:post-detail", kwargs={"pk": post.id})
        data = {
            "title": "partial-update-post",
        }
        api_client.force_authenticate(user=common_user)
        response = api_client.patch(url, data, format="json")
        assert response.status_code == 200
        post.refresh_from_db()
        assert post.title == "partial-update-post"
        assert post.status == post.status

    def test_delete_post_response_401_status(self, api_client, post):
        url = reverse("blog:api-v1:post-detail", kwargs={"pk": post.id})
        response = api_client.delete(url)
        assert response.status_code == 401

    def test_delete_post_response_404_status(self, api_client, other_user, post):
        url = reverse("blog:api-v1:post-detail", kwargs={"pk": post.id})
        api_client.force_authenticate(user=other_user)
        response = api_client.delete(url)
        assert response.status_code in [403, 404]
        assert Post.objects.filter(id=post.id).exists() is True

    def test_delete_post_response_204_status(self, api_client, common_user, post):
        url = reverse("blog:api-v1:post-detail", kwargs={"pk": post.id})
        api_client.force_authenticate(user=common_user)
        response = api_client.delete(url)
        assert response.status_code == 204
        assert Post.objects.filter(id=post.id).exists() is False
