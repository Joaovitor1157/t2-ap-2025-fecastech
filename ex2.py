#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input('Digite o nome de usuário: ')
senha = input("Digite uma senha: ")

while True:
    if nome != senha:
        print("Senha valida")
        break
    else:
        print("Erro 39, senha não pode ser igual ao nome. ")
        senha = input("Digite uma senha: ")