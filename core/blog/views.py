from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import (
    View,
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)

# from django.http import HttpResponse
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse, reverse_lazy
from .models import Post

# from accounts.models import Profile
from blog.forms import PostForm
from comment.models import Comment
from comment.forms import CommentForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    # PermissionRequiredMixin,
)
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# def index(request):
# return render(request,'blog/index.html')

# Function Base View show a template
'''
def indexView(request):
    """
    a function based view to show index page
    """
    return render(request,'index.html', {'name':'ali21'})
'''


class IndexView(TemplateView):
    """
    a class based view to show index page
    """

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "marzya"
        context["posts"] = Post.objects.all()
        return context


"""  FBV for redirect
def redirectToMaktab(request):
    return redirect('https://maktabkhooneh.com')
"""


class RedirectToMaktab(RedirectView):

    url = "https://maktabkhooneh.com"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        print(post)
        return super().get_redirect_url(*args, **kwargs)


class PostListView(LoginRequiredMixin, ListView):  # PermissionRequiredMixin,
    # permission_required = 'blog.view_post'
    # queryset = Post.objects.all()

    model = Post
    context_object_name = "posts"
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset().filter(status=True)

        category = self.request.GET.get("category")
        author = self.request.GET.get("author")

        if category:
            queryset = queryset.filter(category__slug=category)

        if author == "me":
            queryset = queryset.filter(author=self.request.user)
        elif author:
            queryset = queryset.filter(author__id=author)

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        querydict = self.request.GET.copy()

        if "page" in querydict:
            querydict.pop("page")

        context["query_params"] = querydict.urlencode()

        return context


# خودم اینارو اضافه کردم


class CommentGet(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object  # اینو بعدا اضافه کردم
        posts = Post.objects.filter(status=True)  #
        context["form"] = CommentForm()
        context["prev_post"] = posts.filter(id__lt=post.id).order_by("-id").first()
        context["next_post"] = posts.filter(id__gt=post.id).order_by("id").first()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = "blog/post_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse("blog:post-detail", kwargs={"pk": post.pk})


# اینارو برای تست کردن نوشتم
class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    # success_url = '/blog/post/'


class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = "/blog/post/"


class PostDetailView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        view = CommentUpdate.as_view()
        return view(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        view = CommentDelete.as_view()
        return view(request, *args, **kwargs)


"""
class PostCreateView(FormView):
    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

"""


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['author','title','content','status','category','published_date']
    form_class = PostForm
    success_url = "/blog/post/"
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"
    template_name = "blog/post_form.html"

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post-list")
    template_name = "blog/post_confirm_delete.html"

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


@api_view()
def api_post_list_view(request):
    return Response({"name": "marzya"})
