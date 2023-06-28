def binary_search(dictionary, word):
    low = 0
    high = len(dictionary) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_word = dictionary[mid]['word']

        if mid_word == word:
            return dictionary[mid]['definition']
        elif mid_word < word:
            low = mid + 1
        else:
            high = mid - 1
    
    return "Kata tidak ditemukan"

dictionary = [
    {'word': 'apple', 'definition': 'buah apel'},
    {'word': 'banana', 'definition': 'buah pisang'},
    {'word': 'cat', 'definition': 'kucing'},
    {'word': 'duck', 'definition': 'bebek'},
    {'word': 'elephant', 'definition': 'gajah'}
]

word = input("Masukkan kata yang ingin dicari: ")
definition = binary_search(dictionary, word)
print(definition)
