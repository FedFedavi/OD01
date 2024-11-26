# факториал 5! 1*2*3*4*5 = 120
# если число 0, то факториал 1
# сравнение с 0, возврат 1 если
# создание переменной для результата
# перебираем циклом вычитая 1 как доходим до 1 стопаем


def find_fact(number):
    if number == 0:
        return 1
    else:
        fact = 1
        i = number
        while i > 0:
            fact = fact * i
            i = i - 1
    return fact


print(find_fact(6))

