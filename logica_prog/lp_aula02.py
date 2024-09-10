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

''' Continuação do projeto Aula 03.
1. Implementar o while ao projeto.
2. A senha cadastrada anteriormente precisa de um looping, caso o usuário digite a senha errada.
3. A primeira senha deve ser igual a confirmação de senha.
4. Enquanto o usuário não confirmar, o seu programa exibirá a mensagem:
"Senha incorreta, tente novamente."
'''

''' Código já adionado com número de tentativas, caso o usuário erre três vezes a senha, o mesmo
será bloqueado. - Aula 04
'''
tentativas = 0
print("Olá! Sem bem-vindo(a) a tela de cadastro de usuário:")
print("Por favor, cadastre uma senha abaixo:")
senha = input(": -> ")
senha_confir = input("Digite a senha novamente para confirmar e efetuar o cadastro: ")

while senha_confir != senha and tentativas < 3:
    print("Senha incorreta. Tente novamente.")
    tentativas += 1
    senha_confir = input("Digite a senha novamente para confirmar: ")

if senha_confir == senha:
    print("Senha correta. Bem-vindo(a)!")
else:
    print("Número de tentativas excedido. Usuário bloqueado.")