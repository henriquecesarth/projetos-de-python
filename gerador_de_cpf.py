from random import randint

cpf_numeros = str(randint(100000000, 999999999))

# testando os 9 primeiros dígitos
total = 0
for i in range(10,1,-1):
    total += int(cpf_numeros[10-i]) * i

test = 11 - (total % 11) 

if test > 9:
    d1 = 0
else:
    d1 = test

cpf_numeros += str(d1)

# testando os 10 primeiros digitos
total = 0
for i in range(11,1,-1):
    total += int(cpf_numeros[11-i]) * i

test = 11 - (total % 11)

if test > 9:
    d2 = 0
else:
    d2 = test

cpf_novo = str(cpf_numeros)
cpf_novo = cpf_novo[:3] + '.' + cpf_novo[3:6] + '.' + cpf_novo[6:9] + '-' + str(d1) + str(d2)

print(cpf_novo)