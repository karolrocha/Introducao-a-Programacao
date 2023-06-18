"""Problem Statement

Depois de algumas mudanças na gestão da companhia de entretenimento Marvel, até mesmo o homem-aranha da Carreta Furacão foi permitido a fazer parte do Aranhaverso. No entanto, antes de ser oficialmente recebido no grupo, é necessário que ele realize um teste, a fim de avaliar se realmente possui as competências necessárias.

cover

Com o intuito de criar um teste de alto nível, a famosa companhia de cinema procurou os alunos de P1 e de IP do CIn. Nesse sentido, você será responsável por desenvolver um código que aprove - ou não - a entrada do “miranha furacão” no Aranhaverso.

Para que seja integrante do aranhaverso, o homem-aranha deve seguir os seguintes critérios:

    Ter como características Humildade e Bondade (Nesta ordem!);
    Ser apaixonado por Mary Jane ou não ser apaixonado por ninguém;
    Saber fazer as dancinhas da Carreta Furacão ou conseguir lançar teias de aranha;
    Ter tido um bom desempenho na sua vida escolar, o que será medido de acordo com a média de três notas dele (se média ≥ 7, ele teve um bom desempenho e foi responsável).

ATENÇÃO: Estruturas condicionais devem, obrigatoriamente, ser utilizadas nesta questão; É recomendado o uso de operadores; Não esqueça de passar strings para números, quando necessário!

Input

As entradas serão as seguintes:

    Características:

    Caracteristica1

    Caracteristica2

    Pessoa pela qual é apaixonado (caso não seja apaixonado por ninguém, a entrada será “Ninguem”, já caso seja apaixonado por Mary Jane, a entrada será “Mary”):

    Nome

    Habilidade (caso saiba dançar, a entrada será “Dancar”, já caso saiba lançar teia, a entrada será “Lancar”):

    Habilidade

    Notas (do tipo INTEIRO):

    Nota1

    Nota2

    Nota3

Os critérios devem ser checados seguindo a ordem por meio da qual foram expostos no enunciado. Assim que um dos critérios deixar de ser seguido, o homem-aranha deve ser reprovado independente dos critérios seguintes, mas você ainda recebe todos os inputs.

Output

As saídas poderão ser as seguintes:

    Caso o homem-aranha passe no teste:

    Siga em frente, olhe para o lado. Bem-vindo ao aranhaverso, Miranha Furacao!

    Caso não passe no teste, você deve imprimir a mensagem de que ele não passou e a justificativa:

    Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!

    Caso a justificativa esteja relacionada às características:

    Infelizmente você não possui as característica necessárias!

    Caso a justificativa esteja relacionada à paixão:

    Infelizmente você não está apaixonado pela pessoa certa!

    Caso a justificativa esteja relacionada às habilidades:

    Infelizmente você não possui as habilidades necessárias!

    Caso a justificativa esteja relacionada ao desempenho escolar:

    Infelizmente você não obteve um bom desempenho escolar!"""

caracteristica1 = input()
caracteristica2 = input()

apaixonado = input()

habilidade = input()

nota1 = int(input())
nota2 = int(input())
nota3 = int(input())

media = (nota1+nota2+nota3)/3

nao_pode_entrar = 0

if caracteristica1 == "Humildade" and caracteristica2 == "Bondade":
    feedback1 = False
else:
    feedback1 = "Infelizmente você não possui as característica necessárias!"
    nao_pode_entrar = 1

if apaixonado == "Mary" or apaixonado == "Ninguem":
    feedback2 = False
else:
    feedback2 = "Infelizmente você não está apaixonado pela pessoa certa!"
    nao_pode_entrar = 1


if habilidade == "Dancar" or habilidade == "Lancar":
    feedback3 = False
else:
    feedback3 = "Infelizmente você não possui as habilidades necessárias!"
    nao_pode_entrar = 1

if media>=7:
    feedback4 = False
else:
    feedback4 = "Infelizmente você não obteve um bom desempenho escolar!"
    nao_pode_entrar = 1

if nao_pode_entrar == 1:
    print("Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!")

    if feedback1:
        print(f"{feedback1}")
    if feedback2:
        print(f"{feedback2}")
    if feedback3:
        print(f"{feedback3}")
    if feedback4:
        print(f"{feedback4}")

else:
    print("Siga em frente, olhe para o lado. Bem-vindo ao aranhaverso, Miranha Furacao!")

