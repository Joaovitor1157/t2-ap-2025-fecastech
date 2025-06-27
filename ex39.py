# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o 
# segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o 
# número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

t = []

for i in range(10):
    d = []
    d.append(input("Digite o nome do %i° Aluno: " %(i+1)))
    d.append(input("%s pertence a qual numero? " %d[0]))
    d.append(float(input("Digite a altura do %s:(cm) " %d[0])))
    t.append(d)

turma = t [0] [ 2]
p = 0
p2 = 0
for i in range(10):
    if t [i] [2] > turma:
        turma = t [i] [2]
        p = i

turma = t [0] [ 2]
for i in range(10):
    if t [i] [2] < turma:
        turma = t [i] [2]
        p2 = i

print("O aluno mais alto é %s pertencente ao numero %s, com %s cm de altura. " %(t[p] [0], t[p] [1], t[p] [2]))
print("O mais baixo é %s pertencente ao numero %s, com %s cm de altura." %(t[p2] [0], t[p2] [1], t[p2] [2])) 