"""Problem Statement

miranhaverso

O homem aranha após viajar bastante no aranhaverso, acabou indo longe demais e descobriu uma versão sua que apenas combate o tabagismo, o Miranha. Querendo ajudar o Miranha a fazer as pessoas pararem de fumar cigarro, Peter Parker decide desenvolver um programa para ver o círculo social das pessoas e quantos fumantes há, assim fazendo um calculo estatístico da probabilidade da pessoa ser afetada pelo seu círculo e começar a fumar, para assim o Miranha identificar possíveis futuros fumantes, e falando sua frase motivacional: “Fuma não pow, cuide da sua saúde”, para impedir que o tabagismo aumente.

fumanao

Input

A entrada inicial consiste no nome do indivíduo. Logo em seguida, quantas pessoas há em seu círculo social. E após isso, um coeficiente aleatório.

    Davi

    27

    0.9

Você deve verificar se o número total dado é par ou ímpar. Se for par, usar o coeficiente na fórmula:

    coeficiente * (total_pessoas - 1) + 1

Se for ímpar, usar o coeficiente na fórmula:

    coeficiente * (total_pessoas - 1) / 2

O resultado será o número de pessoas fumantes que o indivíduo tem em seu círculo. Você deve calcular a proporção de pessoas fumantes para a quantidade total de pessoas no círculo social. Se o resultado da fórmula for um float no qual o primeiro número depois da vírgula for >= 1 e menor e =< 5, ele deve ser arredondado para o menor inteiro mais próximo, e se for >5 e <=9, deve ser arredondado para o maior inteiro mais próximo. O número de pessoas fumantes deve sempre ser inteiro

OBS: a porcentagem da proporção deve sempre ser um inteiro. Não pode usar round() ou outras facilidades do python.

Output

Primeiro é necessário imprimir na tela a frase, no qual {indivíduo} deve ser o nome dado no input:

    Vamos verificar se {indivíduo} vai fumar singaro!

Após isso, é necessário imprimir qual a proporção calculada na frase:

    {proporção} dos seus amigos fumam singaro

E se a proporção for menor que 25%, a frase a ser imprimida é:

    Você tem poucas chances de fumar singaro, fuma não pow, cuide da sua saúde

Se a proporção for maior que 25% e menor que 50%, deve ser imprimido:

    Cuidado pra não fumar ein, fuma não pow, cuide da sua saúde

Se a proporção for maior que 50%, imprima:

    TIRA ESSE SINGARO DA BOCA. FUMA NÃO POW, CUIDE DA SUA SAÚDE!

*Miranhaverso quando abolir o singaro:"""

nome = input()
quantas_pessoas = int(input())
coeficiente = float(input())

if (quantas_pessoas%2) == 0:
    fumantes_conhecidos = coeficiente*(quantas_pessoas-1)+1
else:
    fumantes_conhecidos = coeficiente*(quantas_pessoas-1) + 1

def arredondar(numero):
    parte_decimal = numero - int(numero)
    decimal_arredondado = int(parte_decimal + 0.5)

    return int(numero) + decimal_arredondado

fumantes_conhecidos = arredondar(fumantes_conhecidos)
proporcao_fumantes_conhecidos = fumantes_conhecidos/quantas_pessoas*100


print(f"Vamos verificar se {nome} vai fumar singaro!")
print(f"{proporcao_fumantes_conhecidos:.0f}% dos seus amigos fumam singaro")

if proporcao_fumantes_conhecidos < 25:
    print("Você tem poucas chances de fumar singaro, fuma não pow, cuide da sua saúde")
elif proporcao_fumantes_conhecidos>25 and proporcao_fumantes_conhecidos <50:
    print("Cuidado pra não fumar ein, fuma não pow, cuide da sua saúde")
elif proporcao_fumantes_conhecidos > 50:
    print("TIRA ESSE SINGARO DA BOCA. FUMA NÃO POW, CUIDE DA SUA SAÚDE!")

