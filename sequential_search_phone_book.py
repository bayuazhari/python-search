def is_similar(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()

    if name1[0] == name2[0]:
        return True
    
    return False


def sequential_search(telepon, nama):
    for i in range(len(telepon)):
        if is_similar(telepon[i]['nama'], nama):
            return telepon[i]['nomor']
    
    return "Nama tidak ditemukan"


telepon = [
    {'nama': 'John Doe', 'nomor': '1234567890'},
    {'nama': 'Jane Smith', 'nomor': '9876543210'},
    {'nama': 'Michael Johnson', 'nomor': '4567890123'},
    {'nama': 'Emily Davis', 'nomor': '7890123456'}
]

nama = input("Masukkan nama yang ingin dicari: ")
nomor_telepon = sequential_search(telepon, nama)
print(nomor_telepon)
