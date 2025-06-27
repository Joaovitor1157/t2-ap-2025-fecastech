# 38) Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que: 
#     a) Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00; 
#     b) Em 1996 recebeu aumento de 1,5% sobre seu salário inicial; 
#     c) A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do 
#     ano anterior. Faça um programa que determine o salário atual deste funcionário. Após concluir isto, 
#     altere o programa permitindo que o usuário digite o salário inicial do funcionário. 

si = 1000
t = 1.5
s = si
print("1995 - R$ 1000,00")
for i in range(1995 , 2025):
    a = si * (t/100)
    s += a
    t = t * 2
    print("%i - R$ %.2f"%(i+1 , s))