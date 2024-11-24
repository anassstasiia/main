def filter_by_state(my_list, my_state):
    """Функция, которая принимает список словарей и опционально значение для ключа"""
    return [i for i in my_list if i["state"] == my_state]


request = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
state = "EXECUTED"

print(filter_by_state(request, state))


def sort_by_date(my_list, my_sort=True):
    """Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки"""
    return sorted(my_list, key=lambda x: x["date"], reverse=my_sort)


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
