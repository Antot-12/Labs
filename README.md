
# 🧪 Python Labs Collection

This repository contains various Python scripts that perform different text processing and basic computational tasks. The scripts include features like reversing text, doubling characters, counting letter frequencies, sorting words, performing basic calculations, and encoding text using a custom algorithm.

## 📋 Overview of Scripts

### 1. **Text Reversal and Doubling Script**

This script contains two small programs:
- **Reverse Words in Sentence**: Reverses the order of characters and words in a given sentence.
- **Double Characters**: Doubles each character in the input sentence.

```python
slogan = str(input("Write your sentence: "))
sentence = slogan[::-1]
words = sentence.split()
sentence_rev = " ".join(reversed(words))
print(sentence_rev)

word = input("Print your sentence, my Lord: ")
p = "".join([x * 2 for x in word])
print(p)
```

### 2. **Text Analysis and Sorting Script**

This script provides a simple command-line interface to:
- **Count the frequency of each letter** in a given text.
- **Sort words alphabetically** after cleaning the text of special characters.

```python
def countstr(text_to_count):
    res = {}
    text_to_count_lower = text_to_count.lower()
    unique_letters = set(text_to_count_lower)
    for letter in unique_letters:
        if letter.isalpha():
            res[letter] = text_to_count_lower.count(letter)
    for k in sorted(res):
        print(k + ":" + str(res[k]))

def sort_text(text_to_sort):
    words = text_to_sort.lower().split()
    unique_words = sorted(dict.fromkeys(words, 1))
    print(unique_words)

def main():
    while True:
        choice = input("""Виберіть ваш варіант:
        1 - Кількість букв в тексті
        2 - Сортувати за абеткою
        3 - Вихід
        Ваш вибір  : """)

        if choice == "3":
            return
        elif choice == "1":
            print("Ви обрали операцію '1' (Обрахувати кількість кожної букви у тексті )")
            user_text = input("Введіть ваш текст: ")
            countstr(user_text)
            print("Програма виконана!")
        elif choice == "2":
            print("Ви обрали операцію '2' (Посортувати слова в словниковому порядку)")
            user_text = input("Введіть ваш текст: ").replace('%', '').replace('$', '').replace('@', '')...
            sort_text(user_text)
            print("Програма виконана!")
        else:
            print("Довбню, ти зламав програму!!!")
```

### 3. **Basic Calculator Script**

This script acts as a basic calculator and also includes a function for calculating powers. Additionally, it provides some basic metadata about the calculator.

```python
print("1. Калькулятор \n 2. Степені \n 3. Про калькулятор")
a = int(input("Виберіть функцію: "))
if a == 1:
    # Calculator operations...
elif a == 2:
    # Power calculation...
elif a == 3:
    print("Версія: v1.0 \n ©BOMBA Production \n Antonio Shyrko")
else:
    print('Гей, придурок, тут тільки 3 можливих функції!!!')
```

### 4. **Simple Text Encoder**

This script encodes text using a basic character substitution method, where each character in the text is shifted by a certain number of steps. It also handles numeric characters with a different shift.

```python
def main():
    alpha = ' abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNMабвгдеєжзиіїйклмнопрстуфхцчшщьюя...'
    step = 2
    step1 = 1
    text = input("Please write your text (000 - exit): ").strip()
    if text == '000':
        return
    # Encoding logic...
    print("Result: " + res)
```

## 🛠️ Usage

To use any of the scripts, clone the repository and run the desired Python script using Python 3.x.

```bash
git clone https://github.com/Antot-12/Labs.git
cd Labs
python script_name.py
```

### 📋 Requirements

- Python 3.x

---

Happy Coding! 💻
