def my_sum():
    global total, num, i
    total = sum(int(i) for int(i) in range(num))
    print(total)
    return total


while True:
    num = input('Введите числа разделенные пробелом! '
                'Для выхода из приложения введите символ / '
                'для продолжения ENTER: ').split()
    total = 0
    for i in num:
        try:
            if i.isalpha():
                print('ВЫ ВВЕЛИ НЕ ЧИСЛО!!!')
            elif i == '/':
                print(my_sum(), 'ВЫХОД')
                break
        except ValueError:
            print('Введите числа или /')
            print(my_sum())
