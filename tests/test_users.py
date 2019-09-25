from oop.oop_classes import User


def test_user_is_not_logged_in_at_start():
    u = User('someemail@example.com')
    assert u.is_logged is False


def test_user_cannot_change_password_with_wrong_key():
    u = User('someemail@example.com')
    u.set_password('wrong_key', 'new_password')
    u.login('new_password')
    assert u.is_logged is False
