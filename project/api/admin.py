from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'author')
    list_display = ('title','author')
    search_fields = ('title',)


admin.site.register(Post, PostAdmin)
