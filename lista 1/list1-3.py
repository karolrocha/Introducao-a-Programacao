"""Problem Statement

Após finalizar um grande período de vilanias, o Venom está cansado de praticar maldades e só quer tirar um período de férias pacíficas. Venom Mas, por ser um vilão muito procurado, o Venom não pode apenas baixar sua guarda. Para poder tirar suas tão sonhadas férias, ele pediu ajuda aos alunos do curso de Ciência da Computação da UFPE para saber se ele tem chances de sofrer um ataque surpresa de algum herói. Como ninguém teve coragem de recusar o pedido de um vilão tão temido, sua tarefa é ajudar o Venom a descobrir um bom local para descansar e se existe a chance de algum herói interromper sua diversão. Spider

Caso ele possa tirar férias, o Venom pedirá dicas de locais para aproveitar ao máximo seu período de diversão. Caso contrário, ele pedirá informações sobre qual herói poderá realizar um ataque.

Input

A entrada inicial consiste na chance de ocorrer um ataque surpresa no período de férias do Venom. Esse número vai de 0 a 100.

    chance

Em seguida, novas entradas serão analisadas baseadas na chance de ataque:

Caso a chance seja menor ou igual a 50, o input será um local recomendado para o Venom passar as férias.

    local_recomendado

Você poderá recomendar um dos seguintes locais para o Venom:

    Maceió

    Pipa

    Caruaru

    Bonito

Mas, o Venom não recusará sua opinião se for um local diferente desses!

Caso a chance seja maior que 50, o input será o nome do herói que está planejado um ataque.

    nome_do_heroi

Os computadores da UFPE possuem dados sobre os seguintes heróis:

    Homem-Aranha

    Capitão América

    Spider Gwen

    Hulk

OBS: AS ENTRADAS SEMPRE SERÃO AMIGÁVEIS!

Output

Após informar a chance de ataque, existem apenas dois casos possíveis:

Caso a chance seja menor ou igual a 50, imprima:

    "Ufa, finalmente posso tirar minhas férias!"

Após informar o local das férias, existem apenas essas saídas:

Se o local for "Maceió":

    "Bem que eu tava com saudade de uma boa praia!"

Se o local for "Pipa":

    "As noites em Pipa parecem muito animadas, to dentro!"

Se o local for "Caruaru":

    "Parece um local muito divertido para aproveitar as festas juninas!"

Se o local for "Bonito":

    "Praticar rapel nas cachoeiras vai ser demais!"

Caso seja um local diferente:

    ”Nunca ouvi falar sobre {local_recomendado}, mas me parece uma boa ideia!”

Caso a chance seja maior que 50, imprima:

    "Esses heróis nunca desistem, lá vou eu enfrentar mais um!"

Após informar o nome do herói, existem apenas essas saídas:

Se o herói for "Homem-Aranha":

    "O amigo da vizinhança nunca me deixa em paz! Será derrotado!"

Se o herói for "Capitão América":

    "Derrotar o carinha do escudo vai ser moleza!"

Se o herói for "Spider Gwen":

    "A namoradinha do spidey nunca será capaz de me derrotar!"

Se o herói for "Hulk":

    "Esse aí só sabe gritar e quebrar tudo, não será páreo para mim!"

Se o herói não estiver na lista de heróis conhecidos pelos computadores da UFPE:

    "Não conheço esse herói {nome_do_heroi}. Preciso me preparar para essa batalha!"""


chance = int(input())
cidade_ou_heroi = input()

if chance <=50:
    print("Ufa, finalmente posso tirar minhas férias!")

    if cidade_ou_heroi == "Maceió":
        print("Bem que eu tava com saudade de uma boa praia!")

    elif cidade_ou_heroi == "Pipa":
        print("As noites em Pipa parecem muito animadas, to dentro!")

    elif cidade_ou_heroi == "Caruaru":
        print("Parece um local muito divertido para aproveitar as festas juninas!")

    elif cidade_ou_heroi == "Bonito":
        print("Praticar rapel nas cachoeiras vai ser demais!")

    else:
        print(f"Nunca ouvi falar sobre {cidade_ou_heroi}, mas me parece uma boa ideia!")

else:
    print("Esses heróis nunca desistem, lá vou eu enfrentar mais um!")

    if cidade_ou_heroi == "Homem-Aranha":
        print("O amigo da vizinhança nunca me deixa em paz! Será derrotado!")

    elif cidade_ou_heroi == "Capitão América":
        print("Derrotar o carinha do escudo vai ser moleza!")
    elif cidade_ou_heroi == "Spider Gwen":
        print("A namoradinha do spidey nunca será capaz de me derrotar!")
    elif cidade_ou_heroi == "Hulk":
        print("Esse aí só sabe gritar e quebrar tudo, não será páreo para mim!")
    else:
        print(f"Não conheço esse herói {cidade_ou_heroi}. Preciso me preparar para essa batalha!")