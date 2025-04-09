def cryptanal():

    freqtable = {
        'a': 0.0804, 'b': 0.0154, 'c': 0.0306, 'd': 0.0399, 'e': 0.1251, 'f': 0.0230, 'g': 0.0196, 'h': 0.0549,
        'i': 0.0726, 'j': 0.0016, 'k': 0.0067, 'l': 0.0414, 'm': 0.0253, 'n': 0.0709, 'o': 0.0760, 'p': 0.0200,
        'q': 0.0011, 'r': 0.0612, 's': 0.0654, 't': 0.0925, 'u': 0.0271, 'v': 0.0099, 'w': 0.0192, 'x': 0.0019,
        'y': 0.0173, 'z': 0.0009
    }

    def calc_freq(text):
        freq = {}
        symbols = 0

        for char in text:
            if char.isalpha():
                char = char.lower()
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
                symbols += 1

        relative_freq = {char: count / symbols for char, count in freq.items()}
        return relative_freq

    def find_key(encrypted_text):
        relative_freq = calc_freq(encrypted_text)
        sort_symbols = sorted(relative_freq, key=lambda x: relative_freq[x], reverse=True)
        most_common_sym_in_text = sort_symbols[0]
        key = ord(most_common_sym_in_text) - ord('e')
        print('Величина відступу:', key)
        return key

    def decrypt(encrypted_text, key):
        decrypted_text = ""
        for char in encrypted_text:
            if char.isalpha():
                char = char.lower()
                decrypted_char = chr(((ord(char) - ord('a') - key) % 26) + ord('a'))
                if char.isupper():
                    decrypted_char = decrypted_char.upper()
            else:
                decrypted_char = char
            decrypted_text += decrypted_char
        return decrypted_text

    if __name__ == "__main__":
        filename = input("Введіть ім'я файлу: ")
        encrypted_text = ""

        try:
            with open(filename, 'r') as file:
                encrypted_text = file.read()
        except FileNotFoundError:
            print(f"Файл '{filename}' не знайдено.")
            exit()

        key = find_key(encrypted_text)

        decrypted_text = decrypt(encrypted_text, key)
        print("Розшифрований текст:")
        print(decrypted_text)

cryptanal()
