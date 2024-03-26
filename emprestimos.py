from datetime import datetime


class Emprestimos:
    def __init__(self ):
        self.pessoa =0
        self.id_usuario = 0
        self.data_retirada = 0
        self.data_devolucao = 0
        self.id_emprestimo = 0 
        self.lista_livros = 0

    ## metodo para criar um emprestimo de livro
    def pedir_emprestimo(self,pessoa,id_usuario,data_devolucao ,id_emprestimo, livros ):
        data = datetime.now()
        self.pessoa = pessoa
        self.id_usuario = id_usuario
        self.data_retirada = data.date()
        self.data_devolucao =data_devolucao
        self.id_emprestimo = id_emprestimo
        self.lista_livros = livros
        print(f'emprestimo feito com sucesso! data de devolução {self.data_devolucao} livro:{self.lista_livros}')


