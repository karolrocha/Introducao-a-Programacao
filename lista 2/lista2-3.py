"""Problem Statement

O InterCIn, a apoteótica gincana entre os alunos do Centro de Informática, está prestes a começar! Porém, o diretório acadêmico precisa da sua ajuda para controlar o estoque de garrafas d'água. Afinal, manter todos hidratados é essencial para a diversão e a energia dos participantes!

meme do homem tremendo bebendo água

Sua missão é criar um programa que gerencie a compra e distribuição das garrafas d'água durante os jogos. Vamos fazer com que cada jogo seja repleto de energia e hidratação para todos os competidores!!!

O campeonato iniciará com 20 garrafas no estoque e foram solicitados 5 voluntários para ajudar na distribuição das garrafas.

Input

Você será responsável por controlar o estoque de garrafas durante uma quantidade indeterminada de rodadas. Assim, a cada início de partida, você receberá uma frase para contabilizar a quantidade de garrafas a serem adicionadas ou retiradas do estoque.

Os inputs poderão ser:

    'Acabou uma partida e precisamos da seguinte quantidade de garrafas para matar a sede dos jogadores'

    'Encham o cooler! O jogo vai começar!!!!'

    'Timeout da partida! Verifiquem quantas garrafas pediram aos voluntários'

    'O InterCIn acabou!!! Vamos verificar nosso estoque de bebidas'

Obs.: o código só deverá encerrar caso o InterCIn acabe ou estoque de garrafas seja insuficiente para atender às necessidades do torneio.

Output

Caso a frase informada seja 'Acabou uma partida e precisamos da seguinte quantidade de garrafas para matar a sede dos jogadores', leia um inteiro, informando a quantidade de jogadores que participaram da partida.

Sabendo que os jogadores terminam a partida com muita sede e que cada um deles beberá uma garrafa d´água, verifique se há garrafas suficientes para hidratar todos os jogadores. Caso não haja garrafas suficientes, imprima a frase:

    'Não teremos água para todos os jogadores... Temos que garantir {n} garrafas!!'

Sendo {n} a quantidade de garrafas que faltam para atender a todos os jogadores que terminaram a partida.

Em seguida, dobre o número de garrafas no estoque e tente novamente atender a todos os jogadores que terminaram a partida. Caso, mesmo após dobrar o estoque, ainda não seja possível fornecer água para todos os jogadores, imprima a frase abaixo e termine o programa:

    'Por questões logísticas, teremos que acabar com os jogos...'

Por sua vez, caso, depois de dobrar o estoque, a quantidade seja suficiente para atender a todos os jogadores, subtraia do estoque uma garrafa para cada jogador.

Caso a frase informada seja 'Encham o cooler! O jogo vai começar!!!!', adicione mais 15 garrafas ao estoque e imprimir a frase:

    'Geladeira cheia!'

Caso a frase informada seja 'Timeout da partida! Verifiquem quantas garrafas pediram aos voluntários', leia 5 números inteiros, representando a quantidade de garrafas solicitadas a cada um dos 5 voluntários:

    quantidade_1

    quantidade_2

    quantidade_3

    quantidade_4

    quantidade_5

Caso o estoque disponível seja menor que o total solicitado aos voluntários, imprima as seguintes frases e termine o programa:

    'Faltaram {n} garrafas para atender o pedido feito aos voluntários'

    'Por questões logísticas, teremos que acabar com os jogos...'

Sendo {n} a quantidade de garrafas que faltam para atender o pedido feito aos voluntários.

Caso a frase informada seja 'O InterCIn acabou!!! Vamos verificar nosso estoque de bebidas', verifique se o estoque é maior que zero. Se for, imprima a seguinde frase e termine o programa:

    'Sobraram {n} garrafas, vamos guardar na geladeira :D'

Onde, [n] é o número de garrafas que sobraram no estoque.

Caso o estoque seja igual a zero, imprima a seguinde frase e termine o programa:

    'Vendemos todas as garrafas! Nosso planejamento foi perfeito!'"""

garrafas = 20

while True:

    frase = input()

    if frase == "Acabou uma partida e precisamos da seguinte quantidade de garrafas para matar a sede dos jogadores":
        jogadores_a_beber = int(input())
        if jogadores_a_beber > garrafas:
            x = jogadores_a_beber - garrafas
            garrafas = 2*garrafas
            print(f"Não teremos água para todos os jogadores... Temos que garantir {x} garrafas!!")
            if jogadores_a_beber > garrafas:
                print("Por questões logísticas, teremos que acabar com os jogos...")
            else:
                garrafas = garrafas - jogadores_a_beber
        else:
            garrafas = garrafas - jogadores_a_beber

    elif frase == "Encham o cooler! O jogo vai começar!!!!":
        garrafas = garrafas + 15
        print("Geladeira cheia!")

        if garrafas < 0:
            print("Por questões logísticas, teremos que acabar com os jogos...")
            break

    elif frase == "Timeout da partida! Verifiquem quantas garrafas pediram aos voluntários":
        quantidade_1 = int(input())
        quantidade_2 = int(input())
        quantidade_3 = int(input())
        quantidade_4 = int(input())
        quantidade_5 = int(input())
        total = quantidade_1 + quantidade_2 + quantidade_3 + quantidade_4 + quantidade_5

        if total > garrafas:
            x = total - garrafas
            print(f"Faltaram {x} garrafas para atender o pedido feito aos voluntários")
            print("Por questões logísticas, teremos que acabar com os jogos...")
            break
        elif total == garrafas or total<garrafas:
            garrafas = garrafas - total

    elif frase == "O InterCIn acabou!!! Vamos verificar nosso estoque de bebidas":
        if garrafas > 0:
            print(f"Sobraram {garrafas} garrafas, vamos guardar na geladeira :D")
            break
        elif garrafas == 0:
            print("Vendemos todas as garrafas! Nosso planejamento foi perfeito!")
            break