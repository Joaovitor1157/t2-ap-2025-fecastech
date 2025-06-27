#A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a 
#série até o n−ésimo termo. 

f = [1 , 1 , 2]
x = int(input("Vai querer quantos numeros: "))

for i in range( 1, x - 2):
    c = f[i] + f[i + 1]
    f.append(c)

print(f)