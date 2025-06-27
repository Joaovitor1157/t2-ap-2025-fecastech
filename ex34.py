# Os números primos possuem várias aplicações dentro da Computação, por exemplo na criptografia. Um
#número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um 
#número inteiro e determine se ele é ou não um número primo. 


y = int(input("Digite um numero inteiro positivo: ")) 

x = [2] # ista para os numeros primos

p = True
e = int(y**0.5) + 1  #limitador

for i in range(2 , e):
    if y % i == 0:
        print("%i não é primo" %y)
        p = False
        break
if p:
    print("%i é primo" %y)
