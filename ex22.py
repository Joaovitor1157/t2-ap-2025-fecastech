#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais 
#número ele é divisível.

y = int(input("Digite um numero inteiro positivo: ")) 

x = [2] # ista para os numeros primos

p = True
e = int(y/2) + 1  #limitador

for i in range(2 , e):
    if y % i == 0:
        print("%i não é primo, pois é divisivel por %i" %(y , i))
        p = False
if p:
    print(y , "é primo")