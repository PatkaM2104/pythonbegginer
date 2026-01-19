A = int(input("aké je A: "))
B = int(input("aké je B: "))
Súčet = A + B
print("Súčet je:", Súčet)


cislo = int(input("Zadaj číslo: "))
if cislo % 2 == 0:
    print("Číslo je párne")
else:
    print("Číslo je nepárne")


a = int(input("Zadaj šírku (a): "))
b = int(input("Zadaj výšku (b): "))

for i in range(b):
    print("*" * a)


a = int(input("Zadaj šírku (a): "))
b = int(input("Zadaj výšku (b): "))

for i in range(b):
    print("*" * i)
