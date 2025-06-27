#A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série 
#até que o valor seja maior que 500. 

f = [0 , 1 , 1]
i = 1

while f[-1] < 500:
    c = f[i] + f[i + 1]
    f.append(c)
    i += 1

print(f)