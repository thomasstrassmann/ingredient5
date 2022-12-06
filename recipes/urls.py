from . import views
from django.urls import path


urlpatterns = [
    path('', views.get_index, name='home'),
    path('recipes/', views.RecipeList.as_view(), name='recipes_list'),
    path('recipes/<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('bookmark/<int:id>', views.RecipeBookmark.as_view(), name="recipe_bookmark"),
    path('cookbook/', views.get_cookbook, name='cookbook_list'),
    path('cookbook/<int:id>', views.BookmarkRemove.as_view(), name='remove_bookmark'),
]