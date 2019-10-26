i = 5
while i < 15:
    alpha = ' abcdefghijklmnopqrstuvwxyz123456789QWERTYUIOPASDFGHJKLZXCVBNM'
    step = 1
    text = input("Please write your text ").strip()
    res = ''
    for c in text:
        if c.isalpha():
            res += alpha[(alpha.index(c) + step) % len(alpha)]
        else:
            res += c
    print("Result: " + res + "")
