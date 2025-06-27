#  O cardápio de uma lanchonete é o seguinte: 
 
# Especificação   Código  Preço 
# Cachorro Quente 100     R$ 1,20 
# Bauru Simples   101     R$ 1,30 
# Bauru com ovo   102     R$ 1,50 
# Hambúrguer      103     R$ 1,20 
# Cheeseburguer   104     R$ 1,30 
# Refrigerante    105     R$ 1,00 
 
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a 
# ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar 
# quando o pedido deve ser encerrado.

cardapio = [["Especificação" , "Código" , "Preço" ],["Cachorro Quente", 100 , 1.20 ],[ "Bauru Simples" , 101 ,1.30 ], ["Bauru com ovo", 102 , 1.50 ],["Hambúrguer" ,103 , 1.20 ],["Cheeseburguer",  104 , 1.30 ], ["Refrigerante" , 105 , 1.00 ]]
servir = [["Quantidade","Especificação" , "Código" , "Preço" , "Preço final" ]]
for linha in cardapio:
    print("{:<18}{:<9}{:<9}".format(*linha).replace("." , ","))
cod = int(input("Digite o codigo do alimento: "))
while True:
    for i in range(1 , 7):
        d = []
        j = 0
        if cod == cardapio [i] [1]:
            quant = int(input("Digite a quantidade de %s: " %cardapio[i] [0]))
            valor_final = quant*cardapio[i] [2]
            d.append(quant)
            d.append(cardapio[i] [0])
            d.append(cardapio[i] [1])
            d.append(cardapio[i] [2])
            d.append("R$ %.2f" %valor_final)
            servir.append(d)
            break
        else:
            j+=1
        if j == 6:
            print("Codigo não cadastrado")
            break
    resp = (input("Mais alguma coisa? "))
    if resp == "não":
        break
    else:
        cod = int(resp)

    if j == 6:
        print("Codigo não cadastrado")
        break
    
for linha in servir:
    print("{:<14}{:<18}{:<9}{:<9}{:<9}".format(*linha).replace("." , ","))
    