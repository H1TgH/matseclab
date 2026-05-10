from cipher.caesar import decrypt
from cipher.alphabets import (
    ALPHABETS,
    RU_FREQUENCY,
    EN_FREQUENCY,
    detect_alphabet
)


def calculate_frequency(text: str, alphabet: str) -> dict[str, float]:
    frequency = {char: 0.0 for char in alphabet}

    if not text:
        return frequency

    for char in text:
        frequency[char] += 1

    total = len(text)

    for char in frequency:
        frequency[char] /= total

    return frequency


def calculate_score(frequency: dict[str, float], reference_frequency: dict[str, float], alphabet: str) -> float:
    score = 0.0

    for letter in alphabet:
        actual = frequency.get(letter, 0.0)
        expected = reference_frequency.get(letter, 0.0)
        score += (expected - actual) ** 2

    return score


def crack(text: str) -> tuple[int, str]:
    alphabet_key = detect_alphabet(text)

    alphabet = ALPHABETS[alphabet_key]
    reference_frequency = RU_FREQUENCY if alphabet_key == "ru" else EN_FREQUENCY
    best_score = float("inf")
    best_key = 0
    best_text = ""

    for key in range(len(alphabet)):
        decrypted = decrypt(text, key)

        freq = calculate_frequency(decrypted, alphabet)
        score = calculate_score(freq, reference_frequency, alphabet)

        if score < best_score:
            best_score = score
            best_key = key
            best_text = decrypted

    return best_key, best_text
