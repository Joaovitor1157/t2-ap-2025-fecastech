#Uma academia deseja fazer um censo entre seus clientes para descobrir o mais alto, o mais baixo, o mais 
#gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da 
#academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário 
#digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores 
#do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos 
#clientes

x = []
a = []
p = []
cda = []
go = m = j = 0

b = 0

y = int(input("Quantas pessoas vão participar do censo? "))

for i in range(y):
    n = input("%i° pessoa pode digitar seu nome: " %(i+1))
    x.append(n)

for i in range(len(x)):
    cd = int(input("%s Qual o seu codigo da academia? " %x[i]))
    cda.append(cd)
    pe = float(input("%s Qual o seu peso? (Kg) " %x[i]))
    p.append(pe)
    al = float(input("%s Qual a sua altura? (M)  " %x[i]))
    a.append(al)

for c in range(len(a)):
    b = 0
    for i in range(len(a)):
        l = a[c] >= a[i]
        if l == True:
            b += 1

    if b == len(a):
        j = c


for c in range(len(p)):
    g = len(p) 
    b = 0
    for i in range(len(p)):
        t = p[c] >= p[i]
        if t == True:
            b += 1
        elif t == False:
            g -= 1
    if b == len(p):
        go = c
    if g == 1:
        m = c

print("%s que pertence ao codigo %i, é a pessoa mais alta da academia com %.2f m" %(x[j] , cda[j] , a[j]))
print("%s que pertence ao codigo %i, é a pessoa mais gorda da academia com %.2f Kg" %(x[go] , cda[go] , p[go]))
print("%s que pertence ao codigo %i, é a pessoa mais magra da academia com %.2f Kg" %(x[m] , cda[m] , p[m]))