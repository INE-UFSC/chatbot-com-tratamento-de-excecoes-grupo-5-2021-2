class Comando():
    def __init__(self, pergunta, resposta):
        self.__pergunta = pergunta
        self.__resposta = resposta

    @property
    def pergunta(self):
        return self.__pergunta

    @property
    def resposta(self):
        return self.__resposta
