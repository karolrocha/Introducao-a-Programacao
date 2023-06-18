"""Problem Statement

Stan Lee de boa

Devido a um bug na matrix, um dos portais do multiverso acabou levando Miles, Gwen e Peter para dentro do MCU (Universo Cinematográfico da Marvel)!!! Nossos heróis não sabem como voltar para seus universos originais e parece que a única esperança é encontrar o criador: Stan Lee. Sendo ele um dos inventores do Homem-Aranha original, talvez essa seja a chave para entender melhor o que está acontecendo. No caminho, eles se encontram com o Miguel O'Hara (o Homem Aranha 2099) que os dá uma dica, porém ela veio codificada... Para conseguir achar o Stan, os miranhas então pediram a ajuda das mentes mais brilhantes no multiverso: os calouros do CIn; para que façam um programa para ajudá-los. Cabe a vocês agora auxiliarem o grupo a voltar para casa enquanto eles viajam pelos filmes da Marvel!

Input

Stan Lee de boa

Primeiramente vocês vão receber a dica, que nada mais é do que um inteiro que, quando decodificado, representa o número de caracteres do nome do filme em que o Stan Lee está (contando com possíveis espaços e sinais)! Contudo, para descobri-la a mensagem precisará ser decodificada através da seguinte fórmula:

Se o número for par

    (a raiz quadrada de metade da dica) + 2

Se o número for ímpar

    (um terço da dica) + 3

Pesquisar sobre a função “len( )”

Após a primeira entrada, os ciners vão receber o nome dos 3 filmes em que os pessoas-aranha irão passar:

    filme_1

    filme_2

    filme_3

A cada filme que eles tiverem que passar o nível de cansaço aumenta em um ponto (Ex. Se for o segundo filme o certo o nível de cansaço será 2 e se fosse o primeiro o nível seria 1) mas se o filme for “Vingadores: Ultimato” o cansaço aumenta em 2 em vez de apenas 1, pelas 3h de duração.

Por fim, caso os heróis encontrem o Stan, ele irá dizer como escapar: um filme do teioso! Porém, para conseguir, Miles e o grupo terão que ficar acordados durante toda a história. Para saber se conseguirão, você receberá o nome do filme e sua duração (em minutos), em linhas separadas.

    nome_do_filme

    duracao

Atenção: Essa última entrada só irá existir caso os heróis encontrem o Stan

Output

Incialmente, vocês terão que checar se eles realmente estão no universo certo. Se o primeiro filme for da DC (Coringa, Batman vs Superman ou O Cavaleiro das Trevas) você deve imprimir na tela <"Algo de errado não está certo!"> e encerrar o programa. Caso contrário você vai checar se o filme bate com a dica do Miguel; se ele não bater, os pessoas-aranha vão ter mais duas chances de tentar achar o filme correto, para que eles não fiquem presos no multiverso. Enquanto os aranhas estão na busca, você deve retornar as seguintes mensagens...

Caso o primeiro filme não tenha o Stan Lee a saída será:

    "Miles: Tou frio, melhor ir procurar nas fases mais antigas"

Se o segundo filme também não tiver:

    "Gwen: Cadê o velho??? Queria um autógrafo"

E caso não ache em nenhuma das chances:

    "Peter: Parece que o próximo filme do aranha-verso vai demorar mais do que esperado pra sair..."

Caso o filme seja o procurado, a saída vai ser:

    "Miles: Achei o easter egg!!!"

Por fim, caso tenham encontrado o Stan Lee, para saber se conseguirão, o CIn deverá analisar a situação da equipe e o tamanho do filme.

Caso o cansaço seja maior ou igual a 2 e a duração seja maior ou igual a 135, eles acabam dormindo no meio da história do filme. Assim, você deverá imprimir:

    "Miles: A mimir".

Se o cansaço for maior ou igual a 2 e a duração for maior ou igual a 120 e menor que 135 eles conseguem na luta, você deverá imprimir:

    "Gwen: Nada que uma xícara de café não resolva!".

Caso a duração seja menor que 120 ou o nível de cansaço seja menor que 2, os heróis conseguem tranquilamente. Assim, imprima:

    "Peter: {nome_filme} é o melhor filme do homem aranha, 10/10"."""



numero = int(input())

if (numero%2) == 0:
    numero = ((numero/2)**0.5) + 2

else:
    numero = (numero/3) + 3

filme1 = input()
filme2 = input()
filme3 = input()

cansaco = 1
encontrou_o_stan = 0

filmes_dc = ["Coringa", "Batman vs Superman", "O Cavaleiro das Trevas"]

if filme1 in filmes_dc:
    print("Algo de errado não está certo!")

else:
    if len(filme1) == numero:
        encontrou_o_stan = 1
        print("Miles: Achei o easter egg!!!")
    else: 
        print("Miles: Tou frio, melhor ir procurar nas fases mais antigas")
        cansaco = cansaco + 1
    
        if len(filme2) == numero:
            encontrou_o_stan = 1
            print("Miles: Achei o easter egg!!!")

        else:
            print("Gwen: Cadê o velho??? Queria um autógrafo")
            cansaco = cansaco + 1

            if len(filme3) == numero:
                encontrou_o_stan = 1
                print("Miles: Achei o easter egg!!!")
                
            else:
                print("Peter: Parece que o próximo filme do aranha-verso vai demorar mais do que esperado pra sair...")
                cansaco = cansaco + 1

if filme1 == "Vingadores: Ultimato" or filme2 == "Vingadores: Ultimato" or filme3 == "Vingadores: Ultimato":
    cansaco = cansaco+1


if encontrou_o_stan == 1:
    nome_do_filme = input()
    duracao = int(input())


if encontrou_o_stan:
    if cansaco >= 2 and duracao >=135:
        print("Miles: A mimir")
    elif cansaco >=2 and duracao >= 120 and duracao <=135:
        print("Gwen: Nada que uma xícara de café não resolva!")
    elif cansaco < 2 or duracao < 120:
        print(f"Peter: {nome_do_filme} é o melhor filme do homem aranha, 10/10")