with open('out_file.txt', 'r', encoding='utf-8') as out_f:
    employee = {}
    for line in out_f:
        key, value = line.split()
        employee = {key: value}
        if int(value) < 20000:
            print(f'Сотрудники с зарплатой менее 20 тыс. рубл.: {key}')
        for key, value in employee.items():
            sum_value = 0
            sum_key = 0
            sum_value += int(value)
            sum_key += 1


print(f'Средний доход сотрудников: {sum_value/sum_key}')
