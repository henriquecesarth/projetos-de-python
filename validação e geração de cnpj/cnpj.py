import re
from random import randint

REGRESSIVOS = [6,5,4,3,2,9,8,7,6,5,4,3,2]

def valida(cnpj):
    """ Valida o CNPJ. Retorna True se for válido e False se for inválido """
    cnpj = remover_caracteres(cnpj) 
    try:
        if eh_sequencia(cnpj):
            return False
    except:
        return False
    try:
        novo_cnpj = calc_novo_cnpj(cnpj)    
    except Exception as e:
        return False

    return compara_cnpj(cnpj, novo_cnpj)

def gera():
    """ Gera um novo CNPJ """
    cnpj = str(randint(0,99999999)) # Gera os 8 primeiros digitos do CNPJ
    cnpj += '0001' # Concatena 0001 ao CNPJ
    cnpj = cnpj.zfill(12) # Insere zeros à esquerda se cnpj tiver menos de 12 digitos para garantir os 12 digitos
    
    novo_cnpj = calc_novo_cnpj(cnpj, gerar=True)
    novo_cnpj = formatar_cnpj(novo_cnpj)
    return novo_cnpj
    
def formatar_cnpj(novo_cnpj):
    """ Formata o CNPJ para o padrão xx.xxx.xxx/0001-xx """
    digitos_cnpj = iter([digito for digito in novo_cnpj])
    novo_cnpj = ''
    for i in range(18):
        if i == 2 or i == 6:
            novo_cnpj += '.'
        elif i == 10:
            novo_cnpj += '/'
        elif i == 15:
            novo_cnpj += '-'
        else:
            novo_cnpj += next(digitos_cnpj)
    return novo_cnpj

def calc_novo_cnpj(cnpj, gerar=False):
    """ Calcula os dois digitos finais do CNPJ baseado no CNPJ fornecido """
    if not gerar: # checa se o CNPJ não está sendo gerado pelo sistema
        novo_cnpj = retirar_dois_ultimos_digitos(cnpj)
    else:
        novo_cnpj = cnpj
    novo_cnpj += primeiro_digito(novo_cnpj)
    novo_cnpj += segundo_digito(novo_cnpj)
    return novo_cnpj

def eh_sequencia(cnpj):
    """ Testa se é uma sequência de números iguais. Ex: 000000000000 """
    if cnpj == cnpj[0]*len(cnpj):
        return True
    else:
        return False

def remover_caracteres(cnpj):
    """ Remove os caracteres que não são números """
    return re.sub(r'[^0-9]', '', cnpj)

def retirar_dois_ultimos_digitos(cnpj):
    """ Retira os dois ultimos digitos do CNPJ """
    return cnpj[:-2]

def calc_digito(soma):
    """ Calcula um dos digitos finais do CPNJ """
    digito = 11 - (soma % 11)
    return digito if digito <= 9 else 0

def soma_cnpj(novo_cnpj, digito):
    """ Soma os digitos do CNPJ de acordo com a regra estabelecida """
    soma = 0
    if digito == 1:
        regressivos = REGRESSIVOS[1:]
    elif digito == 2:
        regressivos = REGRESSIVOS

    for indice, regressivo in enumerate(regressivos):
        soma += int(novo_cnpj[indice])*regressivo
    return soma
    
def primeiro_digito(novo_cnpj):
    """ Retorna o primeiro digito final do CNPJ """
    soma = soma_cnpj(novo_cnpj, digito=1)
    return str(calc_digito(soma))
    
def segundo_digito(novo_cnpj):
    """ Retorna o segundo digito final do CNPJ """
    soma = soma_cnpj(novo_cnpj, digito=2)
    return str(calc_digito(soma))    

def compara_cnpj(cnpj, novo_cnpj):
    """ Compara o CNPJ fornecido com o calculado pelo sistema e retorna verdadeiro ou falso """
    if cnpj == novo_cnpj:
        return True
    else:
        return False