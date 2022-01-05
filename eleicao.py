#Digite 1 para continuar ou 2 para parar, digite sua idade e por fim veja os resultados

obrigatorio = 0
facultativo = 0
nao_eleitor = 0
total = 0

while True:
    ctrl = int(input('Você deseja cadastrar um usuário? \n'
                     'Digite 1 para SIM \t'
                     'Digite 2 para NÃO \n'))

    if ctrl == 2:
        break
    elif ctrl == 1:
        idade = int(input('Quantos anos você tem? \n'))

        if idade >= 18 and idade <= 69:
            obrigatorio = obrigatorio + 1
            print('Eleitor obrigatório\n')
        elif idade == 16 or idade == 17 or idade >= 70:
            facultativo = facultativo + 1
            print('Eleitor facultativo\n')
        elif idade < 16:
            nao_eleitor = nao_eleitor + 1
            print('Eleitor não elegível\n')
        else:
            print('Valor não disponivel\n')
        total = obrigatorio + facultativo + nao_eleitor
    else:
        print('Verifique os números novamente \n')

print('Há {} moradores do qual o voto é obrigatório;'.format(obrigatorio))
print('Há {} moradores do qual o voto é facultativo;'.format(facultativo))
print('Há {} moradores do qual não são eleitores;'.format(nao_eleitor))
print('O total de moradores são {} pessoas.'.format(total))
