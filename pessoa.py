from abc import ABC,abstractmethod

## cria uma classe abstrata para ser herdada por estudante e professor
class Pessoa(ABC):

    @abstractmethod
    def data_devolucao(self):
        pass

    @abstractmethod
    def mostrar_usuario(self):
        pass

    @abstractmethod
    def buscar_nome(self):
        pass
    
    @abstractmethod
    def buscar_id(self):
        pass