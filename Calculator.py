print("1.Калькулятор \n "'2.Степені \n ''3.Про калькулятор')
a = int(input("Виберіть фукнкцію: "))
if a == 1:
    x = float(input("Введіть перше число: "))
    y = float(input("Введіть друге число: "))
    operation = input('Введіть знак операції: ')
    result = None
    if operation == "+":
        result = x + y
    elif operation == '-':
    elif operation == '*':
        result = x * y
    elif (operation == "/") and (y != 0):
        result = x / y
    else:
        print("Ви поламали калькулятор, перезапустіть його")
    print("Результат: ", result)

elif a == 2:
    b = float(input("Введіть число, яке хочете піднести до степеня: "))
    c = float(input("Введіть степінь: "))
    some = b ** c
    print(some)
elif a == 3:
    print("Версія: v1.0 \n ""©BOMBA Production \n ""Antonio Shyrko")
else:
    print('Гей, придурок, тут тільки 3 можливих функції!!!')
