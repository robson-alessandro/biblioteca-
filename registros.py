from emprestimos import Emprestimos
from datetime import datetime

class Registros():
    def __init__(self):
        self.lista_emprestimos = []

    ## adiciona o emprestimo a lista
    def registrar(self, emprestimo:Emprestimos):
        self.lista_emprestimos.append({"pessoa":emprestimo.pessoa,"id usuario":emprestimo.id_usuario,"data_de_retirada":emprestimo.data_retirada,"data_de_devolução":emprestimo.data_devolucao,"id_emprestimo":emprestimo.id_emprestimo,"livro":emprestimo.lista_livros})
        print('emprestimo registrado')

    ## mostra a lista de emprestimo com o id usuario e id emprestimo
    def mostrar_emprestimos(self):
        for emprestimo in self.lista_emprestimos:
            print(emprestimo)

    ## fazar a devolução do livro recebendo o id do emprestimo e deletando ele dos registros e mostra se a entrega foi feita dentro do prazo
    def apagar_emprestimo(self, idEmprestimo):
        data = datetime.now()

        for emprestimo in self.lista_emprestimos:
            if emprestimo["id_emprestimo"] == idEmprestimo:
                if emprestimo['data_de_devolução']>= data.date():
                    emprestimo['data_de_devolução'] = data.date()
                    print('---------devolução concluida dentro da data')
                    self.lista_emprestimos.remove(emprestimo)
                    print(emprestimo)
                    return emprestimo['livro']
                else:
                    print('------------livro entregue atrasado')
                    emprestimo['data_de_devolução'] = data.date()
                    self.lista_emprestimos.remove(emprestimo)
                    print(emprestimo)
                    return emprestimo['livro']

  