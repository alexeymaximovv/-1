numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
print('Исходный список', numbers)
summa1 = sum(numbers[0:4])
summa2 = sum(numbers[5:])
summa = summa1 + summa2
kolvo = len(numbers)
mid = summa / kolvo
numbers[4] = mid
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
