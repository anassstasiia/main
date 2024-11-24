from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_number: str) -> str:
    account_name = ""
    for i in account_number:
        if i.isalpha() or i == " ":
            account_name += i

    if "Счет" in account_number:
        number = int(account_number[5:])
        card = account_name + get_mask_account(number)
    else:
        number = int(account_number[-16:])
        card = account_name + get_mask_card_number(number)
    return card


def get_date(data: str) -> str:
    data1 = data[:4]
    data2 = data[5:7]
    data3 = data[8:10]
    return f"{data3}.{data2}.{data1}"
