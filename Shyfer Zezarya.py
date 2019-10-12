alpha = ' abcdefghijklmnopqrstuvwxyz123456789QWERTYUIOPASDFGHJKLZXCVBNM'
step = 2
text = input("Please write your text ").strip()
res = ''
for c in text:
    res += alpha[(alpha.index(c) + step)%len(alpha)]
print("Result: " + res + "")