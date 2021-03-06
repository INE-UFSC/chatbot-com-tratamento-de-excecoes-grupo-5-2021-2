from Bots.Bot import Bot
from Bots.Comando import Comando

class BotMarombeiro(Bot):
    def __init__(self, nome: str):
        self.__nome = nome
        self.__comandos = [
            Comando('Eai frango', 'Frango é tu rapaz, tem nem 40 de braço, ta doido!?!'),
            Comando('Me passa um treino?', '3x10 supino\n3x10 barra fixa\n3x10 rosca direta\n3x10 tríceps testa\n(perna não precisa)'),
            Comando('Conselho', 'Quer ficar grande? Tem que comer e treinar todo dia!')]
        self.__mensagem_de_erro = 'Digita o comando certo, seu frango!'

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

    def apresentacao(self):
        return 'Treino e dieta eu não furo, tá ligado?'

    def boas_vindas(self):
        return 'HORA DO SHOW P****!'

    def despedida(self):
        return 'Valeu mermão, até a próxima.'
        