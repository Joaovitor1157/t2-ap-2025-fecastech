#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. 
#A saída deve ser conforme o exemplo abaixo:
#Fatorial de: 5 
#5! =  5 . 4 . 3 . 2 . 1 = 120

x = int(input("Digite o numero q deseja fatorar: "))
c = [x]
v = 0
p = 1
for i in range(x - 1):
    v = c[i] - 1
    c.append(v)
for i in range(len(c)):
    p = p * c[i]

for i in range(len(c)):
    c[i] = str(c[i])
for i in range(1 , len(c)):
    c[i] += " " + c[i-1]
y = c[-1].split(" ")
for i in range(len(y)-1):
    y[i] = ". " + y[i]
for i in range(1 , len(c)):
    y[i] += " " + y[i-1]

print("%i!" %x, "=" , y[-1] , "=" , p)