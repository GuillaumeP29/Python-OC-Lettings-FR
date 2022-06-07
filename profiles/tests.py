import pytest
from django.urls import reverse
from django.test import Client, TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db(True)
class LettingsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.profiles_index_url = reverse('profiles:index')
        self.user = User.objects.create(
            username="username_test",
            first_name="user",
            last_name="name",
            email="user.name@mail.com",
            password="username1234!"
        )
        self.profile = Profile.objects.create(
            user=User.objects.get(username="username_test"),
            favorite_city="Test City"
        )
        self.profiles_profile_url = reverse(
            'profiles:profile',
            kwargs={'username': self.user.username}
        )
        self.index_title = "<title>Profiles</title>"
        self.letting_title = f"<title>{self.profile.user.username}</title>"

    def test_page_profiles_index_should_contains_proper_title(self):
        response = self.client.get(self.profiles_index_url)
        assert self.index_title in response.content.decode()

    def test_page_profile_should_contains_proper_title(self):
        response = self.client.get(self.profiles_profile_url)
        assert self.letting_title in response.content.decode()

    def test_get_pofiles_index_should_status_code_ok(self):
        response = self.client.get(self.profiles_index_url)
        assert response.status_code == 200

    def test_get_pofiles_index_without_slash_should_status_code_redirect(self):
        response = self.client.get('/profiles')
        assert response.status_code == 301

    def test_get_pofile_DavWin_should_status_code_redirect(self):
        response = self.client.get(self.profiles_profile_url)
        assert response.status_code == 200
