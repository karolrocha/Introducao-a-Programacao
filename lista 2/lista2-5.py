"""Problem Statement

O InterCIn chegou para movimentar o Centro de Informática da UFPE. Com ele, surgiu a nova casa de apostas CInBet, onde os alunos podem apostar nos seus times preferidos.

Como bons alunos de exatas que habitam o CIn, uma equipe de estudantes decidiu realizar uma análise estatística das métricas dos jogos de futsal de dois times: Manchester CIn e SpiCIn Girls. O objetivo dessa análise é determinar o melhor time para fazer apostas na final do InterCIn na casa de apostas CInBet.

Jogo de Futsal

As métricas analisadas para cada jogo e seus respectivos pontos para cada unidade são:

    Gol: +10 pontos
    Chute ao gol: +3 pontos
    Cartão amarelo: -2 pontos
    Cartão vermelho: -4 pontos

Input

A primeira linha da entrada contém um número inteiro N, representando a quantidade de jogos a serem analisados.

Para cada um dos N jogos, são fornecidos cinco valores, nesta ordem:

    Nome do time sendo analisado (será apenas "Manchester CIn" ou "SpiCIn Girls").
    Número de gols.
    Número de chutes ao gol.
    Quantidade de cartões amarelos.
    Quantidade de cartões vermelhos.

Output

Ao final de cada jogo (após receber as entradas), você calculará os pontos que irá adicionar ao total de cada time. Você fará isso da seguinte forma:

    1 - Somar ao total daquele time os pontos que o time ganhará a partir do quanto cada métrica vale (indicado acima):

    Exemplo: se o time fez 2 gols, deve-se adicionar +20 pontos à pontuação daquele time.

    2 - Você deve realizar as seguintes verificações:

        Se a quantidade de gols for maior ou igual a 30% da quantidade de chutes ao gol (no jogo atual), o time ganha 3 pontos.
        Se a quantidade de cartões vermelhos for maior ou igual à quantidade de cartões amarelos (no jogo atual), o time perde 3 pontos.
        Se algum dos times ficar com pontuação negativa (na pontuação acumulada dos jogos anteriores até o jogo atual), não serão mais aceitas outras entradas, mesmo que ainda existam jogos que não foram analisados.

    Caso algum dos times fique com pontuação negativa após receber os dados de um jogo, não serão mais aceitas outras entradas e deve ser impressa apenas a seguinte mensagem:

    "O time {nome_time} ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro."

    Caso nenhum dos times fique com a pontuação negativa, deve-se somar as pontuações finais dos dois times. Em seguida, deve-se verificar a porcentagem de pontos do time vencedor e imprimir:

    "Com {porcentagem_time_vencedor}% dos pontos, o time {nome_time_vencedor} pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn."

Obs': Não haverá empate dos pontos!

Obs'': A porcentagem do time deverá ter duas casas decimais.

    Exemplo de cálculo da porcentagem do time: Se o Manchester CIn fez 15 pontos e o SpiCIn Girls fez 35 pontos, a soma dos dois é 50 pontos. A porcentagem do SpiCIn Girls, por exemplo, é calculada como 35/50 = 70.00%."""

quantidade_de_jogos = int(input())
contador = 0
pontuacao_final_manchester = 0
pontuacao_final_spicin = 0
manchester_eliminado = 0
spicin_eliminado = 0
parar = False
aposta_insegura = False

while contador < quantidade_de_jogos and not parar:
    
    #receber estatísiticas do time
    if not spicin_eliminado and not manchester_eliminado:
        nome_do_time = input()
    
    if (nome_do_time == "Manchester CIn" and not manchester_eliminado) or (nome_do_time == "SpiCIn Girls") and not spicin_eliminado:
        
        numero_de_gols = int(input())
        chutes_ao_gol = int(input())
        cartoes_amarelos = int(input())
        cartoes_vermelhos = int(input())
        
        #somar pontuação
        pontuacao = (numero_de_gols*10) + (chutes_ao_gol*3) - (cartoes_amarelos*2) - (cartoes_vermelhos*4)
        
        #analisar estatíscas do time e somar os pontos adicionais
        if chutes_ao_gol > 0:
            if (numero_de_gols/chutes_ao_gol) >= 0.30:
                pontuacao += 3
            
        if cartoes_vermelhos >= cartoes_amarelos:
            pontuacao -=3
            
        if nome_do_time == "Manchester CIn":

            if pontuacao < 0:
                manchester_eliminado = 1
            pontuacao_final_manchester += pontuacao

        elif nome_do_time == "SpiCIn Girls":
            
            if pontuacao < 0:
                spicin_eliminado = 1

            pontuacao_final_spicin += pontuacao
            
        if pontuacao_final_manchester < 0:
            manchester_eliminado = 1
        
        if pontuacao_final_spicin < 0:
            spicin_eliminado = 1
    
        if pontuacao < 0:
            print(f"O time {nome_do_time} ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.")
            aposta_insegura = True
            break
            
    else:
        break
    
    contador +=1
    
if pontuacao_final_manchester >= 0 and pontuacao_final_spicin >= 0 and aposta_insegura is not True:
    
    soma_pontos = pontuacao_final_manchester + pontuacao_final_spicin
    porcentagem_spicin = pontuacao_final_spicin/soma_pontos
    porcentagem_manchester = pontuacao_final_manchester/soma_pontos
    
    if porcentagem_manchester > porcentagem_spicin:
        porcentagem_time_vencedor = porcentagem_manchester*100
        nome_time_vencedor = "Manchester CIn"
    else:
        porcentagem_time_vencedor = porcentagem_spicin*100
        nome_time_vencedor = "SpiCIn Girls"
    
    print(f"Com {porcentagem_time_vencedor:.2f}% dos pontos, o time {nome_time_vencedor} pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn.")