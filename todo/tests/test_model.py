from rest_framework.test import APITestCase
from todo.models import Todo
from authentication.models import User
class ModelsTest(APITestCase):
    def test_create_todo(self):
        user = User.objects.create_user(
            username="ahmed", email="ahmed@gmail.com", password="password@#$A")
        todo=Todo.objects.create(title="title",description="desc",is_completed=True,owner=user)
        self.assertEqual(str(todo),"title")

        