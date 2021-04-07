def del_num():
    try:
        x = input('ВВЕДИТЕ ЧИСЛО: ')
        y = input('ВВЕДИТЕ ЧИСЛО: ')
    except ValueError:
        return
    if x.isalpha() or y.isalpha():
        print('ВЫ ВВЕЛИ НЕ ЧИСЛО!!!')
        return
    elif int(y) == 0:
        print('ДЕЛИТЬ НА НОЛЬ НЕЛЬЗЯ!!!')
        return
    res_value = int(x) / int(y)
    return res_value

print(del_num())
