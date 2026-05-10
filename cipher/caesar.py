from cipher.alphabets import ALPHABETS, get_char_alphabet


def encrypt(text: str, key: int) -> str:    
    encrypted = []
    for char in text:
        encrypted.append(_shift_char(char, key))

    return "".join(encrypted)


def decrypt(text: str, key: int) -> str:
    decrypted = []
    for char in text:
        decrypted.append(_shift_char(char, -key))
    
    return "".join(decrypted)


def _shift_char(char: str, offset: int) -> str:
    alphabet = get_char_alphabet(char)
    if not alphabet:
        raise ValueError("В тексте содержатся недопустимые символы!")
    
    current_index = ALPHABETS[alphabet].index(char)
    new_index = (current_index + offset) % len(ALPHABETS[alphabet])

    return ALPHABETS[alphabet][new_index]
