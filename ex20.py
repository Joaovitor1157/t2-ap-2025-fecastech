#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando 
# o fatorial a números inteiros positivos e menores que 16. 
j = True
while j:
    x = int(input("Digite um numero inteiro menor que 16 para fatorar: "))
    if x <= 0 or x > 16:
        v = False
        print("Dados fora do padrão, tente novamente")
    else:
        v = True

    if v == True:
        c = [x]
        v = 0
        p = 1
        for i in range(x - 1):
            v = c[i] - 1
            c.append(v)
        for i in range(len(c)):
            p = p * c[i]
        print(p, "\n")
        w = input("Deseja fatorar novamente? (S/N) ")
        if w == "s" or w == "S" or w == "Sim" or w == "sim":
            j = True
        elif w == "n" or w == "N" or w == "Não" or w == "não" or w == "Nao" or w == "nao":
            j = False