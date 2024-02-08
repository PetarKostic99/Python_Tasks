def get_longest_word(s: str) -> str:
    if not s:
        return "Input is empty"
    current_word = ""
    longest_word = ""
    max_length = 0

    for char in s:
        if char.isspace():
            # Found a whitespace character, consider the current word
            if len(current_word) > max_length:
                longest_word = current_word
                max_length = len(current_word)
            current_word = ""  # Reset current word
        else:
            current_word += char

    # Check the last word in case the string doesn't end with whitespace
    if len(current_word) > max_length:
        longest_word = current_word

    return longest_word


if __name__ == "__main__":
    assert get_longest_word('Python is simple and effective!') == 'effective!'
    assert get_longest_word('Pythonista simple and effective!') == 'Pythonista'
    assert get_longest_word('') == 'Input is empty'
