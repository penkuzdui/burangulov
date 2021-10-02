def some_test():  # Функция без параметров
    x = 23
    return x  # Функция возвращает что-либо


def some_test_2(a, b, c):  # Функция с 3 параметрами
    return a * b * c  # Функция возвращает результат умножение чисел


def print_something(word, prefix):  # Функция с 2 параметрами
    print(prefix, "-", word)
    pass  # Функция ничего не возвращает
print(some_test_2(1,3,4))