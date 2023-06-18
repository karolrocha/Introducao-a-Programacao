"""Problem Statement

Em busca do seu objetivo final, o Miles acaba errando o caminho e então entra no Universo onde ele encontra o Venom Extreme. Agora o Miles seguirá o Venom, que deve derrotar todos os inimigos que encontrar pelo caminho para chegar até o portal do Nether e então viajar até outro Universo.

venom_extreme

O Venom que você encontrou possui os seguintes atributos: vida, ataque e poção de cura.

Informações:

    Vida: O Venom terá uma vida inicial que é a vida máxima que ele pode atingir.

    Poção: A poção de cura só pode ser consumida por completo. Ou seja, o Venom só poderá consumir a poção caso a soma do valor da poção com a sua vida atual não ultrapasse a sua vida máxima. Além disso, ela deve ser consumida depois de cada turno.

Em relação aos inimigos, haverá 2:

1 - Creeper: é o inimigo do turno 1. O dano dele será igual ao dano do Venom. Além disso, o Venom tentará tomar uma poção ao fim da batalha contra o Creeper, caso ainda esteja vivo.

2 - Druida: é o inimigo do turno 2. Ele obrigará o Venom a beber a poção antes do início do turno, ao invés do final. Entretanto, caso a poção exceda a quantidade de vida máxima do Venom, ela não fará efeito e se tornará um veneno, causando dano ao Venom. A taxa de envenenamento é a diferença entre a vida atual do Venom e da sua vida máxima. Então, o ataque dele será o ataque do druida (fornecido na entrada) + taxa de envenenamento.

Em cada turno, ambos os personagens atacam simultaneamente, descontando o valor de seus ataques da vida do oponente e para saber quem venceu você deve seguir a seguinte ordem de critérios de desempate:

1º Critério - Quando um ou os dois personagens morrem. Note que, caso os dois morram, uma derrota deve ser contabilizada para o Venom.

2º Critério - Quem causou mais dano vence.

3º Critério - Quem está mais perto de morrer, ou seja, quem está com a vida mais próxima de 0 (zero) perde.

4º Critério - Se houver empate em todos os critérios acima, uma derrota deve ser contabilizada para o Venom.

PS: Caso o Venom perca no primeiro turno, o segundo turno não ocorrerá.

Input

    Inicialmente você receberá 3 inputs relacionados ao Venom:

    vida_maxima_venom

    ataque_venom

    pocao_venom

    Em seguida, você receberá mais 1 input indicando a vida do Creeper, referente ao primeiro turno:

    vida_creeper

    Por fim, você receberá mais 2 inputs com a vida do Druida e o ataque do Druida, referentes ao segundo turno:

    vida_druida

    ataque_druida

Output

Antes de cada duelo, imprima a seguinte frase:

    SENHORAS E SENHORES! AGORA O VENOM ENFRENTARÁ O {INIMIGO}!

Obs: No print acima, o nome do inimigo deve estar todo em letras maiúsculas.

Em seguida, para cada turno:

    Se Venom, o inimigo ou ambos morrerem, exiba a seguinte mensagem para cada um:

    O {personagem} não tankou e foi de base...

Obs: No print acima, o nome do personagem deve estar todo em letras minúsculas.

Obs2: Caso os dois personagens do duelo morram, o primeiro print que deve aparecer é o do Venom.

    Caso ninguém morra naquele turno, imprima:

    Vida atual do Venom: {vida_venom}

    Dano sofrido pelo Venom: {dano_recebido_venom}

    Vida atual do {inimigo}: {vida_inimigo}

    Dano sofrido pelo {inimigo}: {dano_recebido_inimigo}

    Se o Venom vencer o creeper em quaisquer dos critérios, imprima:

    Isso aí! Ele é todo esquentadinho, mas no final deu tudo certo!

    Caso ele perca para o creeper em quaisquer dos critérios, imprima:

    AH NÃO! O VENOM PEGOU EM BOMBA!

    Caso ele vença o druida em quaisquer dos critérios, imprima:

    Quase me dei mal, nunca mais aceito nada de estranho...

    Caso ele perca para o druida em quaisquer dos critérios, imprima:

    Pelo visto a poção tava fora do prazo de validade :(

    Caso o Venom possa tomar uma poção com sucesso, quando não forçado pelo druida, imprima:

    Ah! Essa poção é da boa!

Ao final dos dois turnos, caso o Venom consiga alcançar o portal com o Miles (ou seja, caso o Venom vença todos os inimigos), imprima:

    Essa aventura foi epicamente épica, meu amigo! Boa viagem aí! * Começa a tocar saxofone *

Caso o Venom não tenha vencido ao menos uma batalha, imprima:

    Pelo visto as aventuras do Miles terminaram por aqui..."""


vida_maxima_venom = int(input())
ataque_venom = int(input())

pocao_venom = int(input())

vida_creeper = int(input())


vida_druida = int(input())

ataque_druida = int(input())

vida_venom = vida_maxima_venom
desempate1 = 1
desempate2 = 1
venom_vence1 =0
venom_vence2 = 0
envenenamento = 0

#turno 1

print("SENHORAS E SENHORES! AGORA O VENOM ENFRENTARÁ O CREEPER!")

vida_venom = vida_venom - ataque_venom
vida_creeper = vida_creeper - ataque_venom

dano_venom1 = ataque_venom

if vida_venom <= 0:
    print("O venom não tankou e foi de base...")

if vida_creeper <=0:
    print("O creeper não tankou e foi de base...")

if vida_venom <= 0:
    if vida_creeper > 0:
        venom_vence1 = 0
        desempate1 = 0
        print("AH NÃO! O VENOM PEGOU EM BOMBA!")


if vida_creeper <=0:
    if vida_venom > 0:
        venom_vence1 = 1
        desempate1 = 0
        print("Isso aí! Ele é todo esquentadinho, mas no final deu tudo certo!")


if vida_creeper > 0 and vida_venom > 0:
    print(f"Vida atual do Venom: {vida_venom}")
    print(f"Dano sofrido pelo Venom: {dano_venom1}")
    print(f"Vida atual do creeper: {vida_creeper}")
    print(f"Dano sofrido pelo creeper: {ataque_venom}")

#começa o desempate

if desempate1:

    if vida_venom <= 0 and vida_creeper <= 0:
        venom_vence1 = 0
        print("AH NÃO! O VENOM PEGOU EM BOMBA!")

    elif vida_venom > vida_creeper:
        venom_vence1 = 1
        print("Isso aí! Ele é todo esquentadinho, mas no final deu tudo certo!")

    elif vida_creeper > vida_venom:
        venom_vence1 = 0
        print("AH NÃO! O VENOM PEGOU EM BOMBA!")

    else:
        venom_vence1 = 0
        print("AH NÃO! O VENOM PEGOU EM BOMBA!")

if vida_venom > 0:
    if (vida_maxima_venom - vida_venom) >= pocao_venom:
        vida_venom = vida_venom + pocao_venom

#turno 2

if venom_vence1 == 1:
    if (vida_maxima_venom - vida_venom) >= pocao_venom:
        vida_venom = vida_venom + pocao_venom
        print("Ah! Essa poção é da boa!")
    else:
        envenenamento = vida_venom + pocao_venom - vida_maxima_venom
        vida_venom = vida_maxima_venom - envenenamento

    print("SENHORAS E SENHORES! AGORA O VENOM ENFRENTARÁ O DRUIDA!")

    vida_druida = vida_druida - ataque_venom
    dano_venom2 = ataque_druida + envenenamento
    vida_venom = vida_venom - ataque_druida

    if vida_venom <= 0:
        print("O venom não tankou e foi de base...")

    if vida_druida <=0:
        print("O druida não tankou e foi de base...")

    if vida_venom <= 0:

        if vida_druida >= 0:
            venom_vence2 = 0
            desempate2 = 0
            print("Pelo visto a poção tava fora do prazo de validade :(")


    if vida_druida <=0:
        if vida_venom >= 0:
            venom_vence2 = 1
            desempate2 = 0
            print("Quase me dei mal, nunca mais aceito nada de estranho...")


    if vida_druida > 0 and vida_venom > 0:
        print(f"Vida atual do Venom: {vida_venom}")
        print(f"Dano sofrido pelo Venom: {dano_venom2}")
        print(f"Vida atual do druida: {vida_druida}")
        print(f"Dano sofrido pelo druida: {ataque_venom}")

    #comeca o desempateee

    if desempate2:

        if vida_venom <= 0 and vida_druida <= 0:
            venom_vence2 = 0
            print("Pelo visto a poção tava fora do prazo de validade :(")

        elif dano_venom2 > ataque_venom:
            venom_vence2 = 0
            print("Pelo visto a poção tava fora do prazo de validade :(")

        elif ataque_venom > dano_venom2:
            venom_vence2 = 1
            print("Quase me dei mal, nunca mais aceito nada de estranho...")

        elif vida_venom > vida_druida:
            venom_vence2 = 1
            print("Quase me dei mal, nunca mais aceito nada de estranho...")

        elif vida_druida > vida_venom:
            venom_vence2 = 0
            print("Pelo visto a poção tava fora do prazo de validade :(")

        else:
            venom_vence2 = 0
            print("Pelo visto a poção tava fora do prazo de validade :(")

if venom_vence1 == 1 and venom_vence2 == 1:
        print("Essa aventura foi epicamente épica, meu amigo! Boa viagem aí! * Começa a tocar saxofone *")

if venom_vence1 == 0 or venom_vence2 == 0:
        print("Pelo visto as aventuras do Miles terminaram por aqui...")



