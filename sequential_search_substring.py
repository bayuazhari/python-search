def sequential_search_substring(text, substring):
    for i in range(len(text)):
        if text[i:i+len(substring)] == substring:
            return i
    return -1

my_string = "Ini adalah contoh string"
sub = "adalah"
position = sequential_search_substring(my_string, sub)
if position != -1:
    print(f"Substring '{sub}' ditemukan pada posisi {position} dalam string.")
else:
    print(f"Substring '{sub}' tidak ditemukan dalam string.")
