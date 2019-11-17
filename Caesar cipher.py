def main():
    while True:
        alpha = ' abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNMабвгдеєжзиіїйклмнопрстуфхцчшщьюяАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЧШЩЬЮЯ0123456789'
        step = 2
        step1 = 1
        text = input("Please write your text (000 - exit): \n ").strip()
        if text == '000':
            return
        res = ''
        digit = ''
        for c in text:
            if c.isalpha():
                if digit:
                    res += str(int(digit) + int(step1))
                    digit = ''
                res += alpha[(alpha.index(c) + step) % len(alpha)]
            elif c == ' ':
                if digit:
                    res += str(int(digit) + int(step1))
                    digit = ''
                res += c
            elif c.isnumeric():
                digit += c
            else:
                res += c
        if digit:
            res += str(int(digit) + int(step1))
        print("Result: " + res + "")

if __name__ == "__main__":
    main()