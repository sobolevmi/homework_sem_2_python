# Реализация алгоритма по перемешиванию списка

size = int(input("Введите размер списка: "))
first_list = list(range(1, size + 1))

print(f"Первоначальный список: {first_list}")

second_list = first_list.copy()
third_list = first_list.copy()
second_list = second_list[0: size: 2]
third_list = third_list[1: size: 2]

second_list.reverse()
third_list.reverse()

result_list = second_list + third_list

print(f"Перемешанный список:{result_list}")