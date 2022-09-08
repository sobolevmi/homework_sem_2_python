# Программа по вычислению вхождений одной строки в другую

user_string_1 = str(input("Введите первую строку: "))

user_string_2 = str(input("Введите вторую строку: "))

count = 0
result = 0

if len(user_string_1) > len(user_string_2):
    for index in range(0, len(user_string_1) - 1):
        for i in range(0, len(user_string_2) - 1):
            if user_string_2[i] == user_string_1[i]:
                count += 1
            if count == len(user_string_2) - 1:
                result += 1
        user_string_1 = user_string_1.replace(user_string_1[index], " ")
    print(f"Количество вхождений второй строки в первую строку: {result}")
elif len(user_string_2) > len(user_string_1):
    for index in range(0, len(user_string_2) - 1):
        for i in range(0, len(user_string_1) - 1):
            if user_string_1[i] == user_string_2[i]:
                count += 1
            if count == len(user_string_1) - 1:
                result += 1
        user_string_2 = user_string_2.replace(user_string_2[index], " ")
    print (f"Количество вхождений первой строки во вторую строку: {result}")
elif len(user_string_1) == len(user_string_2):
    print("Строки не могут быть равны")

