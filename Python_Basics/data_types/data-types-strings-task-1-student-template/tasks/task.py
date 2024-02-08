def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def get_fractions(a_b: str, c_b: str) -> str:
    # Extract numerator and denominator from the input
    a_b_numerator, a_b_denominator = map(int, a_b.split('/'))
    c_b_numerator, c_b_denominator = map(int, c_b.split('/'))

    # Conditions for sucesseful realisation of the function
    if a_b_numerator == 0:
        return c_b
    elif c_b_numerator == 0:
        return a_b
    if a_b_denominator == 0 or c_b_denominator == 0:
        return 'Can not devide with 0'

    # Find the lowest common denominator
    common_denominator = a_b_denominator * c_b_denominator // gcd(a_b_denominator, c_b_denominator)

    # Adjust the numerators based on the common denominator
    a_b_numerator *= (common_denominator // a_b_denominator)
    c_b_numerator *= (common_denominator // c_b_denominator)

    # Additioning
    result_numerator = a_b_numerator + c_b_numerator
    result_denominator = common_denominator

    # Final result
    return a_b + ' + ' + c_b + ' = ' + str(result_numerator) + '/' + str(result_denominator)


if __name__ == "__main__":

    assert get_fractions("3/2", "2/3") == "3/2 + 2/3 = 13/6"
    assert get_fractions("1/6", "2/5") == "1/6 + 2/5 = 17/30"
    assert get_fractions("0/6", "8/3") == "8/3"
    assert get_fractions("6/5", "7/0") == 'Can not devide with 0'
