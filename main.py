# Questão_01 python super
# Informar senha e email cadastrado para comparar com o do cliente

Senhadecadastro = "S1403"
emaildecadastro = "luciana@vutus.com"

while True:

    #Solicitar os dados ao usuario

    senhacliente = input("Digite a senha: ")
    emailcliente = input("Digite o email: ")

    if senhacliente == Senhadecadastro and emailcliente == emaildecadastro:
        print("Seja muito bem vindo")
        break #fim
    else:
        print("Dados incorretos, tente novamente.")