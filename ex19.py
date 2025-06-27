#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

while True:
    x = input("Digite uma sequencia de numeros, entre 0 e 1000, separados por virgula: "). split(",")
    b = r = f = 0
    for i in range(len(x)):
        x[i] = float(x[i])
        if x[i] > 1000 or x[i] < 0:
            f = f + 1
    if f == 0:
        t = True
    else:
        t = False

    if t == True:

        for c in range(len(x)):
            for i in range(len(x)):
                m = x[c] >= x[i]
                if m == True:
                    b += 1

            if b == len(x):
                print(x[c] , 'é o maior')
                b = 0
                w = x[c]
            elif b == 1:
                print(x[c] , 'é o menor')
                y = x[c]
                b = 0
            else:
                b = 0

            r = r + x[c]
            
        print(r , "É a soma dos valores")
        break
    else:
        print("Dados fora do paramerto, por favor tente novamente")