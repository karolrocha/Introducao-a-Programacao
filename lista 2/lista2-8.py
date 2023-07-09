"""Problem Statement

Está na hora do Primeiro Campeonato de Vôlei na Grama do InterCin! O torneio acontecerá logo mais e você foi recrutado para monitorar as partidas, anotando as pontuações, os vencedores e outras informações sobre os jogos. Para testar a usabilidade de suas noções de programação, você decidiu criar um programa em Python que analisará as partidas no seu lugar

Seu programa deve funcionar de acordo com o regulamento interno do InterCin, que diz:

1 - O cálculo de um coeficiente usado para descobrir a dupla vencedora, ao final de todas as partidas é: pontos_totais_duplaX * (vitorias_duplaX/numero_de_partidas)

2 - Caso haja empate no placar de uma partida, ou no cálculo da pontuação final da disputa, a dupla 1 vence por ter sido a primeira a chegar na quadra

Obs.1: pontos_totais_duplaX e vitorias_duplaX são variáveis que se referem a todos os pontos e vitórias acumulados durante todas as partidas pela dupla 1 ou pela dupla 2. Isso significa que você deverá calcular o coeficiente tanto da equipe 1 quanto da equipe 2.

Input

Inicialmente, o programa deve receber os nomes dos participantes das duas duplas da seguinte forma:

    equipe1_nome1

    equipe1_nome2

    equipe2_nome1

    equipe2_nome2

Então, o programa recebe a quantidade de partidas que serão disputadas pelas duplas, sempre terá pelo menos uma partida:

    quantidade_partidas

Com o decorrer das partidas, o programa deve receber o placar de cada partida disputada da seguinte forma:

Primeiro recebe a quantidade de pontos da equipe 1 e depois a quantidade de pontos da equipe 2 (em cada partida)

    10

    11

    8

    7

    …

Note que, para o caso acima, o placar da primeira partida foi 10 a 11 e o placar da segunda partida foi 8 a 7

Output

Inicialmente, o programa deve anunciar o início da partida no seguinte modelo:

    "VAMO VER QUEM VAI COMER GRAMA! TEREMOS {quantidade_partidas} PARTIDAS ENTRE:"

    "{equipe1_nome1} e {equipe1_nome2} X {equipe2_nome1} e {equipe2_nome2}"

Ao decorrer das partidas, o programa deve considerar as seguintes regras:

    Caso uma equipe perca uma partida sem fazer nenhum ponto, o torneio se encerra e o programa retorna nada além da mensagem de desistência:

    "JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 1, QUE VERGONHA"

ou

    "JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 2, QUE VERGONHA"

Não existe a possibilidade das duas equipes terminarem a partida com 0 pontos.

Se o torneio acontecer com todas as partidas previamente esperadas, o programa deve retornar os pontos totais marcados na disputa, os vencedores de acordo com o cálculo de vitória previsto no regulamento, a quantidade total de pontos feita pela dupla vencedora e a quantidade de partidas ganhas:

    "CARAMBA! Tivemos um total de {pontos_totais_da_disputa} bolas ao chão ao longo dessa disputa."

    "{nome_vencedor1} e {nome vencedor2} são os grandes vencedores!"

    "Mataram {quantidade_total_de_pontos_da_dupla} bolas, ganhando {quantidade_de_vitorias} partidas"

Obs.2: Caso o torneio encerre antes do final de todas as partidas previstas inicialmente por conta da desistência de uma equipe, você não receberá mais inputs.

Obs.3: É proibido o uso do break para resolver a questão."""

equipe1_nome1 = input()
equipe1_nome2 = input()

equipe2_nome1 = input()
equipe2_nome2 = input()

quantidade_partidas = int(input())
print(f"VAMO VER QUEM VAI COMER GRAMA! TEREMOS {quantidade_partidas} PARTIDAS ENTRE:")
print(f"{equipe1_nome1} e {equipe1_nome2} X {equipe2_nome1} e {equipe2_nome2}")

contador_partidas = 0
parar = False
vitoria_equipe1 = 0
vitoria_equipe2 = 0
ponto_total_equipe1 = 0
ponto_total_equipe2 = 0

while contador_partidas < quantidade_partidas and parar == False:

    ponto_equipe1 = int(input())
    ponto_equipe2 = int(input())

    if ponto_equipe1 == 0:
        print("JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 1, QUE VERGONHA")
        parar = True
    elif ponto_equipe2 ==0:
        print("JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 2, QUE VERGONHA")
        parar = True

    if ponto_equipe1 > ponto_equipe2:
        vitoria_equipe1 +=1
    elif ponto_equipe1 == ponto_equipe2:
        vitoria_equipe1 +=1
    else:
        vitoria_equipe2 +=1

    ponto_total_equipe1 += ponto_equipe1
    ponto_total_equipe2 += ponto_equipe2
    pontos_totais_da_disputa = ponto_total_equipe1 + ponto_total_equipe2

    contador_partidas += 1

    if contador_partidas == quantidade_partidas:

        coeficiente1 = ponto_total_equipe1*(vitoria_equipe1/quantidade_partidas)
        coeficiente2 = ponto_total_equipe2*(vitoria_equipe2/quantidade_partidas)

        if coeficiente2 > coeficiente1:
            nome_vencedor1 = equipe2_nome1
            nome_vencedor2 = equipe2_nome2
            quantidade_total_de_pontos_da_dupla = ponto_total_equipe2
            quantidade_de_vitorias = vitoria_equipe2
        else:
            nome_vencedor1 = equipe1_nome1
            nome_vencedor2 = equipe1_nome2
            quantidade_total_de_pontos_da_dupla = ponto_total_equipe1
            quantidade_de_vitorias = vitoria_equipe1


        print(f"CARAMBA! Tivemos um total de {pontos_totais_da_disputa} bolas ao chão ao longo dessa disputa.")
        print(f"{nome_vencedor1} e {nome_vencedor2} são os grandes vencedores!")

        if quantidade_de_vitorias == 1:
            print(f"Mataram {quantidade_total_de_pontos_da_dupla} bolas, ganhando {quantidade_de_vitorias} partida")
        else:
         print(f"Mataram {quantidade_total_de_pontos_da_dupla} bolas, ganhando {quantidade_de_vitorias} partidas")

        parar = True



