from django.contrib import admin

from posts.models import Post, Hashtag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'rate', 'created_data', 'created_date', "image",)
    sortable_by = ('rate', 'created_data',)
    list_display_links = ('id', 'title',)
    list_filter = ('rate', 'created_data',)


# admin.site.register(Post)
admin.site.register(Hashtag)
