x = 20

my_dict = {el for el in range(20, 240) if el % x == 0}
print(sorted(my_dict))

y = 21

my_dict2 = {el for el in range(20, 240) if el % y == 0}
print(sorted(my_dict2))
