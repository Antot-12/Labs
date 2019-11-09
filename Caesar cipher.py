i = True
while i:
    alpha = ' abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
    step = 2
    step1 = 1
    text = input("Please write your text ").strip()
    res = ''
    digit = ''
    for c in text:
        if c.isalpha() or c == ' ':
            if digit:
                res += str(int(digit) + int(step1))
                digit = ''
            res += alpha[(alpha.index(c) + step) % len(alpha)]
        elif c.isnumeric():
            digit += c
        else:
            res += c
    if digit:
        res += str(int(digit) + int(step1))
    print("Result: " + res + "")
