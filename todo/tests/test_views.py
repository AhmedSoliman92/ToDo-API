from django.http import response
from rest_framework.test import APITestCase
from django.urls import reverse
from todo.models import Todo
from rest_framework import status


class ViewsAPIsTest(APITestCase):
    def authenticate(self):
        user = {
            "username": "ahmed",
            "email": "ahmed@gmail.com",
            "password": "password@#$A",
        }
        self.client.post(reverse('register'), user)
        response = self.client.post(reverse('login'), user)
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION=f"Beare {token}")

    def create_todo(self):
        my_todo = {
            "title": "title",
            "description": "desc",
            "is_completed": True
        }
        return self.client.post(reverse('todos'), my_todo)


class TodoAPIViewTest(ViewsAPIsTest):
    def test_create_todo(self):
        self.authenticate()
        response = self.create_todo()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_all_todos(self):
        self.authenticate()
        self.create_todo()
        self.create_todo()
        response = self.client.get(reverse('todos'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['count'], int)
        self.assertEqual(response.data['count'], 2)
        print(self)


class TodoDetailAPIView(ViewsAPIsTest):
    def test_retrieve_all_todos(self):
        self.authenticate()
        res = self.create_todo()
        response = self.client.get(
            reverse("todo", kwargs={'id': res.data['id']}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_todos(self):
        self.authenticate()
        res = self.create_todo()
        response = self.client.delete(
            reverse("todo", kwargs={'id': res.data['id']}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_todos(self):
        self.authenticate()
        res = self.create_todo()
        response = self.client.patch(
            reverse("todo", kwargs={'id': res.data['id']}), {
                "title": "New one", 'is_complete': True
            })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
