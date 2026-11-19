from string_utils import StringUtils
import pytest


@pytest.mark.parametrize(
        'text1, expected_res',
        [("Осень", "Осень"),
         ("осень", "Осень"),
         ("", ""),
         ("123", "123")]
        )
def test_utils_text(text1, expected_res):
    utils = StringUtils()
    res = utils.capitalize(text1)
    assert res == expected_res


@pytest.mark.parametrize(
        'text1, expected_res',
        [("  самолёт", "самолёт"),
         ("вагон", "вагон"),
         ("    ", "")]
        )
def test_utils_space(text1, expected_res):
    utils = StringUtils()
    res = utils.trim(text1)
    assert res == expected_res


@pytest.mark.parametrize(
        'text1, symbol, expected_res',
        [("152,2", ",", True),
         ("Заморозки", "о", True),
         ("Исследователь", "б", False),
         ("Ледянной монстр", " ", True),
         ("Футуризм", "а", False)]
        )
def test_utils_symbol(text1, symbol, expected_res):
    utils = StringUtils()
    res = utils.contains(text1, symbol)
    assert res == expected_res


@pytest.mark.parametrize(
        'text1, symbol, expected_res',
        [("Изморось", "с", "Измороь"),
         ("В лесу родилась", " ", "Влесуродилась"),
         ("Аутентификация", "и", "Аутентфкаця"),
         ("Солнце", "o", "Солнце")]
        )
def test_utils_delete(text1, symbol, expected_res):
    utils = StringUtils()
    res = utils.delete_symbol(text1, symbol)
    assert res == expected_res
