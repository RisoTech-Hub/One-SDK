import pytest
from django.contrib.auth import get_user_model

from .factories import UserFactory


@pytest.fixture
def user(db) -> get_user_model():
    return UserFactory()
