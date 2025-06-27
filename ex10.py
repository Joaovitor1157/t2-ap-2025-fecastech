#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo 
#compreendido por eles. 

x = input("Digite dois numeros inteiro separados por espaço: "). split()
s = 0

for i in range(len(x)):
    x[i] = int(x[i])

if x[0] + 1 == x[1] or x[0] - 1 == x[1]:
    print("Não há numeros iteiro entre eles")

elif x[0] > x[1]:
    d = x[0] - x[1]
    v = []
    for i in range(x[1] , x[0]-1 ):
        s = i + 1
        v.append(s)
    print(v)

elif x[0] < x[1]:
    d = x[1] - x[0]
    v = []
    for i in range(x[0] , x[1]-1):
        s = i + 1
        v.append(s)
    print(v)
    
elif x[0] == x[1]:
    print("Eles são iguais")