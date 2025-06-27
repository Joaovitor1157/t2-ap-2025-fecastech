#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120 

x = int(input("Digite o numero q deseja fatorar: "))
c = [x]
v = 0
p = 1
for i in range(x - 1):
    v = c[i] - 1
    c.append(v)
for i in range(len(c)):
    p = p * c[i]
print(p)