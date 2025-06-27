#  40) Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram 
#     obtidos os seguintes dados: 
# a) Código da cidade; 
# b) Número de veículos de passeio (em 1999); 
# c) Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber: 
# d) Qual o maior e menor índice de acidentes de trânsito e a que cidade pertence; 
# e) Qual a média de veículos nas cinco cidades juntas; 
# f) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

estatistica = []
s = t = 0
for i in range(5):
    cidade = []
    cidade.append(input("Digite o codigo da cidade: "))
    cidade.append(int(input("Digite o número de veículos de passeio (em 1999): ")))
    cidade.append(int(input("Digite o número de acidentes de trânsito com vítimas (em 1999): ")))
    estatistica.append(cidade)

#médias
for i in range(5):
    s += estatistica [i] [1]
mc = s / 5
mc = float("%.2f" %mc)
s = 0
for i in range(5):
    if estatistica[i] [2] < 2000:
        s += estatistica [i] [2]
        t += 1
ma = s / t
ma = float("%.2f" %ma)

# menor e maior
maior = estatistica [0] [ 2]
p = 0
for i in range(5):
    if estatistica [i] [2] > maior:
        maior = estatistica [i] [2]
        p = i

menor = estatistica [0] [2]
p2 = 0
for i in range(5):
    if estatistica [i] [2] < menor:
        menor = estatistica [i] [2]
        p2 = i

print("A cidade com o maior indice de acidentes é a %s, com %i acidentes de transito" %(estatistica[p] [0], estatistica[p] [2]))
print("A cidade com o menor indice de acidentes é a %s, com %i acidentes de transito" %(estatistica[p2] [0], estatistica[p2] [2]))
print("A média de veiculos nas cincos cidades é" , mc)
print("A média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio é" , ma)