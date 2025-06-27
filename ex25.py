#Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a média de 
#idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, 
#conforme a média calculada. 

x = int(input("Digite a idade de todas as pessoas separado por espaço: ")). split()
p = 0

for i in range(len(x)):
    p += x[i]
p = p / len(x)

if p >=0 and p <= 25:
    print("A média do grupo é de Jovens")
elif p >= 25.1 and p <= 60:
    print("A média do grupo é de Adultos")    
else:
    print("A média do grupo é de Idosos")