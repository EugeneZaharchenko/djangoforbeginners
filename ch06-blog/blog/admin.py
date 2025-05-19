from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):  # new
    list_display = (
        "title",
        "author_info",
        "body"
    )
    list_editable = 'body',
    list_select_related = ['author']

    def author_info(self, obj):
        return f'{obj.author.username} {obj.author.last_name} {obj.author.first_name}'


admin.site.register(Post, PostAdmin)  # new
