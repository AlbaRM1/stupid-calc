from colorama import init
from colorama import Fore, Back, Style
from math import factorial, fmod, frexp, log10, log2, sqrt, acos, asin, atan, hypot, degrees, cosh, sinh, tanh, acosh, asinh, atanh, pi   #конверт ралиан в градусы, обратный гиперболический косинус, обратный гиперболический синус, обратный гиперболический тангенс, число пи.
init()

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
    print(Fore.YELLOW + "[18] " + Fore.WHITE + " Нахождения арккосинус")
    print(Fore.YELLOW + "[19] " + Fore.WHITE + " Вычисление арксинусa ")
    print(Fore.YELLOW + "[20] " + Fore.WHITE + " Вычисление гипотенузы треугольника с катетами")
    print(Fore.YELLOW + "[21] " + Fore.WHITE + " Гиперболический косинус")
    print(Fore.YELLOW + "[22] " + Fore.WHITE + " Гиперболический синус")
    print(Fore.YELLOW + "[23] " + Fore.WHITE + " Гиперболический тангенс")
    print(Fore.YELLOW + "[24] " + Fore.WHITE + " Обратный гиперболический косинус")
    print(Fore.YELLOW + "[25] " + Fore.WHITE + " Обратный гиперболический синус")
    print(Fore.YELLOW + "[26] " + Fore.WHITE + " Обратный гиперболический тангенс")
    print(Fore.YELLOW + "[27] " + Fore.WHITE + " Число ПИ")
    print("\n")
    print(Fore.YELLOW + "[00] " + Fore.WHITE + " Выход из приложения")

    enter = int(input("=> "))

    if enter == 1:
        a = float(input("Первое значение: "))
        b = float(input("Второе значение: "))
        print(Fore.CYAN + "Будет равно: " + Fore.GREEN + str(a + b))
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 2:
        a = float(input("Первое значение: "))
        b = float(input("Второе значение: "))
        print(Fore.CYAN + "Будет равно: " + Fore.GREEN + str(a - b))
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 3:
        a = float(input("Первое значение: "))
        b = float(input("Второе значение: "))
        print(Fore.CYAN + "Будет равно: " + Fore.GREEN + str(a * b))
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 4:
        a = float(input("Первое значение: "))
        b = float(input("Второе значение: "))
        print(Fore.CYAN + "Будет равно: " + Fore.GREEN + str(a / b))
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 5:
        a = float(input("Первое значение: "))
        b = float(input("Второе значение: "))
        print(Fore.CYAN + "Будет равно: " + Fore.GREEN + str(a // b))
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 6:
        a = float(input("Первое значение: "))
        b = float(input("Второе значение: "))
        print(Fore.CYAN + "Будет равно: " + Fore.GREEN + str(a ** b))
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 7:
        a = float(input("Первая сторона: "))
        b = float(input("Вторая сторона: "))
        print(Fore.GREEN + str(2*(a + b)) + Fore.RED +" СМ²")
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 8:
        a = float(input("Первая сторона: "))
        b = float(input("Вторая сторона: "))
        c = float(input("Третья сторона: "))
        print(Fore.GREEN + str(a + b + c) + Fore.RED +" СМ²")
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 9:
        a = float(input("Первая сторона: "))
        b = float(input("Вторая сторона: "))
        print(Fore.GREEN + str(a * b) + Fore.RED +" СМ³")
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 10:
        a = float(input("Первая сторона: "))
        print(Fore.GREEN + str(a ** 2) + Fore.RED +" СМ³")
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 11:
        a = float(input("Первая сторона: "))
        b = float(input("Вторая сторона: "))
        h = float(input("Высота тропеции: "))
        print(Fore.GREEN + str(0.5 * h * (a + b)) + Fore.RED +" СМ³")
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 12:
        a = int(input("Первое значение: "))
        b = factorial(a)
        c = int(b)
        print(Fore.GREEN + str(c))
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 13:
        a = float(input("Первое значение: "))
        b = float(input("Второе значение: "))
        c = fmod(a, b)
        print(Fore.GREEN + str(c))
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 14:
        a = float(input("Первое значение: "))
        c = frexp(a)
        print(Fore.GREEN + str(c))
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 15:
        a = float(input("Первое значение: "))
        c = log10(a)
        print(Fore.GREEN + str(c))
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 16:
        a = float(input("Первое значение: "))
        c = log2(a)
        print(Fore.GREEN + str(c))
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 17:
        a = float(input("Первое значение: "))
        c = sqrt(a)
        print(Fore.GREEN + str(c))
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 18:
        a = float(input("Первое значение: "))
        b = acos(a)
        c = degrees(b)
        print(Fore.GREEN + str(c) + Fore.WHITE + " Градусов")
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 19:
        a = float(input("Первое значение: "))
        b = asin(a)
        c = degrees(b)
        print(Fore.GREEN + str(c) + Fore.WHITE + " Градусов")
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 20:
        a = float(input("Первый катет: "))
        b = float(input("Второй катет: "))
        c = hypot(a, b)
        print(Fore.GREEN + str(c) + Fore.RED + " СМ")
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 21:
        a = float(input("Первое значение: "))
        c = cosh(a)
        print(Fore.GREEN + str(c))
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 22:
        a = float(input("Первое значение: "))
        c = sinh(a)
        print(Fore.GREEN + str(c))
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 23:
        a = float(input("Первое значение: "))
        c = tanh(a)
        print(Fore.GREEN + str(c))
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 24:
        a = float(input("Первое значение: "))
        c = acosh(a)
        print(Fore.GREEN + str(c))
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 25:
        a = float(input("Первое значение: "))
        c = asinh(a)
        print(Fore.GREEN + str(c))
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    elif enter == 26:
        a = float(input("Первое значение: "))
        c = atanh(a)
        print(Fore.GREEN + str(c))
        input(Fore.WHITE + "Нажмите " + Fore.YELLOW + " Enter " + Fore.WHITE + " для продолжения")
    
    elif enter == 27:
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