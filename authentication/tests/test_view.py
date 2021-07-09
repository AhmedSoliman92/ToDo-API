from authentication import views
from rest_framework.test import APITestCase, force_authenticate
from rest_framework.test import APIRequestFactory
from authentication.models import User


class ViewsTest(APITestCase):

    def test_Register_APIVIEW_register(self):
        user1 = {
            "username": "ahmed",
            "email": "ahmed@gmail.com",
            "password": "password@#$A",
        }
        respons = self.client.post('/api/auth/register', user1)
        self.assertEqual(respons.status_code, 201)

    def test_raise_error_BAD_REQUEST_Register_APIVIEW_register(self):
        user1 = {
            "username": "ahmed",
            "email": "ahmed@gmail.com",
            "password": "password@#$A",
        }
        User.objects.create_user(
            username="ahmed", email="ahmed@gmail.com", password="password@#$A")
        respons = self.client.post('/api/auth/register', user1)
        self.assertEqual(respons.status_code, 400)

    def test_LoginAPIVIEW_login(self):
        user1 = {
            "username": "ahmed",
            "email": "ahmed@gmail.com",
            "password": "password@#$A"
        }
        User.objects.create_user(
            username="ahmed", email="ahmed@gmail.com", password="password@#$A")
        respons = self.client.post('/api/auth/login', user1)
        self.assertEqual(respons.status_code, 200)

    def test_raise_error_unauthorized_user(self):
        user1 = {
            "username": "ahmed",
            "email": "ahmed1@gmail.com",
            "password": "password@#$A"
        }

        User.objects.create_user(
            username="ahmed", email="ahmed@gmail.com", password="password@#$A")
        respons = self.client.post('/api/auth/login', user1)
        self.assertEqual(respons.status_code, 401)

    def test_get_user(self):
        factroy = APIRequestFactory()
        user = User.objects.create_user(
            username="ahmed", email="ahmed@gmail.com", password="password@#$A")
        view = views.AuthAPIView.as_view()
        request = factroy.get('/api/auth/')
        force_authenticate(request, user=user)
        responss = view(request)
