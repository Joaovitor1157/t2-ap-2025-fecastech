#Faça um programa que leia 5 números e informe o maior número. 

x = input("Digite uma sequencia de 5 numeros separados por espaço: "). split()
b = 0 

for i in range(len(x)):
    x[i] = float(x[i].replace("," , "."))

for c in range(len(x)):
    for i in range(len(x)):
        m = x[c] >= x[i]
        if m == True:
            b += 1

    if b == len(x):
        print(x[c] , 'é o maior')
    else:
        b = 0