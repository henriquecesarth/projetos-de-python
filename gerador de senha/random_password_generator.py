from random import sample
from string import ascii_letters, digits, punctuation, ascii_uppercase, ascii_lowercase

total = ascii_letters + digits + punctuation

# gera uma senha que pode ter obrigatoriedades de letras maiusculas, minusculas e caracteres especiais
def generate_password(length, upper=False, lower=False, special=False, number=True):
    while upper or lower or special or number:
        password = "".join(sample(total, length))
        for caracter in password:
            if caracter in ascii_uppercase:
                upper = False
            if caracter in ascii_lowercase:
                lower = False
            if caracter in punctuation:
                special = False
            if caracter in digits:
                number = False
    return password


password = generate_password(8, upper=True, lower=True)

print(f'Senha gerada: {password}')
