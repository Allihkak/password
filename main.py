password_ = ''
print()
a = int(input('Введите число в диапазоне 3-20: '))
for i in range(1, a):
    for j in range(i + 1, a + 1):
        s = i + j
        if a % s == 0:
            password_ += str(i) + str(j)
print('Пароль: ', password_)
