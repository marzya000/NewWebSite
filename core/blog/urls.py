from django.urls import path, include
from . import views

# from django.views.generic import TemplateView
# from django.views.generic.base import RedirectView


app_name = "blog"

urlpatterns = [
    #  ezafi path('cbv-index', views.IndexView.as_view(), name='cbv-index'),
    #  ezafi path('go-to-maktabkhooneh/<int:pk>', views.RedirectToMaktab.as_view(),name="redirect-to-maktabkhooneh"),
    # ezafi path('home/',views.index, name='home'),
    path("", views.IndexView.as_view(), name="index"),
    path("post/", views.PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post/create/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/edit/", views.PostEditView.as_view(), name="post-edit"),
    path(
        "post/<int:pk>/delete/",
        views.PostDeleteView.as_view(),
        name="post-delete",
    ),
    path("api/v1/", include("blog.api.v1.urls")),
    # ezafi path('post/',views.api_post_list_view, name='api-post-list'),
]
