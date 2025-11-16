text = input("Введите текст: ")
words = text.split()

first_letters = []

for word in words:
    if len(word) >= 3:
        
        first_letter = word[0].upper()
        first_letters.append(first_letter)

result = ''.join(first_letters)

print(result)