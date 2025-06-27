#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao 
#segundo número. Não utilize a função de potência da linguagem. 

import math
x = int(input("Digite o valor da base: "))
y = int(input("Digite o valor do expoenete: "))
e = 1

for i in range(y):
    e = x * e

print(e) 