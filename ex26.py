#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada 
#eleitor votar e ao final mostrar o número de votos de cada candidato.

c1 = []
c2 = []
c3 = []
b = 0
x= int(input("Digite o numero de eleitores: "))

for i in range(x):
    p = int(input("Em qual candidato você vai votar? (1 / 2 / 3) "))
    if p == 1:
        c1.append(p)
    elif p == 2:
        c2.append(p)
    elif p == 3:
        c3.append(p)

x = [len(c1) , len(c2) , len(c3)]

for c in range(len(x)):
    for i in range(len(x)):
        m = x[c] >= x[i]
        if m == True:
            b += 1

    if b == len(x):
        print("O candidato %i, ganhou a eleição" %(c+1))
    else:
        b = 0