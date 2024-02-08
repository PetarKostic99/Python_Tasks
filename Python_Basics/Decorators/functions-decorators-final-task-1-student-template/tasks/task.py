def split(data: str, sep=None, maxsplit=-1):
    if maxsplit == 0:
        return [data.lstrip()]

    result = []
    current_split = 0
    split_count = 0

    if sep is not None:
        for i in range(len(data)):
            if data[i:i + len(sep)] == sep:
                result.append(data[current_split:i])
                current_split = i + len(sep)
                split_count += 1

                if maxsplit > 0 and split_count >= maxsplit:
                    break

    result.append(data[current_split:].strip())

    if sep is None:
        # If sep is not provided, split the string at whitespaces
        result = [word for word in result[0].split() if word]

    return result


if __name__ == '__main__':
    assert (split('')) == []
    assert (split('    set   3     4')) == ['set', '3', '4']
    assert (split('test')) == ['test']
    assert (split(',123,', sep=',')) == ['', '123', '']
    assert (split('    Hi     8    9', maxsplit=0)) == ['Hi     8    9']
    assert (split('set;:23', sep=';:', maxsplit=0)) == ['set;:23']
    assert (split('adf<>5', sep='<>', maxsplit=1)) == ['adf', '5']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']

