def filter_by_currency(transactions, currency):
    """Принимает на вход список словарей, представляющих транзакции"""
    for x in transactions:
        value1 = x.get("operationAmount", {})
        value2 = value1.get("currency", {})
        value3 = value2.get("code", {})
        if value3 == currency:
            yield x


def transaction_descriptions(transactions):
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for y in transactions:
        yield y.get("description")


def card_number_generator(start, finish):
    """Выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX
    , где
    X
     — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
     от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    """
    if finish > 10000000000000000:
        raise Exception("Incorrect finish")
    elif start < 0 or finish < 0:
        raise Exception("Incorrect diapason")
    elif start >= finish:
        raise Exception("Incorrect diapason")
    else:
        for x in range(start, finish):
            need_zero = 16 - len(str(x))
            result = "0" * need_zero + str(x)
            result_space = f"{str(result)[:4]} {str(result)[4:8]} {str(result)[-8:-4]} {str(result)[-4:]}"
            yield result_space
