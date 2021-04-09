def data(**kwargs):
    return list(kwargs.values())


def my_func():
    print(data(Имя=input('ВВЕДИТЕ ИМЯ: '),
               Фамилия=input('ВВЕДИТЕ ФАМИЛИЮ: '),
               Год=input('ВВЕДИТЕ ГОД РОЖДЕНИЯ: '),
               Город=input('ВВЕДИТЕ ГОРОД ПРОЖИВАНИЯ: '),
               email=input('ВВЕДИТЕ ЭЛЕКТРОННЫЙ ПОЧТОВЫЙ АДРЕС: '),
               Телефон=input('ВВЕДИТЕ НОМЕР ТЕЛЕФОНА: '),
               ))


my_func()
