def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция фильтрации списка словарей по ключу state"""
    filtered_list = []
    for item in list_dict:
        if item.get("state") == state:
            filtered_list.append(item)
    return filtered_list


def sort_by_date(list_dict: list, type_sort: bool = True) -> list:
    """Функция сортировки списка словарей по дате"""
    return sorted(list_dict, key=lambda x: x["date"], reverse=type_sort)
