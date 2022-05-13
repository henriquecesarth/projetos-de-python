import cnpj as cnpj_func

def validacao(cnpj):
    if cnpj_func.valida(cnpj):
        print(f'{cnpj} é válido')
    else:
        print(f'{cnpj} é inválido')



# cnpj = '04.252.011/0001-10'
          
# validacao(cnpj)

# cnpj = '10.285.063/0001-95'
        
# validacao(cnpj)

# cnpj = '00.000.000/0000-00'
          
# validacao(cnpj)

# cnpj = '123'

# validacao(cnpj)

# cnpj = 'aaaaaaaaaaa'

# validacao(cnpj)

validacao(cnpj_func.gera())