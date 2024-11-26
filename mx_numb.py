# создать переменную для хранения максимального числа в массиве
# перебираем массив в цикле
# # сравниваем текущий элемент с переменной для хранения
# # если текущий элемент больше, то пишем его в переменную
# в конце цикла возвращаем переменную

def find_max(list):
    max_number = list[0]

    for i in list:
        if i > max_number:
            max_number = i

    return max_number


def find_min(list):
    min_number = list[0]

    for i in list:
        if i < min_number:
            min_number = i

    return min_number

numbers = [56, 74, 98, 22, 3, 47, 9, 12, -23]

print(find_max(numbers))
print(find_min(numbers))