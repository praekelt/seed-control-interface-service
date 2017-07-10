from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


class APITestCase(TestCase):

    def setUp(self):
        self.adminclient = APIClient()


class AuthenticatedAPITestCase(APITestCase):

    def setUp(self):
        super(AuthenticatedAPITestCase, self).setUp()

        # Admin User setup
        self.adminusername = 'testadminuser'
        self.adminpassword = 'testadminpass'
        self.adminuser = User.objects.create_superuser(
            self.adminusername,
            'testadminuser@example.com',
            self.adminpassword)
        admintoken = Token.objects.create(user=self.adminuser)
        self.admintoken = admintoken.key
        self.adminclient.credentials(
            HTTP_AUTHORIZATION='Token ' + self.admintoken)


class TestServicesApp(AuthenticatedAPITestCase):

    def test_list_dashboard(self):

        response = self.adminclient.get('/api/v1/dashboard/')

        body = response.json()
        self.assertEqual(len(body['results']), 0)

    def test_list_userdashboard(self):

        response = self.adminclient.get('/api/v1/userdashboard/')

        body = response.json()
        self.assertEqual(len(body['results']), 0)

    def test_list_definition(self):

        response = self.adminclient.get('/api/v1/definition/')

        body = response.json()
        self.assertEqual(len(body['results']), 0)
