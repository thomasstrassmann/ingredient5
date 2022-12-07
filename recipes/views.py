from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import Recipe, Comment
from .forms import CommentForm


def get_index(request):
    return render(request, 'index.html')


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created')
    template_name = 'recipes.html'
    paginate_by = 12

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '0')
        if filter_val == '0':
            queryset = Recipe.objects.filter(status=1).order_by('-created')
            return queryset
        else:
            new_context = Recipe.objects.filter(type=filter_val)
            return new_context


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('-created')
        vegetarian = recipe.vegetarian
        type = recipe.type
        bookmarked = False
        if recipe.bookmarks.filter(id=self.request.user.id).exists():
            bookmarked = True

        return render(
            request, "recipe_detail.html", {
                "recipe": recipe,
                "type": type,
                "comments": comments,
                "comment_form": CommentForm(),
                "commented": False,
                "vegetarian": vegetarian,
                "bookmarked": bookmarked,
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created')
        vegetarian = recipe.vegetarian
        type = recipe.type
        bookmarked = False
        if recipe.bookmarks.filter(id=self.request.user.id).exists():
            bookmarked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.username = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request, "recipe_detail.html", {
                "recipe": recipe,
                "type": type,
                "comments": comments,
                "commented": True,
                "comment_form": CommentForm(),
                "vegetarian": vegetarian,
                "bookmarked": bookmarked,
            }
        )


class CookbookList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(bookmarks=True).order_by('-created')
    template_name = 'cookbook.html'
    paginate_by = 12


def get_cookbook(request):
    bookmarked_recipe = Recipe.objects.filter(bookmarks=request.user)
    return render(request, 'cookbook.html', {
        "bookmarked_recipe": bookmarked_recipe})


class RecipeBookmark(View):

    def post(self, request, id, *args, **kwargs):
        recipe = get_object_or_404(Recipe, id=id)
        if recipe.bookmarks.filter(id=request.user.id).exists():
            recipe.bookmarks.remove(request.user)
        else:
            recipe.bookmarks.add(request.user)

        return HttpResponseRedirect(request.META['HTTP_REFERER'])


class BookmarkRemove(View):

    def post(self, request, id, *args, **kwargs):
        recipe = get_object_or_404(Recipe, id=id)
        recipe.bookmarks.remove(request.user)

        return HttpResponseRedirect(reverse('cookbook_list'))
