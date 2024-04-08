"""
Regras:
a. Pedra ganha de Tesoura, mas perde para Papel.
b. Papel ganha de Pedra, mas perde para Tesoura.
c. Tesoura ganha de Papel, mas perde para Pedra.
d. O jogo vai dizer quem ganhou ou se foi empate.

Valores:
0 - PEDRA
1 - PAPEL
2 - TESOURA
"""

import random

def main():
    continue_flag = True
    while continue_flag == True:
        Jogar()
        continue_flag = ask_continue()
            
def Jogar():
    # Menu
    print("\nBem-vindo ao Jokenpo!\n")
    print("Escolha uma opção para jogar: ")
    print("[0] Pedra")
    print("[1] Papel")
    print("[2] Tesoura")

    # Lista para relacionar as opções com os índices
    lista_opcoes = ["Pedra", "Papel", "Tesoura"]

    escolha_usuario = user_choice()
    escolha_cpu = cpu_choice()
    resultado = battle(escolha_usuario, escolha_cpu)

    # Resultado
    print("JO KEN POH!!!")
    print("-=-=-=-=-=-=-=-=-=-=")
    print("O computador escolheu: ", lista_opcoes[escolha_cpu])
    print("O jogador escolheu: ", lista_opcoes[escolha_usuario])
    print("-=-=-=-=-=-=-=-=-=-=")
    print(resultado)
   
def user_choice():
    valid_options = [0, 1, 2]
    choice = None
    while choice not in valid_options:
        try:
            choice = int(input("Digite sua escolha: "))
            if choice not in valid_options:
                raise ValueError
        except ValueError:
            print("Escolha inválida")
    return choice

def cpu_choice():
    choice = random.choice([0, 1, 2])
    return choice

def battle(user_choice, cpu_choice):
    user_choice = user_choice
    cpu_choice = cpu_choice

    if user_choice == cpu_choice:
        return "Empate!"
    elif (user_choice == 0 and cpu_choice == 2) or (user_choice == 1 and cpu_choice == 0) or (user_choice == 2 and cpu_choice == 1):
        return "Jogador venceu!"
    else:
        return "Computador venceu!"
    
def ask_continue():
    continuar = input("Deseja jogar novamente? (S/N): ")
    continuar = continuar.lower() # força a conversão para lowercase
    if continuar == 's':
        return True
    if continuar == 'n':
        return False
    if continuar != 's' or continuar !='n':
        print("Opção inválida")
        ask_continue()

main()