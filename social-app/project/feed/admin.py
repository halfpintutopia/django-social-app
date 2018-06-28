from django.contrib import admin
# from project.api.models import Author
from project.feed.models import Post

# class AuthorAdmin(admin.ModelAdmin):
#     pass


# admin.site.register(Author, AuthorAdmin)

admin.site.register(Post)
