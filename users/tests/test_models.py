import pytest

from users.models import Users

pytestmark = pytest.mark.django_db


def test_create_user():
    user = Users.objects.create_user(
        first_name="usuario_test", email="usuario@test.com", password="passw0rd"
    )

    assert user.first_name == "usuario_test"
    assert user.email == "usuario@test.com"
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser


def test_create_superuser():
    user = Users.objects.create_superuser(
        first_name="admin_test", email="admin@test.com", password="passw0rd"
    )
    assert user.first_name == "admin_test"
    assert user.email == "admin@test.com"
    assert user.is_active
    assert user.is_staff
    assert user.is_superuser