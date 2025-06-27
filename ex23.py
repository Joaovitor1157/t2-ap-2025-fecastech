#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
#O programa deverá mostrar também o número de divisões que ele executou para encontrar os números 
#primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

import time

y = int(input("Digite um numero inteiro positivo: ")) 

inicio = time.time() #Inicia o cronometro
t = 0
primo = [2] # ista para os numeros primos

for c in range(3 , y , 2):
    p = True
    e = int(c**0.5) + 1  #limitador

    for i in range(3 , e , 2):
        t += 1
        if c % i == 0:
            p = False
            break
    if p:
        primo.append(c)
      

fim = time.time()
l = fim - inicio

if l >= 60:
    l = "%.2f  minutos" %(l/60)
else:
    l = "%.2f segundos" %l
    
print("Total de numeros: " , y)
print("Total de numeros primos: " , len(primo))
print("Total de numeros não primos: " , y - len (primo))
print("Tempo de execução:" , l)
print("Numero de teste feitos:" , t)
