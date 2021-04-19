with open("out_file.txt", 'w', encoding='utf-8') as out_f:
    while True:
        data = input('Запишите любые данные построчно или оставьте строку пустой чтобы выйти: ')
        if data == '':
            print('Ввод данных завершен')
            break
        out_f.writelines(data+'\n')


my_f = open("out_file.txt", 'r', encoding='utf-8')

for line in my_f:
    print(line)

my_f.close()
