from django.contrib import admin
from comment.models import Comment

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ("author", "post", "approved", "created_date")
    list_filter = ("post", "approved")
    search_fields = ["author", "post"]


admin.site.register(Comment, CommentAdmin)
