from django.contrib import admin

# Register your models here.
from .models import Author, Post, Tag, Comment

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('fullName',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('caption',)

class PostAdmin(admin.ModelAdmin):
    list_filter = ('author','date','tags',)
    list_display = ('title','date','author',)
    prepopulated_fields = {'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','comment',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)