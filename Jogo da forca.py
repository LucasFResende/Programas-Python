import os

palavra_secreta = input('Digite a palavra secreta: ')

for l in palavra_secreta:
    if l.isnumeric():
        print('Digite uma palavra válida')
        exit()

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

palavra_secreta = palavra_secreta.lower()
letras_digitadas = []
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

    palavra_temporaria = ''

    if letra in palavra_secreta:
        letras_digitadas.append(letra)
    else:
        vidas -= 1
        print(f'A palavra não possui essa letra. \nVocê tem {vidas} vida(s).')

    for l in palavra_secreta:
        if l in letras_digitadas:
            palavra_temporaria += f'{l}'
        else:
            palavra_temporaria += f'{"*"}'

    if palavra_temporaria == palavra_secreta:
        print(
            f'Parabéns você acertou! A palavra secreta era {palavra_secreta}')
        break

    print(f'Palavra secreta: {palavra_temporaria} \n')
