password = input()

errors = []

if len(password) != 8:
    errors.append("Длина пароля не равна 8")

if not any(char.isupper() for char in password):
    errors.append("В пароле отсутствуют заглавные буквы")

if not any(char.islower() for char in password):
    errors.append("В пароле отсутствуют строчные буквы")

if not any(char.isdigit() for char in password):
    errors.append("В пароле отсутствуют цифры")

special_chars = {'*', '-', '#'}
special = False
invalid = False

for char in password:
    if char in special_chars:
        special = True
    elif not char.isalnum():
        invalid = True

if not special:
    errors.append("В пароле отсутствуют специальные символы")

if invalid:
    errors.append("В пароле используются непредусмотренные символы")

if not errors:
    print("Надежный пароль")
else:
    for error in errors:
        print(error)