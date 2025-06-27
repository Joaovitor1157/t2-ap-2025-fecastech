#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
#Valide a entrada e permita repetir a operação. 

ano = 0
f = True
while f:
    while f:
        a = float(input("Digite a população do cidade A onde a população de A seja menor do que a de B: ").replace("," , "."))
        b = float(input("Digite a população do cidade B onde a população de B seja maior do que a de A: ").replace("," , "."))
        ta = float(input("Digite a taxa de crecimento da cidade A onde a taxa de A seja maior do que a de B: ").replace("," , "."))
        tb = float(input("Digite a taxa de crecimento da cidade B onde a taxa de B seja menor do que a de A: ").replace("," , "."))
        if a < b and ta >= tb:
            while a <= b:
                ano += 1
                a = a + (a * (ta/100))
                b = b + (b * (tb/100))
            print("Vai demorar %i anos" %(ano))
            f = False
        elif a == b:
            print("As populaçoes já são as mesmas")
            f = False
        else:
            print("Dados fora do padrão tente novamente")

    v = input("Deseja fazer o teste de novo? (S/N)")
    if v == "s" or v == "S" or v == "Sim" or v == "sim":
        f = True
    elif v == "n" or v == "N" or v == "Não" or v == "não" or v == "Nao" or v == "nao":
        f = False