def procent(x, y):
    """Сколько процентов от X для y"""
    one_procent = 100/x
    result = y * one_procent
    return result


def print_procent(x, y):
    """Вывод сколько процентов от X для y"""
    print(str(y) + ' это ' + str( procent(x, y)) + '% от ' + str(x))


print_procent(860000, 42000)