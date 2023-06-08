"""Problem Statement

Um dos recursos minerais mais úteis do Minecraft é o ferro, pois é abundante no mundo e bom para fazer armas e armaduras. No jogo, a maioria dos itens podem ser agrupados em um conjunto de 64, que é chamado de stack.

Tantan passou alguns dias apenas construindo e finalizou três vilas:

    Hogsmeade
    Kakariko
    Solitude

Como ele já tinha passado bastante tempo minerando e acumulou vários packs de ferro e decidiu dividir todos os packs igualmente entre as vilas. Para ser justo, ele prometeu jogar fora todo o ferro que sobrasse.

Sua tarefa é escrever um programa para mostrar a Tantan como utilizar os seus packs de ferro.

Input

    P

    P - número natural (3 <= P)

A linha única de entrada contém a quantidade de packs de ferro que Tantan tem.

Obs: A entrada deve ser considerada amigável, ou seja, sempre estará no formato descrito.

Output

    V

    F

    V - número natural
    F - número natural

As linhas de saída correspondem ao número de packs ferros que devem ser distribuídos para cada vila e a quantidade que deve ser dispensada."""


packsDeFerro = input("Insira aqui quantos Packs de Ferro você tem:\n")

P = int(packsDeFerro)

V = P/3
F = P%3

print(int(V), F)