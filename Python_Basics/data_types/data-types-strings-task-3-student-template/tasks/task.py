def replacer(s: str) -> str:
    if not s: return '''Input is empty'''
    result = ''
    for char in s:
        if char == '"':
            result += "'"
        elif char == "'":
            result += '"'
        else:
            result += char
    return result


if __name__ == "__main__":
    assert replacer(''' ' ' ' ''') == ''' " " " '''
    assert replacer(''' " " " ''') == ''' ' ' ' '''
    assert replacer('''This 'is' my "example" ''') == '''This "is" my 'example' '''
    assert replacer('''''') == '''Input is empty'''
