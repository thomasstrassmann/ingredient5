from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

PUBLISHED_STATUS = ((0, "Draft"), (1, "Published"))
CUISINE = ((0, "Unassignable"), (1, "European"), (2, "Asian"), (3, "Arabic"), (4, "African"), (5, "North-/Southamerican"))


class Recipe(models.Model):
    title = models.CharField(max_length=180, unique=True)
    slug = models.SlugField()
    recipe_image = CloudinaryField('image', default='placeholder')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    type = models.IntegerField(choices=CUISINE, null=False, blank=False, default=0)
    content = models.TextField()
    ingredients = models.TextField(blank=True)
    vegetarian = models.BooleanField(default=False)
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
    message = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"Comment by {self.username}: {self.message}"
