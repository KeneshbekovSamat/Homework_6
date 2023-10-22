def choice_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

my_list = [9, 2, 5, 4, 1, 7, 8, 6, 3]

sorted_list = choice_sort(my_list)
print("Отсортированный список:", sorted_list)

target_element = 6


result = binary_search(sorted_list, target_element)
if result != -1:
    print(f"Элемент {target_element} найден на позиции {result}.")
else:
    print(f"Элемент {target_element} не найден.")