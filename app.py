import os

restaurantes = [{'nome':'Praça', 'categoria':'japonesa','ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'pizza','ativo':True},
                {'nome':'Cantina', 'categoria':'italiano','ativo':False}]

def exibir_subtitulo(texto):
    '''Essa função é responsável em exibir o subtitulo'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def menu():
    '''Essa função é responsável em voltar para o menu principal'''
    input('\nDigite uma tecla para voltar para o menu principal ')
    main()

def exibir_titulo():
    '''Essa função é responsável em exibir o título do programa'''
    print('''
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░''')

def exibir_opcoes():
    '''Essa função é responsável em exibir as opções do menu principal'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def cadastrar_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - nome_restaurante
    - categoria

    Outputs:
    - Cadastra um novo restaurante
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Qual a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante,'categoria':categoria,'ativo':False}

    restaurantes.append(dados_restaurante)

    print(f'O Restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    menu()

def listar_restaurantes():
    '''Essa função é responsável em listar os restaurantes cadastrados'''
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    menu()

def alternar_estado_restaurante():
    '''Essa função é responsável por alternar o estado de um restaurante
    
    Inputs:
    - nome_restaurante

    Output:
    - Alterna o estado ativo ou desativo de um restaurante
    
    '''
    exibir_subtitulo('Alternando Estado do Restaurante')

    nome_restaurante = input('Digite o nome do restaurante a ser alterado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    menu()
    
def finalizar_app():
    '''Essa função é responsável por encerrar o programa'''
    exibir_subtitulo('Encerrando Programa')

def opcao_invalida():
    print('Você digitou uma opção inválida')
    menu()

def escolher_opcao():
    '''Essa função é responsável por fazer a escolha da opção do menu
    
    Input:
    - opcao_escolhida
    
    Outpost
    - Leva a função determinada

    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}\n')

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
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