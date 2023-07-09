"""Problem Statement

O InterCIn é um campeonato promovido pelo Diretório Acadêmico do Centro de Informática (CIn) que envolve diversas modalidades, tais como futsal, queimado, vôlei, e-sports e xadrez. Logo, focando na inovação deste ano, o InterCIn está chegando com uma modalidade muito sagaz e acirrada: o dominó.

gif

Entretanto, os responsáveis pelo dominó decidiram automatizar, de forma criativa, os pontos adquiridos nessa modalidade e adicionaram algumas regras para os estudantes:

1 - As duplas para essa modalidade serão fixas durante todo o torneio.

2 - As duplas do dominó precisam ser do mesmo período.

3 - Durante a semana do InterCIn, haverá diversas partidas o dia todo e todos os dias.

4 - Cada vitória conquistada pela dupla renderá um ponto.

5 - A pontuação final de cada dupla será a proporção entre o valor da pontuação conquistada no dominó e o período em que as duplas estão.

    PONTUAÇÃO FINAL = (pontuação no dominó) / (período da dupla)

Atenção: considere até duas casas decimais para a pontuação final.

OBS.: caso haja empate entre as duplas, deve-se considerar a primeira dupla que se qualificar como a vencedora ou perdedora e desconsiderar as seguintes com pontuação igual.

Input

Inicialmente, você receberá a variável N que representa a quantidade de duplas que irão competir no dominó:

    N

Em seguida, você receberá as seguintes entradas N vezes.

Primeiro, o nome da dupla

    nome_duplas

O período (em inteiro) em que a dupla está.**

    periodo_duplas

E a quantidade (em inteiro) de pontos realizados pela dupla.**

    pontos_duplas

Output

Você deve se preparar para dois tipos de saídas: uma para mostrar a dupla vencedora e outra para mostrar a dupla perdedora. Saiba que a dupla vencedora será aquela que tiver a maior pontuação final entre todas as duplas. Já a dupla perdedora será aquela que, entre todas as duplas, tiver a menor pontuação final.

Em primeiro momento, você precisa imprimir a dupla vencedora:

    A dupla vencedora foi {dupla_vencedora} com a pontuação final de {pontos_vencedores} pontos.

Em segundo momento, você precisa imprimir a dupla perdedora:

    A dupla perdedora foi {dupla_perdedora} com a pontuação final de {pontos_perdedores} pontos."""

numero_de_duplas = int(input())
i = 0
dupla_vencedora = ""
maior_pontuacao = 0
dupla_perdedora = ""
menor_pontuacao = 1000

while i<numero_de_duplas:
    nome_dupla = input()
    periodo_dupla = int(input())
    pontos_dupla = int(input())

    pontuacao_dupla = pontos_dupla/periodo_dupla

    if pontuacao_dupla > maior_pontuacao:
        maior_pontuacao = pontuacao_dupla
        dupla_vencedora = nome_dupla

    if pontuacao_dupla < menor_pontuacao:
        menor_pontuacao = pontuacao_dupla
        dupla_perdedora = nome_dupla
        

    i = i + 1

print(f"A dupla vencedora foi {dupla_vencedora} com a pontuação final de {maior_pontuacao:.2f} pontos.")
print(f"A dupla perdedora foi {dupla_perdedora} com a pontuação final de {menor_pontuacao:.2f} pontos.")