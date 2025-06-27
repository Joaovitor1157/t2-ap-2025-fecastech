# 42) Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão 
# nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for 
# lido um número negativo. 
inter1 = []
inter2 = []
inter3 = []
inter4 = []
fora = []
while True:
    num = int(input("Digite um número: "))
    if num >= 0:
        if num >=0 and num <=25:
            inter1.append(num)
        elif num >=26 and num <=50:
            inter2.append(num)
        elif num >=51 and num <=75:
            inter3.append(num)
        elif num >=76 and num <=100:
            inter4.append(num)
        else:
            fora.append(num)
    else:
        break

print("São %i numeros q pertence ao intervalo de o-25, sendo eles: " %(len(inter1)), inter1)
print("São %i numeros q pertence ao intervalo de 26-50, sendo eles: " %(len(inter2)), inter2)
print("São %i numeros q pertence ao intervalo de 51-75, sendo eles: " %(len(inter3)), inter3)
print("São %i numeros q pertence ao intervalo de 76-100, sendo eles: " %(len(inter4)), inter4)
print("São %i numeros q não pertence a nenhum intervalo, sendo eles: " %(len(fora)), fora)