def my_func(x=input('ВВЕДИТЕ ЧИСЛО: '), y=input('ВВЕДИТЕ ЧИСЛО: ')):
    if x.isalpha() or y.isalpha():
        print('ВЫ ВВЕЛИ НЕ ЧИСЛО!!!')
    elif int(y) == 0 or int(x == 0):
        print('ЛЮБОЕ ЧИСЛО В НУЛЕВОЙВОЙ СТЕПЕНИ РАВНО = 1! И ЛЮБАЯ СТЕПЕНЬ ДЛЯ НУЛЯ РАВНА = 0!')
        return None
    try:
        res_val = abs(float(x)) ** (abs(int(y))*-1)
    except ValueError:
        return
    return res_val


print(my_func())
