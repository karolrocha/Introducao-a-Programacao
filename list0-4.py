""" Problem Statement

Quantidade de diamantes é uma boa forma de medir riqueza no Minecraft pois é um dos recursos minerais mais difícil de ser encontrado e minerado no mapa.
Arthur, Luiz e Pedro decidiram fazer uma competição no Minecraft, para decidir quem iria escolher qual brega que irá tocar durantes suas longas noites de
 programação no CIn e pediram ajuda de Tantan para disponibilizar suas vilas como moradia para cada um. Foi combinado que a competição iria ser realizada 
 dentro do jogo, na qual cada participante iria criar um mundo do zero e teria que encontrar o máximo de diamantes no tempo definido.
Para deixar a competição mais divertida, eles combinaram que cada um iria definir uma restrição para o programa que computaria qual o maior
 valor de diamantes encontrado pelos participantes.

    Luiz definiu que o programa não poderia utilizar nenhuma estrutura condicional em seu código, como IF e outras;
    Pedro proibiu a utilização de quaisquer funções de bibliotecas externas para calcular o máximo da quantidade de diamantes do vencedor;
    Arthur falou que, para encontrar o valor final da quantidade máxima de diamantes, seria obrigatório utilizar a seguinte função para encontrar o máximo entre 2 valores: x = (a + b + (|a - b|)) / 2.

Visando deixar a solução mais simples, Arthur e Pedro chegaram a um acordo e decidiram que seria permitido utilizar funções externas para calcular o valor absoluto de um número (abs(), em Python).

Sua tarefa é escrever o programa que vai auxiliar os três a descobrir o vencedor da competição, em acordo com todas as restrições.

Input

    A

    L

    P

    H

As três primeiras linhas representam a quantidade média de diamantes obtidos por hora de Arthur, Luiz e Pedro, respectivamente.

A quarta linha de entrada é composta por um valor que representa a duração da competição, em horas.

obs: Você deve considerar que a entrada é amigável, ou seja, sempre estará dentro do formato descrito.

Output

    M

A linha única da saída é composta por um valor que representa o valor máximo de diamantes obtido por um participante, na competição."""

A = input()
L = input()
P = input()
H = input()

H = int(H)
A = int(A)*H
L = int(L)*H
P = int(P)*H


maior_entre_A_e_L = (A + L + (abs(A-L))) / 2
M = (maior_entre_A_e_L + P + (abs(maior_entre_A_e_L-P))) / 2

print(f"{M: .0f}")



