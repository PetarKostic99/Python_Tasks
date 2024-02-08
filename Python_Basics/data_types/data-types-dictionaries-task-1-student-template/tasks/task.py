from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    # Convert the input string to lowercase to ignore the case
    s = s.lower()

    # Initialize an empty dictionary to store the character frequencies
    char_frequency = {}

    for char in s:
        # Update the frequency in the dictionary
        char_frequency[char] = char_frequency.get(char, 0) + 1

    return char_frequency


if __name__ == "__main__":
    assert get_dict('A n a v o l i m i l o v a n a') == {'a': 4, ' ': 14, 'n': 2, 'v': 2, 'o': 2, 'l': 2, 'i': 2,
                                                         'm': 1}
    assert get_dict('Oh, it is python') == {'o': 2, 'h': 2, ',': 1, ' ': 3, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1,
                                            'n': 1}
    assert get_dict('') == {}
