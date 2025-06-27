#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e 
#a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos. 

x = int(input("Quantas turmas tem? "))
h= []
p=0

for i in range(1 , x+1):
    while True:
        y = int(input("Quantos alunos tem na %i° turma? " %i))
        if y <= 40:
            h.append(y)
            break
        else:
            print("Muitos alunos por turma, verifique novamente se tem menos de 40 alunos")


for i in range(len(h)):
    p += h[i]
p = p / len(h)

print("A média de alunos por turma é %.2f pessoas" %p , len(h))