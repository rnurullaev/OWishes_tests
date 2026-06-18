import pytest

from clients.auth_client import AuthClient
from clients.item_client import ItemClient
from clients.reservation_client import ReservationClient
from clients.wishlist_client import WishlistClient

pytest_plugins = [
    "fixtures.auth_fixtures",
]


@pytest.fixture
def auth_client():
    return AuthClient()


@pytest.fixture
def wishlist_client():
    return WishlistClient()


@pytest.fixture
def item_client():
    return ItemClient()


@pytest.fixture
def reservation_client():
    return ReservationClient()
