from cipher.alphabets import ALPHABETS


def normalize_text(raw_text: str) -> str:
    text = raw_text.lower().replace("ё", "е")

    allowed_chars = set(ALPHABETS["ru"] + ALPHABETS["en"])

    return "".join(char for char in text if char in allowed_chars)


def group_by_five(text: str) -> str:
    chunks = [text[i:i + 5] for i in range(0, len(text), 5)]
    return " ".join(chunks)


# def detect_alphabet(text: str) -> str:
#     if not text:
#         raise ValueError("Пустой текст")

#     ru_set = set(ALPHABETS["ru"])
#     en_set = set(ALPHABETS["en"])

#     has_ru = any(char in ru_set for char in text)
#     has_en = any(char in en_set for char in text)

#     if has_ru and has_en:
#         raise ValueError("Смешанный алфавит не поддерживается.")

#     if has_ru:
#         return "ru"
#     if has_en:
#         return "en"

#     raise ValueError("Не удалось определить алфавит.")
