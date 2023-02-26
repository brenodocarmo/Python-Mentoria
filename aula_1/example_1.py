"""
O nome dos patinhos são: Jack, Kack, Lack, Mack, Nack, Ouack, Pack e Quack. 
Vamos escrever um programa (com Test Case) em que a função receba os prefixos 
'JKLMNOPQ' e adicione o sufixo correto

Se observar as palavras terminam sempre com ack. Além disso, tem duas palavras
que tem a vogal u antes do sufixo ack, são elas Ouack e Quack
"""

def prefix_and_suffix():
    """
    Essa função retorna o prefixo mais
    sufixo correto
    """

    prefix = "JKLMNOPQ"
    suffix = "ack"
    l = []
    for letter in prefix:
        if letter == "O" or letter == "Q":
            l.append(letter + "uack")
            continue
        l.append(letter + suffix) 
    return l

p = prefix_and_suffix()

# Lista original
names =["Jack", "Kack", "Lack", "Mack", "Nack", "Ouack", "Pack", "Quack"]

print(p)
