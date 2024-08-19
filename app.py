import os

restaurantes = [{'nome':'Praça', 'categoria':'japonesa','ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'pizza','ativo':True},
                {'nome':'Cantina', 'categoria':'italiano','ativo':False}]

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def menu():
    input('\nDigite uma tecla para voltar para o menu principal ')
    main()

def exibir_titulo():
    print('''
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░''')

def exibir_opcoes():
    print('1 - Cadastrar Restaurante')
    print('2 - Listar Restaurantes')
    print('3 - Ativar Restaurante')
    print('4 - Sair\n')

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Qual a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante,'categoria':categoria,'ativo':False}

    restaurantes.append(dados_restaurante)

    print(f'O Restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    menu()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']

        print(f'- {nome_restaurante} | {categoria} | {ativo}')
    
    menu()

def finalizar_app():
    exibir_subtitulo('Encerrando Programa')

def opcao_invalida():
    print('Você digitou uma opção inválida')
    menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}\n')

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar Restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_titulo()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()