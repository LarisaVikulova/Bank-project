from datetime import datetime


from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(number: str) -> str:
    """Функция для маскировки счета/карты"""
    if len(number.split()[-1]) == 16:
        new_number = get_mask_card_number(number.split()[-1])
        result = f"{number[:16]}{new_number}"
    elif len(number.split()[-1]) == 20:
        new_number = get_mask_account(number.split()[-1])
        result = f"{number[:20]}{new_number}"
    return result


def get_date(date: str) -> str:
    """Функция, принимающая строку с датой и переводящая ее в формат ДД.ММ.ГГГГ"""
    return f"{date[8:18]}.{date[5:7]}.{date[8:4]}"


