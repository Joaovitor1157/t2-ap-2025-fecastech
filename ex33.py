# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um 
#conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem 
#como a média das temperaturas.

x = input("Digite as temperaturas registradas no dia separadas por virgula: "). split(",")
m = 0
for i in range(len(x)):
    x[i] = float(x[i])

for i in range(len(x)):
    m += x[i]
m = m / len(x)

for c in range(len(x)):
    g = len(x) 
    b = 0
    for i in range(len(x)):
        t = x[c] >= x[i]
        if t == True:
            b += 1
        elif t == False:
            g -= 1
    if b == len(x):
        maior = x[c]
    if g == 1:
        menor = x [c]
      

print("A média de temperatura foi de %.2f°C" %m)
print("A menor tempratura atingida foi de %.2f°C" %menor)
print("A maior tempratura atingida foi de %.2f°C" %maior)