def get_mask_card_number(card_number: int) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""
    if len(str(card_number)) == 16 and card_number > 0:
        return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"
    else:
        raise ValueError("Card 16")


def get_mask_account(account: int) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    if len(str(int(account))) == 20:
        mask_account = "**" + str(account)[-4:]
        return mask_account
    else:
        raise ValueError("account 20")
