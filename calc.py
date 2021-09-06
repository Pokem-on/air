while True:


    try:
        pole1 = float(input("Введіть число:\n"))
    except ValueError:
        print("Ви ввели не число! \nПовторіть спчатку!")
        break

    pole2 = input("Виберіть операцію:\n")



    try:
        pole3 = float(input("Введіть число:\n"))
    except ZeroDivisionError:
        print("Ділення на 0! \n Повторіть спочатку!")
        break
    except ValueError:
        print("Ви ввели не число \n Повторіть спочатку!")
        break



    if pole2 == "+":
        print(pole1 + pole3)
    elif pole2 == "-":
        print(pole1 - pole3)
    elif pole2 == "/":
        print(pole1 / pole3)
    elif pole2 == "*":
        print(pole1 * pole3)
    elif pole2 == "^":
        print(pole1 ** pole3)


    dali = input("Хочете продовжити ? [Y/n]\n")

    if dali == "Y":
        print("ok")
    elif dali == "y":
        print("ok")
    elif dali == "N":
        print("gudbay")
        break
    elif dali == "n":
        print("gudbay")
        break