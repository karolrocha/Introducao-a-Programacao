"""Problem Statement

A abertura das inscrições do InterCIn está cada vez mais próxima, e com isso Caique e seus amigos estão tentando formar um grupo para participar do campeonato. São muitas categorias desde esportes a e-sports. Caique como grande fã de lolzinho estava com vontade de participar do campeonato, porém a quantidade de pessoas do time dele ainda não está definida, podendo ser uma número menor ou maior que a permitida no lolzinho.

Untitled

Depois que Caique montar seu time, ele terá que fazer sua inscrição no campeonato, informando quantas pessoas estarão no time dele. Isso para gerar o número da camisas dos integrantes. Esse números, por sua vez, são gerados seguindo a sequência de Fibonacci (tem que ter um toque nerd né). Então vai funcionar da seguinte forma:

time = 5 pessoas

camisas = 1 1 2 3 5

Sua função é fazer um algoritmo que gere esses números. Desse modo, o usuário vai digitar um número N de integrantes e você deverá retornar os números da camisas dos participantes.

Input

Você receberá um inteiro N, referente ao número de integrantes do time de Caique

    N

Output

Você deverá exibir a seguinte mensagem:

    “A sequência de número das camisas do seu time será: N1, N2, N3,…N”

Sendo N primeiros, os n primeiros termos da sequência de Fibonacci, contando 1 como o primeiro."""

numero_de_integrantes = int(input())
contador = 1
camisa_atual = 1
numero_anterior = 0

print("A sequência de número das camisas do seu time será: 1", end="")

while contador < numero_de_integrantes:
    camisa_a_printar = camisa_atual + numero_anterior
    
    if contador == numero_de_integrantes-1:
        print(f", {camisa_a_printar}")
    else:
        print(f", {camisa_a_printar}", end="")
    
    numero_anterior = camisa_atual
    camisa_atual = camisa_a_printar
    
    contador +=1
    
 