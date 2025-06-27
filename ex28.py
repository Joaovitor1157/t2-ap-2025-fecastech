#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor 
#médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para cada um. 

x = int(input("Quantos CDs você tem? "))
h= []
p=0
for i in range(1 , x+1):
    y = float(input("Quanto você gastou no %i° CD? R$ " %i))
    h.append(y)

for i in range(len(h)):
    p += h[i]
p = p / len(h)

print("A média gastas nos CDs foi R$ %.2f" %p)