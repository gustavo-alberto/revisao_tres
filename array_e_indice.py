def print_names():
    """
    1. Crie uma função que declara um array com 4 nomes diferentes e imprime cada um deles um embaixo do outro. Ao final faça um commit no GitHub.
    Exemplo de entrada: Nenhuma Exemplo de saída:
    1-João
    2-Maria
    3-Fulano
    4-Ciclano
    """
    names = ["Pedro","José","Maria","João"]
    print("1-", names[0])
    print("2-", names[1])
    print("3-", names[2])
    print("4-", names[3])

def print_first_last_name():
    """
    Crie uma função que declara um array com 4 nomes diferentes e imprime o primeiro e último nome do array. Ao final faça um commit no GitHub.
    Exemplo de entrada : Nenhuma 
    Exemplo de saída: 
    1-João
    4-Beltrano
    """
    names = ["Pedro","José","Maria","João"]
    print("1-", names[0])
    print("4-", names[3])

def print_second_third_index():
    """
    Crie uma função que declara um array com 4 nomes diferentes e imprime o conteúdo do segundo e terceiro índice do array. Ao final faça um commit no GitHub.
    Exemplo de entrada: Nenhuma 
    Exemplo de saída: 
    2-Maria
    3-Fulano
    """
    names = ["Pedro","José","Maria","João"]
    print("3-", names[2])
    print("4-", names[3])

def change_array_names():
    """
    Crie uma função que pede 3 nomes de alimentos digitado pelo usuário e substitui os elementos do array [“Macarrão”, “Pepino”, “Batata”] com esses 3 alimentos. Imprima o nome dos alimentos um abaixo do outro. Ao final faça um commit no GitHub
    array_inicial = [“Macarrão”, “Pepino”, “Batata”]
    Exemplo de entrada: Arroz, Feijão, Farinha
    Exemplo de saída: 
    1 - Arroz
    2 - Feijão
    3 - Farinha
    """
    array_inicial = ["Macarrão", "Pepino", "Batata"]

    alimento1 = input("Digite o primeiro alimento: ")
    alimento2 = input("Digite o segundo alimento: ")
    alimento3 = input("Digite o terceiro alimento: ")

    array_inicial[0] = alimento1
    array_inicial[1] = alimento2
    array_inicial[2] = alimento3

    print("1-", array_inicial[0])
    print("2-", array_inicial[1])
    print("3-", array_inicial[2])