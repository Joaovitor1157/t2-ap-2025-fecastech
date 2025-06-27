#Faça um programa que leia 5 números e informe a soma e a média dos números. 

x = input("Digite uma sequencia de 5 numeros separados por virgula: "). split(",")
s = 0
for i in range(len(x)):
    x[i] = float(x[i])
for i in range(len(x)):
    s = s + x[i]
m = s / len(x)

print("A soma da sequência é" , s)
print("A média da sequência é" , m)