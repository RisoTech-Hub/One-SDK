from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings

from ..utils import get_field_diff, make_diffs, field_verbose_name

User = get_user_model()


class TestLedgerUtils(TestCase):
    def test_get_field_diff(self):
        old_str = "Noi dung truoc khi thay doi"
        new_str = "Noi dung sau khi thay doi"
        expected_diffs = '<span>Noi dung </span><del style="background:#ffe6e6;">truoc</del><ins style="background:#e6ffe6;">sau</ins><span> khi thay doi</span>'  # noqa
        diffs = get_field_diff(old_str, new_str)
        assert diffs == expected_diffs

    def test_make_diff(self):
        old_json = {
            "name": "Noi dung truoc khi thay doi",
            "age": 10,
            "address": "Ha Noi",
            "hobbies": ["football", "basketball"],
            "student": True,
            "friends": ["John", "Peter"],
            "not_changed": "Noi dung khong thay doi",
            "removed_field": "Noi dung bi xoa"
        }
        new_json = {
            "name": "Noi dung sau khi thay doi",
            "age": 20,
            "address": "Ho Chi Minh",
            "hobbies": ["football", "basketball", "tennis"],
            "student": False,
            "friends": ["Mary"],
            "not_changed": "Noi dung khong thay doi",
            "new_field": "Noi dung moi"
        }
        diffs = make_diffs(old_json, new_json)
        changed_keys = [diff["key"] for diff in diffs]
        assert "name" in changed_keys
        assert "not_changed" not in changed_keys

    def test_field_verbose_name(self):
        assert "username" in field_verbose_name(User)
