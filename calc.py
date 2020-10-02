from colorama import init
from colorama import Fore, Back, Style
init()
def plus():
    a = float(input("Первое значение: "))
    b = float(input("Второе значение: "))
    print(Fore.CYAN + "Будет равно: " + Fore.GREEN + str(a + b))

def minus():
    a = float(input("Первое значение: "))
    b = float(input("Второе значение: "))
    print(Fore.CYAN + "Будет равно: " + Fore.GREEN + str(a - b))
def umnoj():
    a = float(input("Первое значение: "))
    b = float(input("Второе значение: "))
    print(Fore.CYAN + "Будет равно: " + Fore.GREEN + str(a * b))
def delen():
    a = float(input("Первое значение: "))
    b = float(input("Второе значение: "))
    print(Fore.CYAN + "Будет равно: " + Fore.GREEN + str(a / b))
def delen_modul():
    a = float(input("Первое значение: "))
    b = float(input("Второе значение: "))
    print(Fore.CYAN + "Будет равно: " + Fore.GREEN + str(a // b))
def stepen():
    a = float(input("Первое значение: "))
    b = float(input("Второе значение: "))
    print(Fore.CYAN + "Будет равно: " + Fore.GREEN + str(a ** b))
def perimetr_p():
    a = float(input("Первая сторона: "))
    b = float(input("Вторая сторона: "))
    print(Fore.GREEN + str(2*(a + b)) + Fore.RED +" СМ²")
def perimetr_t():
    a = float(input("Первая сторона: "))
    b = float(input("Вторая сторона: "))
    c = float(input("Третья сторона: "))
    print(Fore.GREEN + str(a + b + c) + Fore.RED +" СМ²")
def ploshad_p():
    a = float(input("Первая сторона: "))
    b = float(input("Вторая сторона: "))
    print(Fore.GREEN + str(a * b) + Fore.RED +" СМ³")
def ploshad_k():
    a = float(input("Первая сторона: "))
    print(Fore.GREEN + str(a ** 2) + Fore.RED +" СМ³")
def ploshad_trop():
    a = float(input("Первая сторона: "))
    b = float(input("Вторая сторона: "))
    h = float(input("Высота тропеции: "))
    print(Fore.GREEN + str(0.5 * h * (a + b)) + Fore.RED +" СМ³")

print(Fore.GREEN + """
 _____    ______  ______  _____  _       ' ______  _____ _____                                 
| | \ \  | |     | |  | \  | |  | |       | |  \ \  | |   | |                                  
| |  | | | |---- | |--| <  | |  | |   _   | |  | |  | |   | |                                  
|_|_/_/  |_|____ |_|__|_/ _|_|_ |_|__|_|  |_|  |_| _|_|_ _|_|_                                 
                                                                                               
 _    __  ______   _       ' _    __  _    _   _        ______  _______  ______   ______    2.0
| |  / / | |  | | | |       | |  / / | |  | | | |      | |  | |   | |   / |  | \ | |  | \      
| |-< <  | |__| | | |   _   | |-< <  | |  | | | |   _  | |__| |   | |   | |  | | | |__| |      
|_|  \_\ |_|  |_| |_|__|_|  |_|  \_\ \_|__|_| |_|__|_| |_|  |_|   |_|   \_|__|_/ |_|  \_\      
                                                                                         
""")

print(Fore.YELLOW + "[01] " + Fore.WHITE + " Сложение")
print(Fore.YELLOW + "[02] " + Fore.WHITE + " Вычитание")
print(Fore.YELLOW + "[03] " + Fore.WHITE + " Умножение")
print(Fore.YELLOW + "[04] " + Fore.WHITE + " Деление")
print(Fore.YELLOW + "[05] " + Fore.WHITE + " Деление по модулю (ака, сколько чисел в числе, например в 20-ти четыре 5-ки)")
print(Fore.YELLOW + "[06] " + Fore.WHITE + " Возведение в степень")
print(Fore.YELLOW + "[07] " + Fore.WHITE + " Нахождение периметра прямоугольника")
print(Fore.YELLOW + "[08] " + Fore.WHITE + " Нахождение периметра треугольника")
print(Fore.YELLOW + "[09] " + Fore.WHITE + " Нахождение площади прямоугольника")
print(Fore.YELLOW + "[10] " + Fore.WHITE + " Нахождение площади квадрата")
print(Fore.YELLOW + "[11] " + Fore.WHITE + " Нахождение площади тропеции")
print("\n")
print(Fore.YELLOW + "[00] " + Fore.WHITE + " Выход из приложения")

enter = int(input("=> "))

if enter == 1:
    plus()
elif enter == 2:
    minus()
elif enter == 3:
    umnoj()
elif enter == 4:
    delen()
elif enter == 5:
    delen_modul()
elif enter == 6:
    stepen()
elif enter == 7:
    perimetr_p()
elif enter == 8:
    perimetr_t()
elif enter == 9:
    ploshad_p()
elif enter == 10:
    ploshad_k()
elif enter == 11:
    ploshad_trop()