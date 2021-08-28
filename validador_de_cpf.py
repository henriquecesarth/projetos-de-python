# validando cpf
cpf = '206.108.509-11'
cpf_numeros = cpf[0:11]
cpf_numeros = cpf_numeros.replace('.','')

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

# basta testar se os ultimos digitos são iguais ao do cpf original
if cpf[-2] == str(d1) and cpf[-1] == str(d2):
    print(f'{cpf} é um CPF VÁLIDO')
else:
    print(f'{cpf} é um CPF INVÁLIDO')


# se quiser testar todos os digitos use isso
# cpf_novo = ''
# for i in range(12):
#     cpf_novo += cpf[i]

# cpf_novo += str(d1)
# cpf_novo += str(d2)

# if cpf == cpf_novo:
#     print(f'{cpf} é um CPF VÁLIDO')
# else:
#     print(f'{cpf} é um CPF INVÁLIDO')

