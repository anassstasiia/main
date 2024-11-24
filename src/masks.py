from typing import Union


def get_mask_card_number(card_number: Union[int]) -> Union[str]:
    """Принимает на вход номер карты и возвращает ее маску"""
    mask_card_number = ""
    for i, number in enumerate(str(card_number), start=1):
        if i in range(7, 13):
            mask_card_number += "*"
        else:
            mask_card_number += number
        if i in (4, 8, 12):
            mask_card_number += " "
    return mask_card_number


def get_mask_account(account: Union[int]) -> Union[str]:
    """Принимает на вход номер счета и возвращает его маску"""
    mask_account = ""
    mask_account = "**" + str(account)[-4:]
    return mask_account
