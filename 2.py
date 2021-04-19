with open("out_file.txt", 'r', encoding='utf-8') as out_f:
    line = 0
    for i in out_f:
        line += 1
    print('Количество строк в текстовом файле: ', line)

    words = 0
    for j in i:
        words += len(i.split())
    print('Количество слов в текстовом файле: ', words)
