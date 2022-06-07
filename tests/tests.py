# import pytest
from django.urls import reverse
from django.test import Client


client = Client()
index_url = reverse('index')
incorrect_url = '/incorrect/'


def test_get_index_should_status_code_ok(client):
    response = client.get(index_url)
    assert response.status_code == 200


def test_get_index_should_status_code_404(client):
    response = client.get(incorrect_url)
    assert response.status_code == 404
