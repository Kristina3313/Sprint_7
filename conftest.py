import pytest
from utils.api_client import APIClient
from pages.courier_page import CourierApi
from pages.order_page import OrderApi


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def courier_page(api_client):
    return CourierApi(api_client)


@pytest.fixture
def order_page(api_client):
    return OrderApi(api_client)
