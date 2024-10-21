from src.masks import get_mask_card_number, get_mask_account
import pytest


@pytest.mark.parametrize(
    "number, masks",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("4571354875129009", "4571 35** **** 9009"),
        ("2504706942057145", "2504 70** **** 7145"),
    ],
)
def test_get_mask_card_number(number, masks) -> str:
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("7000792289606361456783456") == "Неверно введенный номер карты"


def test_get_mask_account() -> str:
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("73654108430135874305123456") == "**3456"
