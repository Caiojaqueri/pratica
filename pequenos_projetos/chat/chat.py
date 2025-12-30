import os # biblioteca usada para interarir com sistema operacional

mensagens = []

nome = input("Nome: ")

while True: ##loop infinito

    #limpando o terminal
    os.system('cls')

    if len(mensagens) > 0: # se a lista de mensagens for maior que 0
        for m in mensagens: # para cada mensagem na lista de mensagens
            print(m['nome'], "-", m['texto']) # printa o nome e o texto da mensagem

    print("________________________________")

    # obtendo o texto
    texto = input("mensagem: ")
    if texto =="fim": # se o texto for igual a "fim"
        break # sai do loop

    #adicionando mensagem na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })
    