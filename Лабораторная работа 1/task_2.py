list_ = 100 #Количество страниц в книге
string_ = 50 #Количество строк на листе
symbol_ = 25 #Количество символов на строке
weight_symbol = 4 #Вес одного символа
disk_size = 1.44 * 1024 * 1024 #Объём дискеты в байтах

count_of_symbols = list_ * string_ * symbol_
weight_book = count_of_symbols * weight_symbol
count_of_books = disk_size/weight_book

print(f"Количество книг, помещающихся на дискету: {count_of_books:.0f}")
