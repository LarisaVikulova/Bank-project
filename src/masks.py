card_number_str = int()
account_str = int()


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску: 7000 79** **** 6361"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску: **4305"""
    return f"**{account[-4:]}"
