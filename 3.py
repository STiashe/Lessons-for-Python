def my_func(a, b, c):
    val_1 = a + b
    val_2 = b + c
    val_3 = a + c
    max_val = max(val_1, val_2, val_3)
    return max_val


print(my_func(10, 7, 3))
