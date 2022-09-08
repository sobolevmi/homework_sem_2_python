# Программа по созданию списка из n чисел последовательности 1 + 1 / n в степени n и вычисление суммы элементов списка

n = int(input("Введите число: "))

pos = pow((1 + 1 / n), n)

user_list = list()

user_list.append(pos)
sum = user_list[0]

for i in range(1, n):
    user_list.append(user_list[i - 1] + pos)
    sum += user_list[i]

print(user_list)
print(f"Для n = {n} -> {round(sum, 3)}")

