import os

numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

palavra_secreta = input('Digite a palavra secreta: ')

for c in numeros:
    while c in palavra_secreta:
        palavra_secreta = input('Digite uma palavra válida')

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

palavra_secreta = palavra_secreta.lower()
letras_certas = []
todas_letras_digitadas = []
vidas = 5

while True:
    if vidas == 0:
        print(f'Você perdeu. A palavra secreta era {palavra_secreta}')
        break

    letra = input('Digite uma letra: ')
    letra = letra.lower()

    if len(letra) > 1:
        print('Digite apenas uma letra.\n')
        continue

    if len(letra) == 0:
        print('Digite uma letra.\n')
        continue

    if letra.isnumeric():
        print('Digite uma letra.\n')
        continue

    if letra in todas_letras_digitadas:
        print('Você já digitou essa letra. Digite outra letra.\n')
        continue

    palavra_temporaria = ''

    if letra in palavra_secreta:
        letras_certas.append(letra)
        todas_letras_digitadas.append(letra)
    else:
        vidas -= 1
        todas_letras_digitadas.append(letra)
        print(f'A palavra não possui essa letra. \nVocê tem {vidas} vida(s).')

    for c in palavra_secreta:
        if c in letras_certas:
            palavra_temporaria += f'{c}'
        else:
            palavra_temporaria += f'{"*"}'

    if palavra_temporaria == palavra_secreta:
        print(
            f'Parabéns você acertou! A palavra secreta era {palavra_secreta}')
        break

    print(f'Palavra secreta: {palavra_temporaria} \n')
