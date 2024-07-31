#module_1_4.py
def main():
    my_string = input("Введите произвольный текст: ")
    print(f"Количество символов в тексте: {len(my_string)}")
    print("Текст в верхнем регистре:", my_string.upper())
    print("Текст в нижнем регистре:", my_string.lower())
    my_string_no_spaces = my_string.replace(" ", "")
    print("Текст без пробелов:", my_string_no_spaces)
    print("Первый символ строки:", my_string[0])
    print("Последний символ строки:", my_string[-1])
if __name__ == "__main__":
    main()
