def simple_separator():
    """
    Функция создает красивый резделитель из 10-и звездочек (**********)
    return: **********
    """
    return print('**********')


simple_separator()


def long_separator(count):
    """
    Функция создает разделитель из звездочек число которых можно регулировать параметром count
    :param count: количество звездочек
    :return: строка разделитель, примеры использования ниже
    """
    return print(count * '*')


long_separator(3)
long_separator(4)


def separator(simbol, count):
    """
    Функция создает разделитель из любых символов любого количества
    :param simbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """
    return print(simbol * count)


separator('-', 10)
separator('#', 5)


def hello_world():
    """
    Функция печатает Hello World в формате:
    **********

    Hello World!

    ##########
    :return: None
    """
    simple_separator()
    print()
    print('Hello World!', '\n')
    separator('#', 10)
    pass


hello_world()


def hello_who(who='World'):
    """
    Функция печатает приветствие в красивом формате
    **********

    Hello {who}!

    ##########
    :param who: кого мы приветствуем, по умолчанию World
    :return: None
    """
    simple_separator()
    print()
    print('Hello', who, '!', '\n')
    separator('#', 10)
    pass


hello_who()
hello_who('Max')


def pow_many(power, *args):
    """
    Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
    :param power: степень
    :param args: любое количество цифр
    :return: результат вычисления # True -> (1 + 2)**1
    """
    result = sum(args) ** power

    return result


print(pow_many(2, 1, 2, 3, 4))


def print_key_val(**kwargs):
    """
    Функция выводит переданные параметры в виде key --> value
    key - имя параметра
    value - значение параметра
    :param kwargs: любое количество именованных параметров
    :return: None
    """
    for key, value in kwargs.items():
        print("{} --> {}".format(key, value))

    pass


print_key_val(name='Max', age=21)
print_key_val(animal='Cat', is_animal=True)

from functools import reduce


def my_filter(iterable, function):
    """
    (Усложненое задание со *)
    Функция фильтрует последовательность iterable и возвращает новую
    Если function от элемента последовательности возвращает True, то элемент входит в новую последовательность иначе нет
    (примеры ниже)
    :param iterable: входная последовательности
    :param function: функция фильтрации
    :return: новая отфильтрованная последовательность
    """
    return list(filter(function, iterable))


print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba'))
print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3))
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2))
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3))
