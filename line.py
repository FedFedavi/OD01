# O(n) - линейная сложность алгоритма

def line_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    else:
        return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(line_search(arr, 9))
print(line_search(arr, 0))


