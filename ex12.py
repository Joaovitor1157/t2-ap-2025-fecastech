#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O 
#usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo: 

v = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9, 10]
x = int(input("Digite o numero da tabuada q deseja ver: "))

print("A tabuada do", x ,"é: ")
for i in range(len(v)):
    p = v[i] * x
    print(v[i], "X", x ,"=", p)