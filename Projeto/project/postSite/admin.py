from django.contrib import admin
from postSite.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'content')

admin.site.register(Post, PostAdmin)