def bin_search(num, array: list, key: int):
    """
    Бинарный поиск
    :param num: число, которое нужно найти
    :param array: список, в котором мы ищем
    :param key: параметр, по которому мы ищем
    :return: индекс искомого числа
    """
    mid = len(array) // 2
    if array[mid][key] == num:
        return mid
    elif array[mid][key] > num:
        mid = bin_search(num, array[:mid], key)
    elif array[mid][key] < num:
        mid += bin_search(num, array[mid:], key)
    return mid


def use_bin_search(num, array: list, key: int):
    """
    Если элемента нет в списке, ф-ция ловит RecursionError и пишет, что элемента нет в списке
    :param num: число, которое нужно найти
    :param array: список, в котором мы ищем
    :param key: параметр, по которому мы ищем
    :return: индекс искомого числа
    """
    try:
        return bin_search(num, array, key)
    except RecursionError:
        return "В этот день ученые отдыхали"


def fast_sorting(array: list, key: int) -> list:
    """
    Функция для сортировки массива
    :param array: массив
    :param key: по какому параметру сортировать
    :return: отсортированный список
    """
    min_num_i = 0  # индекс минимального элемента (локально)
    for start in range(len(array)):  # индекс элемента, который мы хотим поменять
        for i in range(start, len(array)):  # цикл для поиска минимального элемента в диапазане [start:len(array)]
            min_num_i = i if i == start else min_num_i  # минимальным становится первый элемент
            if convert_date_to_days(array[min_num_i][key]) > convert_date_to_days(array[i][key]):  # сравнение минимального и текущего
                min_num_i = i
        array[start], array[min_num_i] = array[min_num_i], array[start]  # меняем местами элемент с индексом start и min_num_i

    return array  # возврат отсортированного массива


def convert_date_to_days(date: str) -> int:
    """
    Дату формата ГГГГ-ММ-ДД превратит в количество дней
    :param date: дата
    :return: кол-во дней
    """
    time = tuple((map(int, date.split('-'))))
    return time[0] * 365 + time[1] * 31 + time[2]


file = open("scientist.txt", encoding="utf-8")  # отвкрываем файл с учеными
file = list(map(lambda s: s.split('#'), file.read().splitlines()[1:]))  # считываем его и разбиваем по "#"
file = fast_sorting(file, 2)

