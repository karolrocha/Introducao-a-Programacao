"""Problem Statement

futsal A principal modalidade do InterCin vai começar! O futsal chamou a atenção de todas as pessoas do CIn e a equipe de IP/P1 não ficou de fora. O treinador Sérgio Soares selecionou os melhores nomes para representar o time e você vai ajudá-lo em busca do título.

Input

A primeira entrada será a quantidade de partidas que terá no campeonato.

    qtd_partidas = n

Em cada partida, será fornecida a quantidade de rodadas.

    qtd_rodadas = y

    Por y vezes serão fornecidas duas entradas de números inteiros que representam a habilidade, respectivamente, do jogador da Equipe de IP/P1 e do jogador da equipe adversária. Haverá uma disputa entre eles e o que tiver maior habilidade ganha a rodada.

PS: Em caso de empate nas habilidades, a vitória da rodada será contabilizada para a equipe de IP/P1

    habilidade_jogador

    habilidade_adversario

    O time que vencer mais rodadas ganha a partida.

Output

    No começo de cada partida você deve imprimir

    "Vai começar a {fase}º partida. Esse jogo terá {qtdRodadas} rodada(s)."

    Onde {fase} representa qual a partida (1º, 2º, etc...) e {qtd_rodadas} é a quantidade de rodadas que terão nesta partida.

    No final das partidas você deve imprimir:

    "Fim de jogo! O placar foi {placar_equipe}x{placar_adversario}"

    Onde {placar_equipe} e {placar_adversario} são respectivamente a quantidade de vezes que a Equipe IP/P1 ganhou uma rodada e a quantidade de vezes que a equipe adversária ganhou uma rodada.

PS: Se a partida terminar empatada, a Equipe IP/P1 é eliminada e não deverá ocorrer mais nenhuma partida.

    Em caso de eliminação, imprima:

    "Não foi dessa vez! Treinar pro ano que vem!"

    Se a equipe de IP/P1 ganhar uma partida antes da final com uma diferença de 5 ou mais pontos, o campeonato acaba imediatamente, independente da quantidade de partidas jogadas! Imprima:

    "QUE GOLEADAAAA!!! Essa vitória fez os outros times desistirem e a equipe de IP/P1 é a campeã!"

    Caso nenhuma dessas duas opções ocorra, imprima:

    "Vamos para próxima fase!"

Na partida final, os outputs serão diferentes:

        No começo da partida, imprima:

    "Tá na hora da grande final! Esse jogo terá {qtd_rodadas} rodada(s)."

        Em caso de derrota ou empate a mensagem deve ser a seguinte:

    "Ah não!! Chegaram tão longe mas não foi dessa vez. :("

        Caso seja campeão jogando todas as partidas, imprima:

    "É CAMPEÃO! O TIME DE IP/P1 GARANTIU A TAÇA!"""

quantidade_partidas = int(input())
contador_partidas = 0
placar_equipe = 0
placar_adversario = 0
equipe_eliminada = 0
adversario_eliminado = 0
placar_partida_equipe = 0
placar_partida_adversario = 0

while contador_partidas < quantidade_partidas:

    quantidade_rodadas = int(input())
    contador_rodadas = 0

    if contador_partidas == (quantidade_partidas-1):
        print(f"Tá na hora da grande final! Esse jogo terá {quantidade_rodadas} rodada(s).")
    else:
        print(f"Vai começar a {contador_partidas+1}º partida. Esse jogo terá {quantidade_rodadas} rodada(s).")

    placar_adversario = 0
    placar_equipe = 0

    while contador_rodadas < quantidade_rodadas:
        habilidade_jogador = int(input())
        habilidade_adversario = int(input())

        if habilidade_jogador >= habilidade_adversario:
            placar_equipe += 1
        else:
            placar_adversario +=1

        contador_rodadas += 1

    print(f"Fim de jogo! O placar foi {placar_equipe}x{placar_adversario}")

    if placar_equipe > placar_adversario:
        placar_partida_equipe +=1
    else:
        placar_partida_adversario +=1

    if placar_adversario == placar_equipe:
        equipe_eliminada = 1

        if contador_partidas == (quantidade_partidas - 1):
            print("Ah não!! Chegaram tão longe mas não foi dessa vez. :(")
            break
        else:
            print("Não foi dessa vez! Treinar pro ano que vem!")
            break

    elif contador_partidas < (quantidade_partidas-1) and placar_equipe >= (placar_adversario + 5):
        print("QUE GOLEADAAAA!!! Essa vitória fez os outros times desistirem e a equipe de IP/P1 é a campeã!")
        break

    contador_partidas += 1

    if (quantidade_partidas - contador_partidas) >= 1:
        print("Vamos para próxima fase!")

if placar_partida_adversario == 0 and contador_partidas == quantidade_partidas:
    print("É CAMPEÃO! O TIME DE IP/P1 GARANTIU A TAÇA!")





