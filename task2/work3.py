# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2**k),
# не превосходящие числа N.



def powers_of_two(N):
    power = 0
    result = 1
    while result <= N:
        print(result)
        power += 1
        result = 2 ** power

N = int(input("Введите число N: "))
print("Целые степени двойки, не превосходящие N:")
powers_of_two(N)
