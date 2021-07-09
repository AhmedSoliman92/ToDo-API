from rest_framework.test import APITestCase
from authentication.models import User



class TestModel(APITestCase):

    def test_create_user(self):
        user = User.objects.create_user(
            username="ahmed", email="ahmed@gmail.com", password="password@#$A")
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'ahmed@gmail.com')

    def test_if_not_username_raise_error(self):
        self.assertRaises(ValueError, User.objects.create_user,
                          username="", email="ahmed@gmail.com", password="password@#$A")

    def test_if_not_email_raise_error(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(
                username="ahmed", email="", password="password@#$A")

    def test_create_supperuser_is_staff_and_superuser(self):
        user = User.objects.create_superuser(
            username="ahmed", email="ahmed@gmail.com", password="password@#$A")

        self.assertTrue(user.is_staff, True)
        self.assertTrue(user.is_superuser, True)

    def test_create_superuser_raise_error_if_not_staff(self):
        self.assertRaises(ValueError, User.objects.create_superuser, username="ahmed",
                          email="ahmed@gmail.com", password="password@#$A", is_staff=False)

    def test_create_superuser_raise_error_if_not_superuser(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            user = User.objects.create_superuser(
                username="ahmed", email="ahmed@gmail.com", password="password@#$A", is_superuser=False)

    