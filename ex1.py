#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
#continue pedindo até que o usuário informe um valor válido.

n = float(input('Digite uma nota entre 0 e 10: ').replace("," , "."))
while True:
    if n >= 0 and n <= 10:
        print("Nota válida")
        break
    else:
        print("Nota invalida, tente novamente")
        n = float(input('Digite uma nota entre 0 e 10: '))