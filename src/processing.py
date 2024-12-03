def filter_by_state(line: list, parameter: str = "EXECUTED") -> list:
    """Функция, которая принимает список словарей и опционально значение для ключа"""
    return [i for i in line if i["state"] == parameter]


def sort_by_date(id_card: list, by_date: bool = True) -> list:
    """Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки"""
    return sorted(id_card, key=lambda x: x["date"], reverse=by_date)
