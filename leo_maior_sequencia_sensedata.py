"""
    # Teste tenico - SenseData - DevSr python #
    # 28/12/2020 #

Maior soma contínua
Crie um programa para encontrar a sub-sequência contínua dentro do array A que possua maior soma:

Ex:
     Input: [-1, 5, 2, 1, 4, -7, 8, -3, -4, 2]
    Output: 13

Neste exemplo, o subarray [5, 2, 1, 4, -7, 8] é a sequência contínua de maior soma contida dentro do array e a soma deste array é 13

Ex 2:
    Input: [6, -4, -2, 1, -3, 5, -1, 2, 1, 1, -5, 4]
    Output: 8

Neste exemplo, o subarray [5, -1, 2, 1, 1] é a sequência contínua de maior soma contida dentro do array e a soma destes número é 8.

Seu programa só precisa exibir o VALOR da maior soma, não é necessário exibir o array em questão.

RESP: https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

"""

print(50*'*'+' Sense Data Test '+50*'*')

def max_currency_total(input):

    total = sum(input)
    print('Soma total de todos os valores: ',total)
    maior_max = input[0]
    atual = input[0]

    for x in range(1,len(input)):
        atual = max(input[x], atual + input[x])
        maior_max = max(maior_max, atual)

    return maior_max

print('Total da sequencia de maior soma: ', max_currency_total([-1, 5, 2, 1, 4, -7, 8, -3, -4, 2]))
