"""Problem Statement

O Diretório Acadêmico do CIn-UFPE, também conhecido como DA, promoveu durante o InterCIn um torneio insano de Ping Pong em sua famosa sala do bloco A.

Os participantes desse torneio competiam entre si para acumular pontos, que eram recebidos de acordo com a diferença de placar em suas vitórias. Haviam também penalidades que eram aplicadas por diversos motivos, incluindo danos causados as raquetes e bolinhas da sala do DA.

WhatsApp-Video-2023-06-22-at-13 04 15

Após horas de torneio, os organizadores encontraram-se com uma ficha contendo os nomes, pontos e penalidades de cada um dos participantes, mas como estavam ocupados realizando outros torneios pelo CIn, decidiram pedir a ajuda de um calouro muito supimpa, para criar um código que decida de forma precisa quem foi o vencedor!

Input

A primeira entrada do seu código será um número inteiro N, que dirá quantos participantes o torneio teve. Após isso, serão recebidos N conjuntos de entradas contendo os nomes dos participantes, seguidos da sua pontuação total e o total de penalidades recebidas, separados por quebra de linha.

Exemplo:

Renato

100

35

Output

A saída do seu código deve indicar quem foi o vencedor ou vencedora do torneio, subtraindo dos pontos de cada competidor as penalidades que eles receberam. Ao final, quem tiver a maior pontuação vence, e deve ser impressa a seguinte mensagem:

“O grande vencedor do torneio foi {Nome do vencedor} com um total de {Pontuação} pontos!”

Obs: Como os deuses do Ping Pong são muito bondosos com os calouros, eles decidiram que não ocorrerão empates nesse torneio."""


numero_de_participantes = int(input())
i = 1
maior_pontuacao = 0
nome_ganhador = ""


while i <= numero_de_participantes:
    nome = input()
    pontuacao = int(input())
    penalidades = int(input())

    pontuacao_final = pontuacao - penalidades

    if pontuacao_final > maior_pontuacao:
        maior_pontuacao = pontuacao_final
        nome_ganhador = nome


    i = i + 1


print(f"O grande vencedor do torneio foi {nome_ganhador} com um total de {maior_pontuacao} pontos!")


