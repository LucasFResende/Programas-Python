from random import randrange

novo_cpf = str(randrange(111111111, 999999999))

n = 10

while True:
    x = 0
    soma = 0

    for i in range(n, 1, -1):
        soma += int(novo_cpf[x]) * i
        x += 1

    condicao = 11 - (soma % 11)

    if condicao > 9:
        novo_digito = 0
    else:
        novo_digito = condicao

    novo_cpf = novo_cpf + str(novo_digito)

    n += 1

    if len(novo_cpf) == 11:
        print('Seu CPF é {0}.{1}.{2}-{3}'.format(novo_cpf[0:3],novo_cpf[3:6],novo_cpf[6:9],novo_cpf[9:]))
        break
