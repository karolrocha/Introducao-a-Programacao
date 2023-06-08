"""Problem Statement

No jogo Minecraft, o jogador precisa escolher um nome de usuário (nickname) para servir como um identificador, que é muito necessário em ambientes multi-jogador.

Esse nickname precisa atender as seguintes restrições:

    Mínimo de 3 caracteres;
    Máximo de 16 caracteres;
    Apenas caracteres alfanuméricos e underlines são permitidos.

Quando Tantan foi escolher seu nickname, ele foi informado que não poderia utilizar espaços na composição do nome de usuário.

Sua tarefa é escrever um programa que gera o nickname baseado no nome da pessoa, para ajudar Tantan com o problema encontrado.

Input

    N

    S

    N - string
    S - string

As linhas de entrada correspondem ao primeiro e último nome do jogador, respectivamente.

Obs:

    A entrada deve ser considerada amigável, ou seja, sempre estará no formato descrito;
    O número total de caracteres sempre vai estar entre 3 e 16.

Output

    K

    K - string

A linha única de saída é composta pelo nickname que vai ser usado pelo usuário, que deve ser formado pela junção do primeiro e último nome do jogador, sem ser separado por espaço."""


N = input()
S = input()

K = N +S

print(K)