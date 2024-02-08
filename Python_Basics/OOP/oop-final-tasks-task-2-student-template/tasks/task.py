class Cipher:
    def __init__(self, keyword):
        self.keyword = keyword.upper()
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.cipher_alphabet = self.generate_cipher_alphabet()

    def generate_cipher_alphabet(self):
        unique_keyword = "".join(sorted(set(self.keyword), key=self.keyword.index))
        remaining_letters = "".join(letter for letter in self.alphabet if letter not in unique_keyword)
        return unique_keyword + remaining_letters

    def encode(self, plaintext):
        encoded_text = ""
        for char in plaintext:
            if char.isalpha():
                is_upper = char.isupper()
                char = char.upper()
                index = self.alphabet.find(char)
                encoded_text += self.cipher_alphabet[index] if is_upper else self.cipher_alphabet[index].lower()
            else:
                encoded_text += char
        return encoded_text

    def decode(self, ciphertext):
        decoded_text = ""
        for char in ciphertext:
            if char.isalpha():
                is_upper = char.isupper()
                char = char.upper()
                index = self.cipher_alphabet.find(char)
                decoded_text += self.alphabet[index] if is_upper else self.alphabet[index].lower()
            else:
                decoded_text += char
        return decoded_text


# Example usage:
cipher = Cipher("crypto")
encoded_text = cipher.encode("Hello world")
print(encoded_text)

decoded_text = cipher.decode("Fjedhc dn atidsn")
print(decoded_text)
