import pytest
from django.urls import reverse
from django.test import Client, TestCase
from lettings.models import Address, Letting


@pytest.mark.django_db(True)
class LettingsPagesTitleTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.address = Address.objects.create(
            number=1, street="street",
            city="city", state="ST",
            zip_code=12345, country_iso_code="FR"
        )
        self.letting = Letting.objects.create(
            title="Test Title",
            address=self.address
        )
        self.lettings_index_url = reverse('lettings:index')
        self.lettings_letting_url = reverse(
            'lettings:letting',
            kwargs={'letting_id': self.letting.id}
        )
        self.index_title = "<title>Lettings</title>"
        self.letting_title = f"<title>{self.letting.title}</title>"

    def test_page_lettings_index_should_contains_proper_title(self):
        response = self.client.get(self.lettings_index_url)
        assert self.index_title in response.content.decode()

    def test_page_letting_should_contains_proper_title(self):
        response = self.client.get(self.lettings_letting_url)
        assert self.letting_title in response.content.decode()


@pytest.mark.django_db(True)
class LettingsRoutesTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.address = Address.objects.create(
            number=1, street="street",
            city="city", state="ST",
            zip_code=12345, country_iso_code="FR"
        )
        self.letting = Letting.objects.create(
            title="Test Title",
            address=self.address
        )
        self.lettings_index_url = reverse('lettings:index')
        self.lettings_letting_url = reverse(
            'lettings:letting', kwargs={'letting_id': self.letting.id}
        )

    def test_get_lettings_index_should_status_code_ok(self):
        response = self.client.get(self.lettings_index_url)
        assert response.status_code == 200

    def test_get_lettings_index_without_slash_should_status_code_redirect(self):
        response = self.client.get('/lettings')
        assert response.status_code == 301

    def test_get_letting_DavWin_should_status_code_redirect(self):
        response = self.client.get(self.lettings_letting_url)
        assert response.status_code == 200
