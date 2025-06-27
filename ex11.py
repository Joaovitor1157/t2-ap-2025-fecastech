#Altere o programa anterior para mostrar no final a soma dos números. 

x = input("Digite dois numeris inteiro separados por espaço: "). split()
s , c = 0 , 0

for i in range(len(x)):
    x[i] = int(x[i])

if x[0] + 1 == x[1] or x[0] - 1 == x[1]:
    print("Não há numeros iteiro entre eles")
    print("A soma de todos os numeros é:" , x[1] + x[0])

elif x[0] > x[1]:
    d = x[0] - x[1]
    v = []
    for i in range(x[1] , x[0]-1 ):
        s = i + 1
        v.append(s)
    print(v)
    for u in range(len(v)):
        c = c + v[u]
    print("A soma de todos os numeros é:" , c + x[1] + x[0])

elif x[0] < x[1]:
    d = x[1] - x[0]
    v = []
    for i in range(x[0] , x[1]-1):
        s = i + 1
        v.append(s)
    print(v)
    for u in range(len(v)):
        c = c + v[u]
    print("A soma de todos os numeros é:" , c + x[1] + x[0])
    
elif x[0] == x[1]:
    print("Eles são iguais")
    print("A soma de todos os numeros é:" ,  x[1] + x[0])