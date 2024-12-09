transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07"
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93"
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34"
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54"
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70"
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


def filter_by_currency(transactions, currency):
    for x in transactions:
        value1 = x.get("operationAmount", {})
        value2 = value1.get("currency", {})
        value3 = value2.get("code", {})
        if value3 == currency:
            yield x


# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(2):
#     print(next(usd_transactions))


def transaction_descriptions(transactions):
    for y in transactions:
        yield y.get("description")




# descriptions = transaction_descriptions(transactions)
# for _ in range(5):
#     print(next(descriptions))


def card_number_generator(start, finish):
    if finish > 10000000000000000:
        raise ValueError("Incorrect diapason")
    elif start < 0 or finish < 0:
        raise ValueError("Incorrect diapason")
    elif start >= finish:
        raise ValueError("Incorrect diapason")
    else:
        for x in range(start, finish):
            need_zero = 16 - len(str(x))
            result = "0" * need_zero + str(x)
            result_space = f'{str(result)[:4]} {str(result)[4:8]} {str(result)[-8:-4]} {str(result)[-4:]}'
            yield result_space


if __name__ == '__main__':
    print(list(card_number_generator(-5, -1)))