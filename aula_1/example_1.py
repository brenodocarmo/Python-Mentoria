"""
O nome dos patinhos são: Jack, Kack, Lack, Mack, Nack, Ouack, Pack e Quack. 
Vamos escrever um programa (com Test Case) em que a função receba os prefixos 
'JKLMNOPQ' e adicione o sufixo correto

Se observar as palavras terminam sempre com ack. Além disso, tem duas palavras
que tem a vogal u antes do sufixo ack, são elas Ouack e Quack
"""
__version__ = "0.0.1"
__author__ = "Breno do Carmo"
__license__ = "Unlicense"


def generate_duck_names(letters):

    suffix = "ack"

    name = []
    for letter in letters:
        if letter == "O" or letter == "Q":
            name.append(letter + "uack")
            continue
        name.append(letter + suffix) 
    return name


prefix = "JKLMNOPQ"
generate = generate_duck_names(letters=prefix)

print(generate)



