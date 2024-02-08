def check_str(s: str):
    if not s: return "Input is empty"

    s = s.lower()

    start = 0
    end = len(s) - 1

    # Continue checking characters until the pointers meet or cross
    while start < end:
        # Ignore non-alphanumeric characters from the start
        while start < end and not s[start].isalnum():
            start += 1

        # Ignore non-alphanumeric characters from the end
        while start < end and not s[end].isalnum():
            end -= 1

        if s[start] != s[end]:
            return False

        # Move the pointers towards each other
        start += 1
        end -= 1

    return True


if __name__ == "__main__":
    assert check_str("A dog! A panic in a pagoda!") == True
    assert check_str("Aleksandar radna skela") == True
    assert check_str("1234231") == False
    assert check_str("") == "Input is empty"
