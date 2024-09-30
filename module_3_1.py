# Создать переменную calls = 0 вне функций.
calls = 0
# Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
# Функция count_calls подсчитывающая вызовы остальных функций.
def count_calls():
    global calls
    calls += 1

# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
def string_info(string):
    count_calls()
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return (length, upper_case, lower_case)
# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке,
# False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
def is_contains(string, list_to_search):
    count_calls()
    lower_string = string.lower()
    for item in list_to_search:
        if item.lower() == lower_string:
            return True
    return False

# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
print(string_info('Capibara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
# Вывести значение переменной calls на экран(в консоль).
print(calls)