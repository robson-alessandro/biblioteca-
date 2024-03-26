import json

class Biblioteca:
    def __init__(self):
        self.biblioteca = []

    ## metodo que faz o cadastro do livro no banco de dados
    def cadastrar_livros(self, titulo,  autor, publicacao, editora, genero):
        self.biblioteca.append({"titulo": titulo,"autor":autor, "publicacao":publicacao,"editora":editora,"genero":genero,"status":"disponivel"})


    ## mostra a lista de livros 
    def mostrar_livros(self):
        for livro in self.biblioteca:
            print(livro)

    ## faz uma busca do livro recebe tres variaveis chave(em qual chave a busca sera realizada), valor(o valor que abusca deseja encontrar), retorno (cahve na qual o valor ira retornar)
    def buscar_livro(self,chave, valor, retorno):
        for x in self.biblioteca:
            if x[chave] == valor:
                return x[retorno]

    ## carrega os livros para uma lista de objetos
    def carregar_banco(self):
        with open("dado.json", 'r') as arquivo:
            dados = json.loads(arquivo.read())
        for u in dados:
            self.biblioteca.append(u)

    ## altera o status do livro 
    def alterar_status(self,livro,status):
        for x in self.biblioteca:
            if x["titulo"] == livro:
                x["status"] = status

    ## metodo para salvar os livros no banco de dados
    def gravar(self):
        with open("dado.json", "w") as arquivo:
            json.dump(self.biblioteca, arquivo , indent=4)