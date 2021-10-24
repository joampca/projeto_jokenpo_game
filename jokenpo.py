# Importando as bibliotecas
import random 
from time import sleep 
import os

# Definindo Função para o título
def title():
    print('{:=^40}'.format('\033[7;34;40mJ O K E N P Ô\033[m'))

# Função Principal
def choice():
    lista = ['PEDRA', 'PAPEL', 'TESOURA']
    
    print("""\n- SUAS OPÇÕES - 
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA""")

    # Randomização da escolha do computador
    computer = random.choice(lista)
    # Escolha no usuário
    while True:
        try:
            player = int(input('\nDIGITE A SUA OPÇÃO: '))
            if not 0 <= player <= 2:
                raise ValueError('Opção inválida.. Tente novamente: ')
            break
        except ValueError as error:
            print(error)

    # Timer interativo
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!')

    print('-=-=' * 11)

    # Resultado
    if computer == 'PEDRA': 
        if player == 0:
            print(f'Computador escolheu {computer}\nVocê escolheu PEDRA')
            print('\033[7;33;40mEMPATE\033[m')
        elif player == 1:
            print(f'Computador escolheu {computer}\nVocê escolheu PAPEL')
            print('VOCÊ \033[7;32;40mVENCEU!!!\033[m')
        elif player == 2:
            print(f'Computador escolheu {computer}\nVocê escolheu TESOURA')
            print('VOCÊ \033[7;31;40mPERDEU!!!\033[m')
    elif computer == 'PAPEL':
        if player == 0:
            print(f'Computador escolheu {computer}\nVocê escolheu PEDRA')
            print('VOCÊ \033[7;31;40mPERDEU!!!\033[m')
        elif player == 1:
            print(f'Computador escolheu {computer}\nVocê escolheu PAPEL')
            print('\033[7;33;40mEMPATE\033[m')
        elif player == 2:
            print(f'Computador escolheu {computer}\nVocê escolheu TESOURA')
            print('VOCÊ \033[7;32;40mVENCEU!!!\033[m')
    elif computer == 'TESOURA':
        if player == 0:
            print(f'Computador escolheu {computer}\nVocê escolheu PEDRA')
            print('VOCÊ \033[7;32;40mVENCEU!!!\033[m')
        elif player == 1:
            print(f'computador escolheu {computer}\nVocê escolheu PAPEL')
            print('VOCÊ \033[7;31;40mPERDEU!!!\033[m')
        elif player == 2:
            print(f'Computador escolheu {computer}\nVocê escolheu TESOURA')
            print('\033[7;33;40mEMPATE\033[m')
    # Opção de jogar novamente   
    while True:
        keep = input('QUER JOGAR NOVAMENTE?? [S / N]: ')
        if keep.lower() == 's':
            print('\nReiniciando...')
            sleep(2.0)
            choice()
            os.system('cls')
            title ()
            continue
        elif keep.lower() == 'n':
            sleep (2.0)
            print('\nObrigado, até a próxima')
            sleep (2.0)
            break            

title()
choice()