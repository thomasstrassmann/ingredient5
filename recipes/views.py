from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe, Comment


def get_index(request):
    return render(request, 'index.html')


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created')
    template_name = 'recipes.html'
    paginate_by = 5


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created')
        bookmarked = False
        if recipe.bookmarks.filter(id=self.request.user.id).exists():
            bookmarked = True
        
        return render(
            request, "recipe_detail.html", {
                "recipe": recipe,
                "comments": comments,
                "bookmarked": bookmarked,
            }
        )
