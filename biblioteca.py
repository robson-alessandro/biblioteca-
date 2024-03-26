from datetime import datetime, timedelta
from livro import  Biblioteca
from emprestimos import Emprestimos
from estudante import Estudante
from professor import Professor
from registros import Registros
from pessoa import Pessoa


print('----------sistema biblioteca-------------')
escolha = 10

##cria listas para amazenar usuario
listaDeEstudante = []
listaDeProfessor = []

## carrega os livros do banco de dados para o objeto livros
livros = Biblioteca()
livros.carregar_banco()

## cria uma listra de registros para amazenar os emprestimos
registros = Registros()

## variavel para criar id ususario seguencialmente 
gerarId = 1

## variavel para criar id emprestimo seguencialmente
idEmprestimo = 1

## efetua as ações de acordo com a escolha pelo numero digitado 
while escolha != 0:
    escolha =int( input('\ndigite o numero referente a sua escolha:\n 1-criar usuario\n 2-mostrar livros\n 3-pedir emprestimo livro\n 4-mostrar registros de emprestimos\n 5-devolução \n 6- cadatrar livro \n0-sair do aplicativo : '))

    match escolha:

        ## metodo para criar o usuario (estudante ou professor)
        case 1:
            print('******criar usuario*******')
            nome = input('digite o nome do usuario:')
            telefone = input('digite o telefone do usuario:')
            email = input('digite o email do usuario:')
            tipoUsuario= int(input('digite qual o tipo de usuario ira criar(1-estudante, 2-professor): \n'))

            ## cria o usuario estudante
            if tipoUsuario == 1:
                estudante = Estudante(gerarId, nome , telefone, email)
                estudante.mostrar_usuario()
                listaDeEstudante.append(estudante)
                

            ## cria o usuario professor
            else:
                professor = Professor(gerarId, nome, telefone, email)
                professor.mostrar_usuario()
                listaDeProfessor.append(professor)
                
            gerarId +=1

        case 2 :
            print('******livros*******\n')
            
            ## mostra os livros do banco de dados
            livros.mostrar_livros()
        
        ## faz a criaçao de um emprestimo de livro relacionando com o usuario
        case 3:
            print('******pedir emprestimo*******\n')

            emprestimo = Emprestimos()
            tipoUsuario= int(input('digite qual usuario ira pedir o livro(1-estudante, 2-professor): \n'))

            ## ususario escolhe a busca por autor ou titulo
            escolha = input('deseja buscar livro por autor ou titulo?:')

            if escolha == 'autor':
                autor = input('digite o autor do livro: ')
                titulo = livros.buscar_livro('autor',autor,'titulo')

            else:
                titulo = input('digite o titulo do livro: ')

            
            ## confirma se o livro escolhido esta disponivel ou não
            if livros.buscar_livro('titulo',titulo,'status') == "indisponivel":
                    print('####titulo esta indisponivel!!!#####')
            else:

                ## faz o emprestimo de acordo com o usuario escolhido 
                if tipoUsuario == 1:
                    print(listaDeEstudante)

                    ## indentifica qual usuario faz o emprestimo
                    id =int(input('digite o id do estudante:'))
                    for usuario in listaDeEstudante:
                        if Estudante.buscar_id(usuario) == id:
                            estudante = usuario

                    dataDevolucao = estudante.data_devolucao()
                    nomeUsuario = estudante.buscar_nome()
                    idUsuario = estudante.buscar_id()
                    emprestimo.pedir_emprestimo(nomeUsuario, idUsuario, dataDevolucao, idEmprestimo, titulo)

                    ##faz o registro 
                    registros.registrar(emprestimo)

                else:
                    print(listaDeProfessor)

                    id =int(input('digite o id do professor:'))
                    for usuario in listaDeProfessor:
                        if Professor.buscar_id(usuario) == id:
                            professor = usuario

                    dataDevolucao = professor.data_devolucao()
                    nomeUsuario = professor.buscar_nome()
                    idUsuario = professor.buscar_id()
                    emprestimo.pedir_emprestimo(nomeUsuario, idUsuario ,dataDevolucao, idEmprestimo , titulo)
 
                    ##faz o registro 
                    registros.registrar(emprestimo)
                    
                ## altera o status do livro para indisponivel
                livros.alterar_status(titulo, "indisponivel")

                ## atualiza id do emprestimo
                idEmprestimo += 1

        ## mostra a lista de emprestimos
        case 4:
            print('******lista de emprestimos*******\n')
            registros.mostrar_emprestimos()
            

        ## faz a devolução do livro
        case 5:
            print('******devolução*******\n')
            id = int(input('digite o id do emprestimo que ira devolver:'))
            titulo = registros.apagar_emprestimo(id)
            livros.alterar_status(titulo , "disponivel")
            print('livro devolvido com sucesso!!!')
        
        ## faz o cadastro do livro no banco de dados
        case 6 :
            print('------cadastrar livro-----------')

            titulo = input('digite o titulo do livro:')
            autorLivro = input('digite o autor do livro:')
            publicacao = input('digite o ano de publicação:')
            editora = input('digite a editora:')
            genero = input('digite o genero:')

            ## cria o livro e chama o metodo para salvar no banco de dados
            livros.cadastrar_livros(titulo,autorLivro,publicacao,editora,genero)
            livros.gravar()
