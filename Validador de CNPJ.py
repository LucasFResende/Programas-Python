alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

cnpj = input('Digite um CNPJ: ')
cnpj = cnpj.lower()
cnpj = cnpj.replace('.', '')
cnpj = cnpj.replace('/', '')
cnpj = cnpj.replace('-', '')

for c in alfabeto:
    while c in cnpj or len(cnpj) != 14:
        cnpj = input('Digite um CNPJ válido: ')
        cnpj = cnpj.lower()
        cnpj = cnpj.replace('.', '')
        cnpj = cnpj.replace('/', '')
        cnpj = cnpj.replace('-', '')

novo_cnpj = cnpj[:-2]

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
        if novo_cnpj == cnpj:
            print(
                'O CNPJ {0}.{1}.{2}/{3}-{4} é válido'.format(cnpj[0:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:]))
            break
        else:
            print('O CNPJ {0}.{1}.{2}/{3}-{4} é inválido'.format(cnpj[0:2], cnpj[2:5], cnpj[5:8], cnpj[8:12],
                                                                 cnpj[12:]))
            break

    n1 += 1
    n3 += 1
