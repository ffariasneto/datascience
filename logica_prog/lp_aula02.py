''' INICIANDO PROJETO
-> Neste módulo você construirá um simulador de cadastro de senha e
inicialização de celular.

Vamos supor que o usuário acabou de comprar um celular na loja e após a primeira
carga, ele liga o celular pela primeira vez.

Ao iniciar o celular, a primeira coisa que aparecec na tela é o pedido para
cadastrar a senha e, logo após, confirmar a senha.

Essa é a sua primeira tarefa.
Construa o pedido de senha e confirmação.
Se a senha confirmada estiver correta, exiba a mensagem: Senha correta. Bem-vindo.
Senão, exiba a mensagem: Senha incorreta. Tente novamente.
'''

print("Olá! Sem bem-vindo(a) a tela de cadastro de usuário:")
print("Por favor, cadastre uma senha abaixo:")
senha = input(": -> ")
senha_confir = input("Digite a senha novamente para confirmar e efetuar o cadastro: ")
if senha_confir == senha:
    print("Senha correta. Bem-vindo(a)")
else:
    print("Senha incorreta. Tente novamente.")