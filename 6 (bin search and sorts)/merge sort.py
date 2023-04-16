def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Разбиваем массив на две части
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Рекурсивно сортируем каждую половину
    left = merge_sort(left)
    right = merge_sort(right)

    # Объединяем отсортированные половины
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # Сравниваем элементы левой и правой половин
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы из левой и правой половин
    result += left[i:]
    result += right[j:]

    return result

arr=[int(i) for i in input().split()]
print(*merge_sort(arr))