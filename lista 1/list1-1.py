"""Problem Statement

Reunidos todos em São Francisco, a família Aranha agora se prepara pra serem lançados em suas missões pelo Dikastisverso que os levarão a diferentes locais no Globo, e precisam da ajuda de um estudante do CIn para programar a máquina dos portais que os levarão!

Dikastisverso

Seu trabalho vai ser ajustar o destino da Máquina de acordo com duas variáveis: O nome do Aranha em questão e a frequência em que está a Máquina.

Input

Você sempre vai receber 2 inputs para cada caso, o nome do Aranha que vai ser enviado e a frequência em que a Máquina vai estar:

    nome_aranha

    frequencia_maquina

Output

    Se o Aranha em questão for o “Miles Morales” e a frequência da máquina for maior ou igual a 800 e menor que 2400, imprima o seguinte Output:

        “Miles será enviado para a praça do Harlem! O Rino e o Prowler estão causando problemas demais essa hora do dia!”

    Se o Aranha em questão for o “Miles Morales” e a frequência esteja abaixo de 800:

        “Miles está mais livre e pode passar pra visitar sua mãe Rio em seu apartamento!”

    Se o Aranha em questão for o “Miles Morales” e a frequência seja igual ou acima de 2400:

        “Essa frequência é desconhecida para o Miles! Com certeza vai achar encrenca!”

    Se o Aranha em questão for a “Spider-Gwen” e a frequência da máquina frequência da máquina for maior ou igual a 600 e menor que 3000, imprima o seguinte Output:

        “A Gwen deve ir dar um basta nas operações da Tinkerer, ajustaremos a Máquina para a Times Square!”

    Se o Aranha em questão seja a “Spider-Gwen” e a frequência esteja abaixo de 600:

        “A Gwen está liberada pra tomar Sorvete no Central Park, esse será seu Destino”

    Se o Aranha em questão seja a “Spider-Gwen” e a frequência seja igual ou acima de 3000:

        “Sabemos que a Gwen está mais habituada pra viajar entre Universos mas essa frequência é perigosa até para ela!!”

    Se o Aranha em questão for o “Miranha-Furacão” e a frequência da máquina estiver acima de 0, imprima o seguinte Output:

        “A Carreta Furacão sai desgovernada pra animar mais uma rua em Cabrobó!”

    Se o Aranha em questão for o “Miranha-Furacão” e a frequência seja 0 ou tenha um valor negativo:

        “Mas o que é isso?! Esse bregueço deve ta quebrado, Miranha-Furacão, Pica-Pau, Pikachu, Mickey e Cascão vão continuar treinando seu número em casa!”

    Se o Aranha em questão for o “Homem-Aranha do PS4” ou o “Homem-Funko-Pop”:

        “Maceió! Há rumores de um Vilão misterioso nas praias, alguns Aranhas devem ir pra lá!”

    Se o Aranha em questão for o “Porco-Aranha”:

        “O destino será a Fazendinha do Plaza!”

    Finalmente, caso o Aranha não esteja entre os citados nesses casos acima, imprima:

        “Quê?! Ou esse Aranha não existe ou não deve ser enviado em nenhuma missão pelo Dikastisverso!”

Se atente aos pontos e detalhes de cada Output na programação da Máquina! Você não quer mandar ninguém pro lugar errado e testar os extremos da máquina faz parte da questão! Se estiver em dúvida, use um Diff-Checker para procurar diferenças entre seu Output e os esperados e tenha certeza que seus intervalos de frequência estão precisos, cada detalhe importa!"""


nome_aranha = input()
frequencia_maquina = input()

frequencia_maquina = int(frequencia_maquina)

if nome_aranha == "Miles Morales":

    if frequencia_maquina >= 800 and frequencia_maquina < 2400:
        print("Miles será enviado para a praça do Harlem! O Rino e o Prowler estão causando problemas demais essa hora do dia!")

    elif frequencia_maquina < 800:
        print("Miles está mais livre e pode passar pra visitar sua mãe Rio em seu apartamento!")

    elif frequencia_maquina >= 2400:
        print("Essa frequência é desconhecida para o Miles! Com certeza vai achar encrenca!")

elif nome_aranha == "Spider-Gwen":
    if frequencia_maquina >= 600 and frequencia_maquina < 3000:
        print("A Gwen deve ir dar um basta nas operações da Tinkerer, ajustaremos a Máquina para a Times Square!")

    elif frequencia_maquina < 600:
        print("A Gwen está liberada pra tomar Sorvete no Central Park, esse será seu Destino")
    elif frequencia_maquina >= 3000:
        print("Sabemos que a Gwen está mais habituada pra viajar entre Universos mas essa frequência é perigosa até para ela!!")

elif nome_aranha == "Miranha-Furacão":
    if frequencia_maquina > 0:
        print("A Carreta Furacão sai desgovernada pra animar mais uma rua em Cabrobó!")
    elif frequencia_maquina <=0:
        print("Mas o que é isso?! Esse bregueço deve ta quebrado, Miranha-Furacão, Pica-Pau, Pikachu, Mickey e Cascão vão continuar treinando seu número em casa!")

elif nome_aranha == "Homem-Aranha do PS4" or nome_aranha == "Homem-Funko-Pop":
    print("Maceió! Há rumores de um Vilão misterioso nas praias, alguns Aranhas devem ir pra lá!")

elif nome_aranha == "Porco-Aranha":
    print("O destino será a Fazendinha do Plaza!")

else:
    print("Quê?! Ou esse Aranha não existe ou não deve ser enviado em nenhuma missão pelo Dikastisverso!")
