"""Problem Statement

miranhaxvenom Com a instabilidade dos portais do multiverso, o Homem Aranha foi enviado para Maceió para tentar encontrar o Venom e estragar de vez com suas férias. Como o bom “nerd da cadeira” que você é, você sugeriu desenvolver um código que indique os lugares mais badalados de Maceió que o Venom possa estar.

Só que existe um porém, você tem 3 chances para encontrar o Venom ou ele conseguirá fugir de vez.

Input

Inicialmente você receberá o local em que o Venom está se escondendo para curtir as férias.

    ex: “Praia”

Em seguida você receberá um possível local para procurá-lo.

    ex: “Piscinas naturais”

PS': se o local onde você procurou não for igual ao local onde o Venom está, você deverá receber outro local e refazer a verificação, mas lembre-se que são apenas 3 chances no total.

PS'': Não haverá diferença entre letras maiúsculas ou minúsculas. Logo, caso o input do esconderijo do Venom seja "PRAIA" e o input onde você deve procurar seja "praia", considere que você o encontrou.

Output

Caso o local de busca seja igual ao local do esconderijo, imprima:

    “Ahá, te encontrei e é o fim das suas férias!”

Caso contrário, você irá imprimir a seguinte mensagem:

    “Carambolas, ele não está aqui. Ele continua se divertindo!”

Caso você busque nos 3 lugares e não encontre nada, deverá imprimir a seguinte mensagem:

    “AAAAAAAH, ele escapou de vez!”"""

local = input().lower()

onde_procurar = input().lower()
if local == onde_procurar:
    print("Ahá, te encontrei e é o fim das suas férias!")

else:
    print("Carambolas, ele não está aqui. Ele continua se divertindo!")
    onde_procurar = input().lower()
    if local == onde_procurar:
        print("Ahá, te encontrei e é o fim das suas férias!")

    else:
        print("Carambolas, ele não está aqui. Ele continua se divertindo!")
        onde_procurar = input().lower()
        if local == onde_procurar:
            print("Ahá, te encontrei e é o fim das suas férias!")
        else:
            print("Carambolas, ele não está aqui. Ele continua se divertindo!")
            print("AAAAAAAH, ele escapou de vez!")