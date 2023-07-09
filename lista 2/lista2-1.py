"""Problem Statement

O Intercin está uma loucura de animação!! Estamos na etapa mais animada, em que os times irão competir para prosseguir para as fases finais!! A competição possui 5 partidas classificatórias para a definição do grande vencedor. A métrica analisada para definir o vencedor de cada jogo é: o time que tiver a maior pontuação acumula 1 vitória.

gif

OBS.: você só deve utilizar conceitos que foram vistos até este momento na disciplina.

Input

    A primeira e segunda linha da entrada contém os nomes dos dois times:

    time_1

    time_2

    Em seguida, para cada partida são fornecidos dois valores inteiros, que representam a pontuação que cada time obteve na partida, nesta ordem:

    pontuação_do_time 1

    pontuação_do_time 2

    Vale ressaltar que são no máximo 5 jogos (rodadas), havendo possibilidade de terminar antes, caso um dos times consiga 3 vitórias primeiro. O time que alcançar 3 vitórias primeiro será o grande ganhador no final, independente do número de rodadas que precisou passar. Porém, lembre-se que o número máximo sempre é 5.
    O time que tiver maior pontuação leva a vitória da rodada.

Obs: Nunca há empate nos pontos das rodadas nem das partidas.

Output

    Em cada rodada, após receber a pontuação de cada time, você irá comparar esses pontos e imprimir a mensagem abaixo para o vencedor:

    O vencedor da {n}ª rodada foi: {vencedor_rodada}

    No final, quando um dos times alcançar a condição de 3 vitórias, a seguinte mensagem deve ser impressa para o time vencedor:

    O time {vencedor_partida} ganhou a partida final!

Obs: Caso o número de 3 vitórias seja alcançada antes das 5 rodadas, o programa deve ser encerrado imediatamente, e você não receberá novas entradas"""

time_1 = input()
time_2 = input()
i = 1
vitoria1 = 0
vitoria2 = 0

while i <= 5:
    pontuação_do_time_1 = int(input())
    pontuação_do_time_2 = int(input())

    if pontuação_do_time_1 > pontuação_do_time_2:
        vitoria1 = vitoria1 + 1
        print(f"O vencedor da {i}ª rodada foi: {time_1}")
    else:
        vitoria2 = vitoria2 + 1
        print(f"O vencedor da {i}ª rodada foi: {time_2}")

    if vitoria1 == 3 or vitoria2 == 3:
        break
    i = i + 1

if vitoria1 > vitoria2:
    print(f"O time {time_1} ganhou a partida final!")

else:
    print(f"O time {time_2} ganhou a partida final!")