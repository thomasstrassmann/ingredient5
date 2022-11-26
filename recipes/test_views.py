from django.test import TestCase
from .models import Recipe


class TestViews(TestCase):

    def test_get_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_recipe_list(self):
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes.html')

    def test_get_cookbook_list(self):
        response = self.client.get('/cookbook/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookbook.html')

    def test_get_recipe_details(self):
        recipe = Recipe.objects.create(
            title='test', slug='test', status=1,
        )
        response = self.client.get(f'/recipes/{recipe.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')
