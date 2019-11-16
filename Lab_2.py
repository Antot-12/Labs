def countstr(text_to_count):
    res = {}
    for letter in text_to_count:
        if letter.isalpha():
            res[letter] = text_to_count.count(letter)
    for k in sorted(res):
        print(k + ":" + str(res[k]))


def sort_text(text_to_sort):
    words = text_to_sort.split()
    wordsDict = dict.fromkeys(words, 1)
    wordsDict = sorted(wordsDict)
    print(wordsDict)


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
            user_text = input("""Введіть ваш текст : 
            """)
            countstr(user_text)

            print("Програма виконана! ")
        elif choice == "2":
            print("Ви обрали опрерацію '2' (Посортувати слова в словниковому порядку)")
            user_text = input("""Введіть ваш текст  : 
            """).replace('%', '').replace('$', '').replace('@', '').replace('*', '').replace('.', ' ')\
                .replace('!', ' ').replace('&', '').replace('#', '').replace(';', ' ').replace('(', '')\
                .replace(')', '').replace('№', '').replace(':', '2')\
                .replace('^', '')\

            sort_text(user_text)
            print("Програма виконана!")
        else:
            print("Довбню, ти зламав програму!!! ")


if __name__ == "__main__":
    main()
