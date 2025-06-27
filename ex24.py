#Faça um programa que calcule e mostre a média aritmética de N notas. 

x = input("Digite as notas separadas por virgula: ").split(",")

for i in range(len(x)):
    x[i] = float(x[i])
s = 0

for i in range(len(x)):
    s = s + x[i]

m = s / len(x)

print("A média das notas é: %.2f" %m)