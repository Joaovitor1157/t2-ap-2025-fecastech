#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma 
#dos valores. 

x = input("Digite uma sequencia de numeros separados por virgula: "). split(",")
b = r = 0

for i in range(len(x)):
    x[i] = float(x[i])

for c in range(len(x)):
    for i in range(len(x)):
        m = x[c] >= x[i]
        if m == True:
            b += 1

    if b == len(x):
        print(x[c] , 'é o maior')
        b = 0
    elif b == 1:
        print(x[c] , 'é o menor')
        b = 0
    else:
        b = 0

    r = r + x[c]
    
print(r , "É a soma dos valores")