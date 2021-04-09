def del_num(x=input('ВВЕДИТЕ ЧИСЛО: '), y=input('ВВЕДИТЕ ЧИСЛО: ')):
    if x.isalpha() or y.isalpha():
        print('ВЫ ВВЕЛИ НЕ ЧИСЛО!!!')
    elif int(y) == 0:
        print('ДЕЛИТЬ НА НОЛЬ НЕЛЬЗЯ!!!')
    try:
        res_val = int(x) / int(y)
    except ValueError:
        return
    return res_val


print(del_num())
