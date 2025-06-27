# Faça um programa que leia e valide as seguintes informações: 
# a) Nome: maior que 3 caracteres; 
# b) Idade: entre 0 e 150; 
# c) Salário: maior que zero; 
# d) Sexo: 'f' ou 'm'; 
# e) Estado Civil: 's', 'c', 'v', 'd'; 
# Use a função len(string) para saber o tamanho de um texto (número de caracteres). 

e = ['Solteiro(a)' , "Casado(a)" , "Viuvo(a)" , "Divorciado(a)"]
c = ["S" , "C" , "V" , "D"]
y = 0
while True:
    n = input("Digite um nome (Com mais de 3 letras): ")
    if len(n) < 3:
        print("Nome com menos de 3 letras, por favor digite outro nome")
        n = input("Digite um nome: ")
    else: 
        print("Tudo certo pode prossegir")
        break
while True:
    i = int(input("Digite uma idade entre 0 e 150 anos: "))
    if i > 0 and i < 150:
        print("Tudo certo pode prosseguir")
        break
    else:
        print("Idade fora do parametro, por favor digite outra idade")

while True:
    s = float(input("Digite seu salário: "))
    if s > 0 :
        print("Você tem um salario, parabens!!")
        break
    else:
        print("salario invalido")
while True:
    sx = input("Digite seu sexo(F/M): ")
    if sx == "F" or sx == "f":
        print("Então você é uma Mulher")
        break
    elif sx == "M" or sx == "m":
        print("Então você é um homem")
        break
    else:
        print("Dado invalido, por favor tente novamente")
while True:
    ec = input("Digite seu estado civil(S/ C/ V/ D): ")
    for i in range(4):
        if ec == c[i]:
            print("Então você é" , e[i])
            break
        else:
            y += 1
    if y == 4:
        print("Dado invalido, por favor tente novamente")
        y = 0
    else:
        break