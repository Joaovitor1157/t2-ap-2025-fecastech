#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a 
#quantidade de números ímpares.

x = input("Digite 10 numeros inteiros separado por espaço: ").split()
c = []
f = []
for i in range(len(x)):
    x[i] = int(x[i])

for i in range(len(x)):
    if x[i] % 2 == 0:
        a=str(x[i])
        c.append(a)
    else:
        a=str(x[i])
        f.append(a)
        
print( "São %i impar, sendo eles:" %len(f) , ", ".join(f))
print( "São %i par, sendo eles:" %len(c) , ", ".join(c))