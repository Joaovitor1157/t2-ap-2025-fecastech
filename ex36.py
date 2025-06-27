# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, 
#mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser 
#informados também pelo usuário, conforme exemplo abaixo: 
 
#Obs: Você deve verificar se o usuário não digitou o final menor que o inicial
v=[]
x = int (input("Fazer a tabuado do numero: "))
y = int(input("Deseja começar por qual numero? "))
l = y -1
while True:
    z = int(input("Vamos terminar com um numero maior que %i: " %y))

    if y <= z:
        for i in range(y , z+1):
            l = l + 1
            v.append(l)
        print("A tabuada do", x ,"é: ")
        for i in range(len(v)):
            p = v[i] * x
            print(v[i], "X", x ,"=", p)
        break
    else:
        print("Numeros fora dopedido por favor digite outro numero")
