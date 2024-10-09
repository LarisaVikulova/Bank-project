from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(number_card: str) -> str:
    """Функция для маскировки счета/карты"""
    if "Счет" in number_card:
        return f"Счет {get_mask_account(number_card)}"
    else:
        card = get_mask_card_number(number_card[-16:])
        new_card = number_card.replace(number_card[-16:], card)
    return new_card


def get_date(date: str) -> str:
    """Функция, принимающая строку с датой и переводящая ее в формат ДД.ММ.ГГГГ"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
