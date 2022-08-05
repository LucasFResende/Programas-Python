alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

cpf = input('Digite um CPF: ')
cpf = cpf.lower()
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')

for c in alfabeto:
    while c in cpf or len(cpf) != 11:
        cpf = input('Digite um CPF válido: ')

novo_cpf = cpf[:-2]
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
        if novo_cpf == cpf:
            print('O CPF {0}.{1}.{2}-{3} é válido.'.format(novo_cpf[0:3], novo_cpf[3:6], novo_cpf[6:9], novo_cpf[9:]))
            break
        else:
            print(
                'O CPF {0}.{1}.{2}-{3} não é válido'.format(novo_cpf[0:3], novo_cpf[3:6], novo_cpf[6:9], novo_cpf[9:]))
            break
    else:
        continue
