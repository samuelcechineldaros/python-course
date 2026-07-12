import os

restaurantes = [{'nome':'Pizza Buonna', 'categoria':'Italiano', 'ativo':False},
                {'nome':'Sushi Saboroso', 'categoria':'Japonês', 'ativo':True},
                {'nome':'Pizza Suprema', 'categoria':'Italiano', 'ativo':False}]

def exibir_subtitulo(subtitulo):
    #os.system('cls')   # no windows
    os.system('clear')  # no mac e linux
    linha_adorno = '*' * (len(subtitulo))
    print(linha_adorno)
    print(subtitulo)
    print(linha_adorno)
    print()

def exibir_nome_app():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def listar_opcao():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar/Desativar restaurante')
    print('4. Sair\n')

def retornar_ao_menu_principal():
    input('\nDigite qualquer tecla para retornar ao menu principal.')
    main()

def opcao_invalida():
    print('Opção inválida\n')
    retornar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Escreva a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_novo_restaurante = {'nome':nome_do_restaurante ,'categoria':categoria_do_restaurante ,'ativo':False}
    restaurantes.append(dados_do_novo_restaurante)
    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    
    retornar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')

    #print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'activado' if restaurante['ativo'] else 'desactivado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    retornar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando o estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante para ativar/desativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
    
    retornar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
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

def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def main():
    #exibir_subtitulo()
    exibir_nome_app()
    listar_opcao()
    escolher_opcao()

if __name__ == '__main__':
    main()