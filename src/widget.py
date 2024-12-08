from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_number: str) -> str:
    account_name = ""
    name_account_name = ["Visa Platinum ", "Maestro ", "MasterCard ", "Visa Classic ", "Visa Gold ", "Счет "]
    for i in account_number:
        if i.isalpha() or i == " ":
            account_name += i

    if account_name in name_account_name[-1]:
        number = int(account_number[5:])
        card = account_name + get_mask_account(number)
    elif account_name in name_account_name:
        number = int(account_number[-16:])
        card = account_name + get_mask_card_number(number)
    else:
        raise ValueError("Incorrect input name card")
    return card


def get_date(data: str) -> str:
    if len(data) == 26:
        data1 = data[:4]
        data2 = data[5:7]
        data3 = data[8:10]
        if int(data1) and int(data2) and int(data3) in range(1, 3000):
            return f"{data3}.{data2}.{data1}"
        else:
            raise ValueError("Incorrect data")
    else:
        raise ValueError("Incorrect 26 symbols")
