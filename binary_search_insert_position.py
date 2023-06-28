def binary_search_insert_position(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low

data = [2, 4, 6, 8, 10, 12, 14]
target = 7
position = binary_search_insert_position(data, target)
print(f"Elemen {target} dapat disisipkan pada indeks {position} untuk menjaga daftar tetap terurut.")
