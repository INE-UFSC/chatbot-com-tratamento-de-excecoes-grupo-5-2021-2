from abc import ABC, abstractmethod
from Bots.Comando import Comando

class Bot(ABC):

    def __init__(self, nome, comandos=[]):
        self.__nome = nome
        self.__comandos = comandos
        self.__mensagem_de_erro = 'Digite um comando válido.'

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos

    @property
    def mensagem_de_erro(self):
        return self.__mensagem_de_erro

    @mensagem_de_erro.setter
    def mensagem_de_erro(self, mensagem_de_erro):
        self.__mensagem_de_erro = mensagem_de_erro

    def adiciona_comando(self, comando, resposta):
        novo_comando = Comando(comando, resposta)
        self.comandos.append(novo_comando)

    def remove_comando(self, comando):
        if comando in self.comandos:
            self.comandos.remove(comando)

    def mostra_comandos(self):
        for i, comando in enumerate(self.comandos):
            print(f'{i} - {comando.pergunta}')

    def executa_comando(self, comando):
        if (comando < len(self.comandos)):
            print(f'--> {self.nome} diz: Você disse "{self.comandos[comando].pergunta}"')
            print(f' --> Eu te respondo: "{self.comandos[comando].resposta}"')
        else:
            print(f'{self.mensagem_de_erro}')

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass
