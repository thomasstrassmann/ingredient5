from django.test import TestCase 
from .forms import CommentForm


class TestCommentForm(TestCase):

    def test_message_is_required(self):
        form = CommentForm({'message': ''})
        self.assertFalse(form.is_valid())

