# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da 
# dívida, valor dos juros, quantidade de parcelas e valor da parcela. 
# Os juros e a quantidade de parcelas seguem a tabela abaixo: 
 
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida 
# 1       0 
# 3       10 
# 6       15 
# 9       20 
# 12      25 
 
# Exemplo de saída do programa: 
 
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela 
# R$ 1.000,00     0               1                       R$  1.000,00 
# R$ 1.100,00     100             3                       R$    366,00 
# R$ 1.150,00     150             6                       R$    191,67 

valor = float(input("Digite o valor da divida: R$ ").replace("," , "."))
d = []
matriz = [["Valor da Dívida", "Valor dos Juros", "Quantidade de Parcelas" , "Valor da Parcela"]]
taxa = 0.05
for i in range(0, 13 , 3):
    d =[]
    if i == 0:
        d.append(("R$ %.2f" %valor).replace("." , ","))
        d.append("R$ 0")
        d.append(str(1))
        d.append(("R$ %.2f" %valor).replace("." , ","))
        matriz.append(d)
    else:
        taxa += 0.05
        juros = valor * taxa
        vf = valor + juros
        d.append(("R$ %.2f" %vf).replace("." , ","))
        d.append(("R$ %.2f" %juros).replace("." , ","))
        d.append(str(i))
        d.append(("R$ %.2f" %(vf/i)).replace("." , ","))
        matriz.append(d)
for i in matriz:
    print("{:<18}{:<18}{:<24}{:<18}".format(*i))