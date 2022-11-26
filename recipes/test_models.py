from django.test import TestCase
from .models import Recipe

# This is a test to confirm, that the default model generates
# the right standard values for vegetarian, status and type


class TestModels(TestCase):

    def test_default_recipe(self):
        recipe = Recipe.objects.create(
            title='test',
            content='This is a test',
        )
        self.assertFalse(recipe.vegetarian)
        self.assertEqual(recipe.status, 0)
        self.assertEqual(recipe.type, 0)
