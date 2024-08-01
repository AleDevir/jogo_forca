'''
exercio 6 do desafio 4. Vamos construir um jogo de forca. O programa escolherá
aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
secreta será representada por espaços em branco, um para cada letra
da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
na palavra secreta, ela será revelada nas posições correspondentes. Se
a letra não estiver na palavra, uma mensagem de erro deverá ser
informada. Após um número máximo de erros, o jogador perde. O jogo
continua até que o jogador adivinhe a palavra ou exceda o número
máximo de tentativas.

'''


import os
from random import choice
import re
import platform
from typing import Final
from typing import Any

# Não esquecer de coloacr duas \\ quando for \
PEDACOS_DO_BONECO:Final[list[str]] = ['',
'''
       F O R C A
         ___
        / _ \\
       | (_) |
        \\___/
         ||
'''
,
'''
       F O R C A
         ___
        / _ \\
       | (_) |
        \\___/
         ||
         ___
       / / 
      / /
     / / 
    /_/
'''
,
'''
       F O R C A
         ___
        / _ \\
       | (_) |
        \\___/
         ||
         ___
       / / \\ \\
      / /   \\ \\
     / /     \\ \\
    /_/       \\_\\
'''
,
'''
       F O R C A
         ___
        / _ \\
       | (_) |
        \\___/
         ||
         ___
       / / \\ \\
      / /| |\\ \\
     / / | | \\ \\
    /_/  | |  \\_\\
'''
,
'''
       F O R C A
         ___
        / _ \\
       | (_) |
        \\___/
         ||
         ___
       / / \\ \\
      / /| |\\ \\
     / / | | \\ \\
    /_/  | |  \\_\\
        _|_|_
       / /
      / /  
     / /    
    /_/      
'''
,
'''
       F O R C A
         ___
        / _ \\
       | (_) |
        \\___/
         ||
         ___
       / / \\ \\
      / /| |\\ \\
     / / | | \\ \\
    /_/  | |  \\_\\
        _|_|_
       / /\\ \\
      / /  \\ \\
     / /    \\ \\
    /_/      \\_\\

    G A M E   O V E R !
'''
]

COR_BRANCA: Final[str] = '\033[0;0m'
COR_BRIGHT_AMARELA: Final[str] = '\033[93m'
COR_VERDE: Final[str] = '\033[32m'
COR_BRIGHT_VERMELHA: Final[str] = '\033[91m'
PALAVRAS_SECRETAS:  Final[list[str]] = [
    'massa',
    'bola',
    'banquete',
    'carro', 
    'cachorro', 
    'adivinha', 
    'elefante',
]
LETRA_VALIDA: Final[str] = r'^[a-zA-Z]$'


# Habilita os caracteres ANSI escape no terminal Windows.
os.system("")

def bright_amarelo(conteudo: Any) -> Any:
    '''
    Colore o texto informado em amarelo brilhante.
    Retorna o texto colorido.
    '''
    return f"{COR_BRIGHT_AMARELA}{conteudo}{COR_BRANCA}"

def verde(conteudo: Any) -> Any:
    '''
    Colore o texto informado em verde.
    Retorna o texto colorido.
    '''
    return f"{COR_VERDE}{conteudo}{COR_BRANCA}"

def bright_vermelho(conteudo: Any) -> Any:
    '''
    Colore o texto informado em vermelho brilhante.
    Retorna o texto colorido.
    '''
    return f"{COR_BRIGHT_VERMELHA}{conteudo}{COR_BRANCA}"

def limpar_console():
    '''
    Limpa o console de acordo com a plataforma.
    '''
    if platform.system() == 'Windows':
        os.system('cls')
    if platform.system() == 'Linux':
        os.system('clear')

def exibir_cabecalho() -> None:
    '''
    Exibe o cabeçalho.
    '''
    limpar_console()
    print(bright_amarelo('*************Jogo da Forca************ \n'))
    print(bright_amarelo(' ATENÇÃO - Seis erros perde o jogo!\n'))

def exibir_boneco(numero_erros: int) -> None:
    '''
    Exibi o corpo do boneco de acordo com o nuúmero de erros.
    '''
    print(f'\n{PEDACOS_DO_BONECO[numero_erros]}')

def escolher_uma_palavra_aleatoriamente() -> str:
    '''
    Uma palavra da lista será escolhida aleatóriamente.
    Retorna a plavra escolhida.
    '''
    palavra_escolhida = choice(PALAVRAS_SECRETAS)
    return palavra_escolhida

def ganhar_o_jogo( letras_corretas:list[str], palavra_secreta:str) -> bool:
    '''
    Ganha quem entra com todas letras da palavra.
    Retorna True ou False.
    '''
    for letra in palavra_secreta:
        if letra not in letras_corretas:
            return False
    return True

def preencher_palavra(letra_informada:str, palavra_secreta:str, palavra_montada:str) -> str:
    '''
    Preenche a palavra quando as letras informadas correspondem a palavra secreta.
    Retorna a palavra montada.
    '''
    letras_palavra_secreta = [*palavra_secreta]
    letras_palavra_montada = [*palavra_montada]

    for indice, letra in enumerate(letras_palavra_secreta):
        if letra_informada == letra:
            letras_palavra_montada[indice] = letra_informada

    return ''.join(letras_palavra_montada)

def get_input(msg: str) -> str:
    '''
    Encapsula as chamadas dos inputs.
    Confeccionada para poder mokar os testes.
    '''
    return input(msg)

def obter_letra() -> str:
    '''
    Obtem uma letra.
    Retorna a letra.
    '''
    while True:
        letra = get_input("\nLetra: ").lower()
        letra_valida = re.match(LETRA_VALIDA, letra)
        if letra_valida:
            return letra
        print(f"'{bright_vermelho(letra)}' Opção inválida! Apenas letra é válida")

def exibir_jogo(palavra_montada:str, erros:list[str], acertos:list[str]) -> None:
    '''
    Exibe o jogo apresentando a palavra sendo montada e as letras certas ou errdas em uma lista.
    '''
    exibir_cabecalho()
    print(bright_amarelo('\n Palavra secreta:'))
    print(bright_amarelo(f'\n {'|'.join(palavra_montada)}\n'))
    print(f"Letras corretas ({verde(' ,'.join(acertos))})")
    print(f"Tentativas erradas: {bright_vermelho(len(erros))}")
    print(f"Letras erradas ({bright_vermelho(' ,'.join(erros))})")

    exibir_boneco(len(erros))

def forca() -> None:
    '''
    Fluxo principal do programa.
    '''
    palavra_secreta = escolher_uma_palavra_aleatoriamente()
    erros: list[str] = []
    acertos: list[str] = []
    palavra_montada = " " * len(palavra_secreta)
    exibir_cabecalho()

    while len(erros) < 6 and not ganhar_o_jogo(acertos, palavra_secreta):
        letra_por_chance = obter_letra()
        if letra_por_chance in erros or letra_por_chance in acertos:
            print(bright_vermelho(f'A letra |{letra_por_chance}| já foi digitada. Tente outra.'))
        else:
            if letra_por_chance in palavra_secreta:
                acertos.append(letra_por_chance)
                palavra_montada = preencher_palavra(
                    letra_por_chance,
                    palavra_secreta,
                    palavra_montada
                )
            else:
                erros.append(letra_por_chance)
            exibir_jogo(palavra_montada, sorted(erros), sorted(acertos))

    if len(erros) < 6:
        print(verde('\n**********************'))
        print(verde('\n**** VOCÊ GANHOU! ****'))
        print(verde('\n**********************'))
    else:
        print(bright_vermelho('\n**********************'))
        print(bright_vermelho('\n**** VOCÊ PERDEU! ****'))
        print(bright_vermelho('\n**********************'))
    print(verde(f'\nA palavra secreta é: {palavra_secreta}'))
