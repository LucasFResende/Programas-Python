from random import randrange

novo_cnpj = str(randrange(000000000000, 999999999999))

n1 = 5
n2 = 9
n3 = 4

while True:
    x = 0
    soma1 = 0
    soma2 = 0

    while x < n3:
        for i in range(n1, 1, -1):
            soma1 += int(novo_cnpj[x]) * i
            x += 1

    while n3 <= x < len(novo_cnpj):
        for i in range(n2, 1, -1):
            soma2 += int(novo_cnpj[x]) * i
            x += 1

    soma = soma1 + soma2
    condicao = 11 - (soma % 11)

    if condicao > 9:
        novo_digito = '0'
    else:
        novo_digito = str(condicao)

    novo_cnpj = novo_cnpj + novo_digito

    if len(novo_cnpj) == 14:
        print('Seu CNPJ é {0}.{1}.{2}/{3}-{4}'.format(novo_cnpj[0:2], novo_cnpj[2:5], novo_cnpj[5:8],
                                                           novo_cnpj[8:12], novo_cnpj[12:]))
        break

    n1 += 1
    n3 += 1
