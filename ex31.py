#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de 
#conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá 
#receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser 
#informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e 
#perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta 
#operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser 
#conforme o exemplo abaixo: 
#Lojas Tabajara  
#Produto 1: R$ 2.20 
#Produto 2: R$ 5.80 
#Produto 3: R$ 0 
#Total: R$ 9.00 
#Dinheiro: R$ 20.00 
#Troco: R$ 11.00 

p = []
k = 1
print("Mercadinho do Sr. Manoel ")
while True:
    c = float(input("  Produto %i: R$ " %k))
    k += 1
    
    if c == 0:
        break
    else:
        p.append(c)

s = 0

for i in range(len(p)):
    s += p[i]


r = float(input("\nQual o valor recebido: "))
t = r - s
b = t
while True:
    
    if b < 0:
        b = -b
        print(" Falta %.2f\n" %b)
    else:
        break
    j = float(input("Qual o valor recebido: "))
    r += j
    b = j - b

t = r - s
print("\nMercadinho do Sr. Manoel")
print("  Quantidades de itens comprados: " , len(p))
print("  Valor da compra: R$ %.2f" %s)
print("  Valor recebido: R$ %.2f" %r)
print("  Troco a ser entregue : R$ %.2f " %t)