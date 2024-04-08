def count_to_20():
    """
    Crie uma função que imprime uma contagem de 0 a 20. Ao final faça um
    commit no GitHub.
    Exemplo de entrada: Nenhuma
    Exemplo de saída:
    0
    1
    2
    """
    for i in range(21):
        print(i)

def count_to_n():
    """
    Crie uma função que imprime uma contagem de 0 até o número que o
    usuário digitou. Ao final faça um commit no GitHub.
    Exemplo de entrada: 3
    Exemplo de saída:
    0
    1
    2
    3
    """
    try:
        n = int(input("Deseja contar até que número? "))
        for i in range(0, n+1):
            print(i)
    except:
        print("Entrada inválida")
        count_to_n()

def addition_table_2():
    """
    Crie uma função que imprime a tabuada de adição do número 2. Ao final
    faça um commit no GitHub.
    Entrada: Nenhuma
    Exemplo de saída:
    2 + 1 = 3
    2 + 2 = 4
    2 + 3 = 5
    2 + 4 = 6
    """
    for i in range(1,11):
        result = i + 2
        print("2 + {} = {}".format(i, result))