import math

def find_ord(number):
    if number <= 1:
        return False

    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False

    return True


print(find_ord(2))
print(find_ord(3))
print(find_ord(5))
print(find_ord(7))
print(find_ord(6))
print(find_ord(19))