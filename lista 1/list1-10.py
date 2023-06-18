"""Problem Statement

O multiverso está desestabilizado e mais uma vez vilões e outros aranhas foram trazidos para Nova York, e os aranhas estão se aliando para lutar contra os vilões.

Numa dessas batalhas, o aranha se depara com um vilão e não sabe se vai conseguir vencer dessa vez

SpiderVerse

Para saber como será o desfecho dessa perigosa aventura, crie um código que mostrará o desenrolar da batalha do Aranha contra o vilão.

Acontecerão 3 confrontos, onde no primeiro confronto o aranha ataca, no segundo confronto o vilão ataca e no 3º o aranha ataca novamente

Como funcionam os confrontos:

•Se o dano do atacante for maior que a defesa do defensor, o atacante ganha

•Se o dano do atacante for igual a defesa do do defensor:

    caso eles não tenham ajuda do parceiro ou ambos tenham ajuda do parceiro na rodada, o aranha ganha pelo "protagonismo"

    caso apenas um tenha ajuda do parceiro, aquele que tiver com um parceiro ganha

•Se a defesa for maior que o dano do atacante, o defensor ganha

Obs.: cada confronto vencido por um personagem deve ser contabilizado, para que ao final possa-se saber quem é o grande vencedor.

Como funciona o fator sorte:

Todo confronto terá o fator sorte, um número de 0 a 3 que muda algumas coisas:

    0, ambos atacam e defendem sozinhos

    1, o atacante ataca com seu parceiro

    2, o defensor defende com seu parceiro

    3, ambos atacam e defendem com seus respectivos parceiros

Como funcionam os parceiros:

O parceiro do aranha é o aliado e o parceiro do vilão é o capanga.

    Caso o atacante esteja com seu parceiro, o seu dano naquela rodada é dado por "dano + danoParceiro"

    Caso o defensor esteja com seu parceiro, a sua defesa naquela rodada é dada por "defesa + defesaParceiro"

    Caso ambos estejam com seus parceiros, o dano do atacante será "dano + danoParceiro" e a defesa do defensor será "defesa + defesaParceiro"

Input

Primeiro, vamos receber o nome do nosso aranha e seus atributos seguido com o nome e atributos dos seu aliado

    nomeAranha

    ataqueAranha

    defesaAranha

    nomeAliado

    ataqueAliado

    defesaAliado

Em seguida, vamos receber os nomes e atributos do vilão e seu capanga

    nomeVilao

    ataqueVilao

    defesaVilao

    nomeCapanga

    ataqueCapanga

    defesaCapanga

E por último, para cada rodada, vamos receber o fator sorte

    fatorSorte

    fatorSorte

    fatorSorte

Output

No início de cada rodada imprima:

    "{n}° confronto:"

Para quando o aranha atacar:

Caso o aranha ganhe:

    "O {nomeAranha} acertou vários golpes no {nomeVilao}"

Caso o aranha perca:

    "O {nomeVilao} está dificultando a vida do {nomeAranha}"

Para quando o aranha defender:

Caso o aranha ganhe:

    "O {nomeAranha} contra-atacou o {nomeVilao}"

Caso o aranha perca:

    "O {nomeAranha} não consegue se defender contra o {nomeVilao}"

Ao final das 3 rodadas:

Se o aranha ganhar a maioria dos confrontos, imprima:

    "O {nomeAranha} e {nomeAliado} conseguiram derrotar o {nomeVilao} e recuperar o multiverso!"

Se o vilão ganhar a maioria dos confrontos, imprima:

    "O {nomeVilao} e {nomeCapanga} invadiram Nova York, onde estão os outros aranhas??"""



nomeAranha = input()
ataqueAranha = int(input())
defesaAranha = int(input())

nomeAliado = input()
ataqueAliado = int(input())
defesaAliado = int(input())

nomeVilao = input()
ataqueVilao = int(input())
defesaVilao = int(input())

nomeCapanga = input()
ataqueCapanga = int(input())
defesaCapanga = int(input())

sorte1 = int(input())
sorte2 = int(input())
sorte3 = int(input())

print("1° confronto:")

if sorte1 == 0:
    if ataqueAranha > defesaVilao:
        aranhaVitoria1 = 1
    elif defesaVilao > ataqueAranha:
        aranhaVitoria1 = 0
    else:
        aranhaVitoria1 = 1

elif sorte1 == 1:
    if (ataqueAranha + ataqueAliado) > defesaVilao:
        aranhaVitoria1 = 1
    elif defesaVilao > (ataqueAranha + ataqueAliado):
        aranhaVitoria1 = 0
    else:
        aranhaVitoria1 = 1

elif sorte1 == 2:
    if ataqueAranha > (defesaVilao + defesaCapanga):
        aranhaVitoria1 = 1
    elif (defesaVilao + defesaCapanga) > ataqueAranha:
        aranhaVitoria1 = 0
    else:
        aranhaVitoria1 = 0

elif  sorte1 == 3:
    if (ataqueAranha + ataqueAliado) > (defesaVilao + defesaCapanga):
        aranhaVitoria1 = 1
    elif (defesaVilao + defesaCapanga) > (ataqueAranha + ataqueAliado):
        aranhaVitoria1 = 0
    else:
        aranhaVitoria1 = 1

if aranhaVitoria1:
    print(f"O {nomeAranha} acertou vários golpes no {nomeVilao}")
else:
    print(f"O {nomeVilao} está dificultando a vida do {nomeAranha}")


print("2° confronto:")

if sorte2 == 0:
    if ataqueVilao > defesaAranha:
        aranhaVitoria2 = 0
    elif defesaAranha > ataqueVilao:
        aranhaVitoria2 = 1
    else:
        aranhaVitoria2 = 1

elif sorte2 == 1:
    if (ataqueVilao + ataqueCapanga) > defesaAranha:
        aranhaVitoria2 = 0
    elif defesaAranha > (ataqueVilao + ataqueCapanga):
        aranhaVitoria2 = 1

    else:
        aranhaVitoria2 = 0

elif sorte2 == 2:
    if ataqueVilao > (defesaAranha + defesaAliado):
        aranhaVitoria2 = 0
    elif (defesaAranha + defesaAliado) > ataqueVilao:
        aranhaVitoria2 = 1
    else:
        aranhaVitoria2 = 1

elif sorte2 == 3:
    if (ataqueVilao + ataqueCapanga) > (defesaAranha + defesaAliado):
        aranhaVitoria2 = 0
    elif (defesaAranha + defesaAliado) > (ataqueVilao + ataqueAliado):
        aranhaVitoria2 = 1
    else:
        aranhaVitoria2 = 1

if aranhaVitoria2 == 1:
    print(f"O {nomeAranha} contra-atacou o {nomeVilao}")
else:
    print(f"O {nomeAranha} não consegue se defender contra o {nomeVilao}")



print("3° confronto:")

if sorte3 == 0:
    if ataqueAranha > defesaVilao:
        aranhaVitoria3 = 1

    elif defesaVilao > ataqueAranha:
        aranhaVitoria3 = 0
    else:
        aranhaVitoria3 = 1

elif sorte3 == 1:
    if (ataqueAranha + ataqueAliado) > defesaVilao:
        aranhaVitoria3 = 1
    elif defesaVilao > (ataqueAranha + ataqueAliado):
        aranhaVitoria3 = 0

    else:
        aranhaVitoria3 = 1

elif sorte3 == 2:
    if ataqueAranha > (defesaVilao + defesaCapanga):
        aranhaVitoria3 = 1
    elif (defesaVilao + defesaCapanga) > ataqueAranha:
        aranhaVitoria3 = 0

    else:
        aranhaVitoria3 = 0

elif  sorte3 == 3:
    if (ataqueAranha + ataqueAliado) > (defesaVilao + defesaCapanga):
        aranhaVitoria3 = 1

    elif (defesaVilao + defesaCapanga) > (ataqueAranha + ataqueAliado):
        aranhaVitoria3 = 0
    else:
        aranhaVitoria3 = 1

if aranhaVitoria3 == 1:
    print(f"O {nomeAranha} acertou vários golpes no {nomeVilao}")
else:
    print(f"O {nomeVilao} está dificultando a vida do {nomeAranha}")

somaVitorias = aranhaVitoria1 + aranhaVitoria2 + aranhaVitoria3

if somaVitorias >= 2:
    print(f"O {nomeAranha} e {nomeAliado} conseguiram derrotar o {nomeVilao} e recuperar o multiverso!")

else:
    print(f"O {nomeVilao} e {nomeCapanga} invadiram Nova York, onde estão os outros aranhas??")
