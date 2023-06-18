"""Problem Statement

Depois de muito sofrer pulando de um universo para o outro, Miles finalmente chega em um dos seus destinos finais, que é conseguir o seu novo traje aranha, com novas funcionalidades, novas tecnologias, tudo diferente. ganke Ao chegar no sótão para pegar o traje, Miles notou que o criador da roupa, como medida de segurança, só liberaria a vestimenta se um teste fosse realizado e aprovado pelo sistema. O menino aranha percebeu que o teste envolvia, além de informações sobre as novas funcionalidades do traje, programação e estruturas condicionais, logo, pensou em você para resolver tal teste. miles O teste funciona levando em consideração as funcionalidades novas desse novo traje e o quanto elas usam de energia. Temos um novo lançador de teias, lentes de visão avançada, uma funcionalidade que torna o traje à prova de balas, ativação de inteligência artificial e membranas planadoras.

A todo tempo, a energia do traje é renovada, porém dependendo da combinação de funcionalidades que são feitas, o tempo de renovação não é páreo para a intensidade de energia gasta. O teste consiste em fazer um programa que será usado no próprio traje, em que será mostrado ao Miles mensagens de alerta dependendo das combinações das funcionalidades que estão sendo realizadas.

Input

A entrada será composta por uma série intercalada de strings e inteiros que são as funcionalidades que o Miles está usando no momento e seu respectivo custo de energia. O traje o permite usar no máximo 5 funcionalidades ao mesmo tempo, logo você terá o par de entrada funcionalidade e funcionalidade_ponto, como o exemplo abaixo, repetido 5 vezes.

    funcionalidade - string

    funcionalidade_ponto - inteiro

Você também poderá receber a string ‘NADA’ que significa que o menino aranha decidiu não usar alguma das entradas de ativação que sua vestimenta possui, então precisa preencher com essa string para seguir com o programa e quanto ao valor, é preenchido com 0.

Output

    Se o Miles usar o novo lançador de teias como primeira funcionalidade e usar qualquer funcionalidade em seguida, imprima:

    “Com calma, aranha”

    Se ele usar o lançador de teias na primeira funcionalidade e logo em seguida usar a lentes de visão avançada, imprima:

    “Lembre de desativar as lentes depois, e cuidado ao usar as teias no escuro”

    Se ele usar o lançador de teias na primeira funcionalidade, as lentes na segunda e o traje à prova de balas como terceira, imprima:

    “UOU, só tente sair dessa vivo, vou otimizar a energia aqui”

    Se o Miles usar a ativação de inteligência artificial a qualquer momento, imprima:

    “Espero que não esteja ativando isso para usar nas provas”

    Se a soma das funcionalidades for igual ou maior a 80:

    “Vou descarregar em questão de minutos, pare AGORA”

    Se Miles usar membranas planadoras, novo lançador de teias e ativação de inteligência artificial juntos em qualquer ordem ou posição, imprima:

    “Tudo certo, mas cuidado ao ficar conversando com IA enquanto voa”

    No final de tudo, imprima quantos pontos de energia foram gastos ao total:

    “Aranha, nessa sequência você usou {soma_funcionalidade} de energia!”

Obs.1: As entradas em string (novo lançador de teias, lentes de visão avançada, traje à prova de balas, etc) vão ser escritas exatamente como está na listagem na descrição da questão.

Obs.2: Algo muito importante é quanto a ordem da saída das mensagens escritas, elas devem estar na ordem que estão dispostas acima. Ou seja, se tiver o caso de ter duas mensagens a serem impressas, a ordem deve ser a do enunciado. Por exemplo, se tiver um caso que na saída irá ter: “‘Com calma, aranha” e “Vou descarregar em questão de minutos, pare AGORA”, deverá vir primeiro “‘Com calma, aranha”, porque no enunciado essa instrução vem primeiro.

Boa sorte! Lembre-se, o Miles depende de você!!!"""

funcionalidade1 = input()
pontos1 = int(input())

funcionalidade2 = input()
pontos2 = int(input())

funcionalidade3 = input()
pontos3 = int(input())

funcionalidade4 = input()
pontos4 = int(input())

funcionalidade5 = input()
pontos5 = int(input())

funcionalidades = [funcionalidade1, funcionalidade2, funcionalidade3, funcionalidade4, funcionalidade5]
pontos_totais = pontos1 + pontos2 + pontos3 + pontos4 + pontos5


if funcionalidade1 == "novo lançador de teias" and funcionalidade2 != "NADA":
    print("Com calma, aranha")

    if funcionalidade1 == "novo lançador de teias" and funcionalidade2 == "lentes de visão avançada":
        print("Lembre de desativar as lentes depois, e cuidado ao usar as teias no escuro")

        if funcionalidade3 == "traje à prova de balas":
            print("UOU, só tente sair dessa vivo, vou otimizar a energia aqui")

if "ativação de inteligência artificial" in funcionalidades:
    print("Espero que não esteja ativando isso para usar nas provas")

if pontos_totais >=80:
    print("Vou descarregar em questão de minutos, pare AGORA")

if "membranas planadoras" in funcionalidades and "ativação de inteligência artificial" in funcionalidades and "novo lançador de teias" in funcionalidades:
    print("Tudo certo, mas cuidado ao ficar conversando com IA enquanto voa")

print(f"Aranha, nessa sequência você usou {pontos_totais} de energia!")