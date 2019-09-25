from oop.oop_classes import User


def test_user_is_not_logged_in_at_start():
    u = User('someemail@example.com')
    assert u.is_logged is False


def test_user_cannot_change_password_with_wrong_key():
    u = User('someemail@example.com')
    u.set_password('wrong_key', 'new_password')
    u.login('new_password')
    assert u.is_logged is False

"""
Test cases:
1. Stworzenie produktu, pobranie ceny i nazwy
2. Stworzenie koszyka -> powinien być pusty
3. Dodanie pojedynczego produktu do koszyka i pobranie ceny, count
4. Dodanie wielu produktów i policzenie ceny, count
5. Dodanie 10 produktów na raz, pobranie ceny i count
6. Dodanie 11 produktów -> błąd
7. Dodanie 10 i dodanie kolejnego -> błąd
8. Dodanie 9 i dodanie 2 -> błąd
9. Czyszczenie koszyka -> nowa metoda, TDD
10. Zniżka -> poprawna, policzenie ceny
11. Zniżka niepoprawna -> błąd
"""