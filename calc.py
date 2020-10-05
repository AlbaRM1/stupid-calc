from colorama import init
from colorama import Fore, Back, Style
from math import factorial, fmod, frexp, log10, log2, sqrt, acos, asin, atan, hypot, degrees, cosh, sinh, tanh, acosh, asinh, atanh, pi   #конверт ралиан в градусы, обратный гиперболический косинус, обратный гиперболический синус, обратный гиперболический тангенс, число пи.
init()
def plus():
    a = float(input("Первое значение: "))
    b = float(input("Второе значение: "))
    print(Fore.CYAN + "Будет равно: " + Fore.GREEN + str(a + b))
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def minus():
    a = float(input("Первое значение: "))
    b = float(input("Второе значение: "))
    print(Fore.CYAN + "Будет равно: " + Fore.GREEN + str(a - b))
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def umnoj():
    a = float(input("Первое значение: "))
    b = float(input("Второе значение: "))
    print(Fore.CYAN + "Будет равно: " + Fore.GREEN + str(a * b))
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def delen():
    a = float(input("Первое значение: "))
    b = float(input("Второе значение: "))
    print(Fore.CYAN + "Будет равно: " + Fore.GREEN + str(a / b))
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def delen_modul():
    a = float(input("Первое значение: "))
    b = float(input("Второе значение: "))
    print(Fore.CYAN + "Будет равно: " + Fore.GREEN + str(a // b))
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def stepen():
    a = float(input("Первое значение: "))
    b = float(input("Второе значение: "))
    print(Fore.CYAN + "Будет равно: " + Fore.GREEN + str(a ** b))
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def perimetr_p():
    a = float(input("Первая сторона: "))
    b = float(input("Вторая сторона: "))
    print(Fore.GREEN + str(2*(a + b)) + Fore.RED +" СМ²")
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def perimetr_t():
    a = float(input("Первая сторона: "))
    b = float(input("Вторая сторона: "))
    c = float(input("Третья сторона: "))
    print(Fore.GREEN + str(a + b + c) + Fore.RED +" СМ²")
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def ploshad_p():
    a = float(input("Первая сторона: "))
    b = float(input("Вторая сторона: "))
    print(Fore.GREEN + str(a * b) + Fore.RED +" СМ³")
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def ploshad_k():
    a = float(input("Первая сторона: "))
    print(Fore.GREEN + str(a ** 2) + Fore.RED +" СМ³")
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def ploshad_trop():
    a = float(input("Первая сторона: "))
    b = float(input("Вторая сторона: "))
    h = float(input("Высота тропеции: "))
    print(Fore.GREEN + str(0.5 * h * (a + b)) + Fore.RED +" СМ³")
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")


def fact():
    a = int(input("Первое значение: "))
    b = factorial(a)
    c = int(b)
    print(Fore.GREEN + str(c))
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def fm():
    a = float(input("Первое значение: "))
    b = float(input("Второе значение: "))
    c = fmod(a, b)
    print(Fore.GREEN + str(c))
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def xp():
    a = float(input("Первое значение: "))
    c = frexp(a)
    print(Fore.GREEN + str(c))
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def lg10():
    a = float(input("Первое значение: "))
    c = log10(a)
    print(Fore.GREEN + str(c))
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def lg2():
    a = float(input("Первое значение: "))
    c = log2(a)
    print(Fore.GREEN + str(c))
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def koren():
    a = float(input("Первое значение: "))
    c = sqrt(a)
    print(Fore.GREEN + str(c))
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")

''' ------ '''
def af():
    a = float(input("Первое значение: "))
    c = acos(a)
    print(Fore.GREEN + str(c))
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def asi():
    a = float(input("Первое значение: "))
    c = asin(a)
    print(Fore.GREEN + str(c))
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def at():
    a = float(input("Первое значение: "))
    c = atan(a)
    print(Fore.GREEN + str(c))
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def hy():
    a = float(input("Первый катет: "))
    b = float(input("Второй катет: "))
    c = hypot(a, b)
    print(Fore.GREEN + str(c) + Fore.RED + " СМ")
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def co():
    a = float(input("Первое значение: "))
    c = cosh(a)
    print(Fore.GREEN + str(c))
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def sin():
    a = float(input("Первое значение: "))
    c = sinh(a)
    print(Fore.GREEN + str(c))
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def tan():
    a = float(input("Первое значение: "))
    c = tanh(a)
    print(Fore.GREEN + str(c))
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def aco():
    a = float(input("Первое значение: "))
    c = acosh(a)
    print(Fore.GREEN + str(c))
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def asinhh():
    a = float(input("Первое значение: "))
    c = asinh(a)
    print(Fore.GREEN + str(c))
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
def ata():
    a = float(input("Первое значение: "))
    c = atanh(a)
    print(Fore.GREEN + str(c))
    input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")

while True:
  try:
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

    print(Fore.YELLOW + "[12] " + Fore.WHITE + " Нахождение факториала от числа")
    print(Fore.YELLOW + "[13] " + Fore.WHITE + " Нахождение остатка от числа")
    print(Fore.YELLOW + "[14] " + Fore.WHITE + " Возвращает мантиссу и экспоненту числа")
    print(Fore.YELLOW + "[15] " + Fore.WHITE + " Нахождение логарифма по числу 10")
    print(Fore.YELLOW + "[16] " + Fore.WHITE + " Нахождение логарифма по числу 2")
    print(Fore.YELLOW + "[17] " + Fore.WHITE + " Нахождение квадратного корня от числа")
    print(Fore.YELLOW + "[18] " + Fore.WHITE + " Нахождения арккосинус числа")
    print(Fore.YELLOW + "[19] " + Fore.WHITE + " Вычисление гипотенузы треугольника с катетами")
    print(Fore.YELLOW + "[20] " + Fore.WHITE + " Гиперболический косинус")
    print(Fore.YELLOW + "[21] " + Fore.WHITE + " Гиперболический синус")
    print(Fore.YELLOW + "[22] " + Fore.WHITE + " Гиперболический тангенс")
    print(Fore.YELLOW + "[23] " + Fore.WHITE + " Обратный гиперболический косинус")
    print(Fore.YELLOW + "[24] " + Fore.WHITE + " Обратный гиперболический синус")
    print(Fore.YELLOW + "[25] " + Fore.WHITE + " Обратный гиперболический тангенс")
    print(Fore.YELLOW + "[26] " + Fore.WHITE + " Число ПИ")
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
    elif enter == 12:
        fact()
    elif enter == 13:
        fm()
    elif enter == 14:
        xp()
    elif enter == 15:
        lg10()
    elif enter == 16:
        lg2()
    elif enter == 17:
        koren()
    elif enter == 18:
        af()
    elif enter == 19:
        hy()
    elif enter == 20:
        co()
    elif enter == 21:
        sin()
    elif enter == 22:
        tan()
    elif enter == 23:
        aco()
    elif enter == 24:
        asinhh()
    elif enter == 25:
        ata()
    elif enter == 26:
        pi = pi
        print(Fore.GREEN + str(pi))
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 0:
        break
    else:
        print("Вы написали не ту цифру")
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
  except:
      print("Не пиши буквы!")
      input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")