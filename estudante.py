from pessoa import Pessoa
from datetime import datetime, timedelta

class Estudante(Pessoa):
    def __init__(self,id_pessoa,nome, telefone, email, tipo='estudante'):
        self.__id_pessoa = id_pessoa
        self.__nome = nome 
        self.__telefone = telefone
        self.__email = email
        self.__tipo = tipo

    ## metodo retorna nome do usuario
    def buscar_nome(self):
        return self.__nome
    
    ## metodo retorna id do usuario
    def buscar_id(self):
        return self.__id_pessoa

    ## retorna a data de devolução do livro de acordo com o usuario 3 dias para estudante
    def data_devolucao(self):
        data= datetime.now()
        dataEmprestimo  = data + timedelta(days=3)
        return (dataEmprestimo.date())
    
    ## mostrar os atributos
    def mostrar_usuario(self):
        print(f'usuario cadastrado!  id usuario: {self.__id_pessoa} - nome: {self.__nome} - telefone: {self.__telefone} - email: {self.__email} - tipo:{self.__tipo}')

    def __repr__(self):
        return f'id usuario: {self.__id_pessoa} - nome: {self.__nome} - telefone: {self.__telefone} - email: {self.__email} - tipo:{self.__tipo}'
    
