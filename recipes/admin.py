from django.contrib import admin
from .models import Recipe, Comment


class RecipeAdmin(admin.ModelAdmin):
    list_filter = ('created', 'status')
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'created', 'status')
    search_fields = ('title', 'content')


class CommentAdmin(admin.ModelAdmin):
    search_fields = ('username', 'message')
    list_filter = ('created', 'approved')
    list_display = ('username', 'recipe', 'message', 'created', 'approved')
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment, CommentAdmin)
