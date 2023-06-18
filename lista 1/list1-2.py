"""Problem Statement

Mais um dia usual na Terra 4010, e Peter Parker ainda não está muito nessa vibe de pular entre um Universo e outro. Mas, como você sabe, ele tem que se virar nos 30 para ser um adolescente estudioso e o super-herói mais requisitado da cidade de Nova Iorque. Porém, até “O Espetacular Homem-Aranha” precisa de uma ajudinha. Você, da Terra que tem o Homem-Aranha da Carreta Furacão, através da confusão de abrir e fechar portais do multiverso, acabou conseguindo ouvir o rádio da central de ocorrência da polícia nova-iorquina da Terra 4010. Portanto, você consegue saber se é necessário que o Spider trabalhe. Além disso, você consegue avisá-lo por meio de um software inter-universal do R5 criado no CIn por Silvio Melo! Assim, você deve ajudar Peter Parker a saber se há ou não alguma confusão que só o Homem-Aranha é capaz de resolver.

Agora, cuidado com as interferências multiversais, pois caso as ocorrências aconteçam em lugares de outros universos, não precisa nem avisar ao Homem-Aranha.

Input

Primeiramente você receberá a entrada do local da ocorrência:

    local

Após isso receberá a ocorrência que o Homem-Aranha deve intervir:

    ocorrencia

As ocorrências SEMPRE serão alguma dessas três:

    "um carrinho de bebê prestes a se chocar numa árvore"

    "perseguição policial contra assaltantes de banco por aqui"

    "esse caminhão desgovernado não está conseguindo frear"

Obs: As ocorrências exigidas serão estritamente essas, então não se preocupem em contemplar outros casos diferentes disso.

Output

Caso o local se encaixe em um desses 3: Queens, Times square e Central Park, a saída será a seguinte:

    "Parece que hoje teremos que dar umas teiada por aí... simboora!"

Se não, a saída será a seguinte:

    "Tudo maravilindo! mas tenho que estudar para prova de Inglês e História ainda boy..."

Caso o local seja um dos 3 citados anteriormente, as saídas serão:

    Se for no Queens:

    "Eita... [ocorrencia], e logo aqui perto da tia May viiu?!"

    Se for na Times square:

    "Movimentação intensa de cria aqui pra variar, mas tem [ocorrencia], não posso deixar isso acontecer!"

    Se for no Central Park:

    "Nossa... [ocorrencia], depois de salvar vou pegar um hot dog meermo."

Atenção: Os nomes dos locais devem estar escritos da forma exata que estão dispostos acima, incluindo caracteres maiúsculos e minúsculos. Recomendamos que você copie do próprio texto."""

local = input()
ocorrencia = input()

if local == "Queens":
    print("Parece que hoje teremos que dar umas teiada por aí... simboora!")
    print(f"Eita... {ocorrencia}, e logo aqui perto da tia May viiu?!")

elif local == "Times square" :
    print("Parece que hoje teremos que dar umas teiada por aí... simboora!")
    print(f"Movimentação intensa de cria aqui pra variar, mas tem {ocorrencia}, não posso deixar isso acontecer!")

elif local == "Central Park":
    print("Parece que hoje teremos que dar umas teiada por aí... simboora!")
    print(f"Nossa... {ocorrencia}, depois de salvar vou pegar um hot dog meermo.")

else:
    print("Tudo maravilindo! mas tenho que estudar para prova de Inglês e História ainda boy...")

