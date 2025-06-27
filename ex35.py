#Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos 
#existentes entre 1 e um número inteiro informado pelo usuário. 

y = int(input("Digite um numero inteiro positivo: ")) 

t = 0
m = 0

x = [2] # ista para os numeros primos

for c in range(3 , y , 2):
    p = True
    e = int(c**0.5) + 1  #limitador

    for i in range(3 , e , 2):

        if c % i == 0:
            p = False
            break
    if p:
        x.append(c)
        print(x[m] , "é primo")
        m += 1
