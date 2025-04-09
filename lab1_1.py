import random

def Read_File(filename):
    with open(filename, 'r') as file:
        return file.read()

def Write_File(filename, resultText, Key, replacement_table):
    with open(filename, 'w') as file:
        file.write(f"Result: {resultText}\n")
        file.write(f"Key: {Key}\n")
        file.write("Table:\n")
        for original, replacement in replacement_table.items():
            file.write(f"{original} - {replacement}\n")

def encryption(text, Key):
    resultText = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encryptioned_char = chr(((ord(char) - ord('A') + Key) % 26) + ord('A'))
            else:
                encryptioned_char = chr(((ord(char) - ord('a') + Key) % 26) + ord('a'))
        else:
            encryptioned_char = char
        resultText += encryptioned_char
    return resultText

def create_replacement_table():
    al = 'abcdefghijklmnopqrstuvwxyz'
    num = list(range(10, 100))
    random.shuffle(num)
    replacement_table = {}
    for char in al:
        random_number = num.pop()
        replacement_table[char] = str(random_number)
    return replacement_table

def replacement(text, table):
    replacement_table = table
    replacement_text = ""
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in replacement_table:
                replacement_text += replacement_table[char]
            else:
                replacement_text += char
        else:
            replacement_text += char
    return replacement_text


def decrypted_with_replacement_table(resultText, replacement_table):
    decrypted_result = ""
    i = 0
    while i < len(resultText):
        char = resultText[i]

        if char.isdigit():
            code = char + resultText[i + 1]
            i += 2
            for original, replacement in replacement_table.items():
                if replacement == code:
                    decrypted_result += original
                    break
        else:
            decrypted_result += char
            i += 1
    return decrypted_result

def decrypted_with_Key(resultText, Key):
    decrypted_result = ""
    for char in resultText:
        if char.isalpha():
            char = char.lower()
            decrypted_char = chr(((ord(char) - ord('a') - Key) % 26) + ord('a'))
            if char.isupper():
                decrypted_char = decrypted_char.upper()
        else:
            decrypted_char = char
        decrypted_result += decrypted_char
    return decrypted_result

def read_from_file(filename):
    resultText = ""
    Key = 0
    replacement_table = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("text:"):
                resultText = line.split(":")[1].strip()
            elif line.startswith("Key:"):
                Key = int(line.split(":")[1].strip())
            elif line.startswith("table:"):
                for line in lines[lines.index("table:\n")+1:]:
                    if line.strip():
                        original, replacement = line.strip().split(":")
                        replacement_table[original.strip()] = replacement.strip()
    return resultText, Key, replacement_table

if __name__ == "__main__":
    while True:
        choice = int(input("Введіть дію(1-шифрування, 2-дешифрування) : "))
        if choice == 1:
            replacement_table = create_replacement_table()
            filename = input("Введіть ім'я файлу: ")
            Key = int(input("Введіть відступ: "))
            text = Read_File(filename)
            if text:
                resultText = replacement(encryption(text, Key), replacement_table)
                Write_File("encrypted_" + filename, resultText, Key, replacement_table)
                print(f"Зашифрований текст зберігається у файлі 'encrypted_{filename}'")
        elif choice == 2:
            filename = input("Введіть ім'я файлу: ")
            resultText, Key, replacement_table = read_from_file(filename)
            resultText2 = decrypted_with_replacement_table(resultText, replacement_table)
            decrypted_result = decrypted_with_Key(resultText2, Key)
            print(f"Розшифрований текст: {decrypted_result}")
