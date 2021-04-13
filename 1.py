from sys import argv


script_name, first_param, second_param, third_param = argv
print("Расчет заработной платы сотрудника: ", script_name)
print("Выработка в часах: ", first_param)
print("Ставка в часах: ", second_param)
print("Премия: ", third_param)
print('Текущая зарплата сотрудника: ',
      int(third_param) + (int(first_param) * int(second_param)))
