from django.db import models
from django.contrib.auth.models import User

PUBLISHED_STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    title = models.CharField(max_length=180, unique=True)
    slug = models.SlugField(max_length=180, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=PUBLISHED_STATUS, default=0)
    bookmarks = models.ManyToManyField(User, related_name="recipe_bookmarks", blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def num_of_bookmarks(self):
        return self.bookmarks.count()

class Comment(models.Model):

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    username = models.CharField(max_length=50)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"Comment by {self.username}: {self.message}"