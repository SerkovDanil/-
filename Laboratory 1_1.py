numbers = [2, -93, -2, 8, "None",-44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
b1 = len(set(numbers))
print("количество символов:", b1)

m = list()
fl = list()
inter = list()
for i in numbers:
    if isinstance(i, int):
        inter.append(i)
    elif isinstance(i, float):
        fl.append(i)
    elif isinstance(i, str):
        m.append(i)
s = sum(inter)/b1
#  print(m)
#  print(inter)
#  print(fl)
print("средним арифметическим: ", s)

numbers1 = list(map(lambda x: x if x != "None" else s, numbers))

print("Старый список:", numbers)
print("Измененный список:", numbers1)