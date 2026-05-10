from cipher.text_utils import group_by_five, normalize_text
from cipher.caesar import encrypt, decrypt
from cipher.cracker import crack


def main():
    try:
        operation = int(input("Введите нужный режим "))
    except ValueError:
        raise ValueError("Режим должен быть числом 0, 1 или 2")

    text = input("Введите исходный текст: ")
    text = normalize_text(text)

    if not text:
        raise ValueError("Исходный текст должен содержать хотя бы одну букву из доступных алфавитов (латиница, кириллица).")

    if operation == 0:
        try:
            key = int(input("Введите ключ шифрования: "))
        except ValueError:
            raise ValueError("Ключ должен быть целым числом.")

        result = encrypt(text, key)

    elif operation == 1:
        try:
            key = int(input("Введите ключ шифрования: "))
        except ValueError:
            raise ValueError("Ключ должен быть целым числом.")

        result = decrypt(text, key)

    elif operation == 2:
        key, result = crack(text)
        print(f"\nНайденный ключ: {key}")

    else:
        raise ValueError("Недопустимая операция (0/1/2)")

    grouped = group_by_five(result)

    print(grouped)


if __name__ == "__main__":
    main()