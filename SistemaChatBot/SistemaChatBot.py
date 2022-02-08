from Bots.Bot import Bot
import time
import sys

class SistemaChatBot:
    def __init__(self, empresa: str, lista_bots: list):
        self.__empresa = empresa
        ##verificar se a lista de bots contém apenas bots
        for bot in lista_bots:
            if not isinstance(bot, Bot):
                erro = f'{bot} é do tipo {type(bot)} e não Bot'
                self.lista_bots.remove(bot)
                raise TypeError(erro)
        self.__lista_bots = lista_bots
        self.__bot = None
                
    @property 
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, empresa):
        self.__empresa = empresa
        
    @property
    def lista_bots(self):
        return self.__lista_bots

    @property
    def bot(self):
        return self.__bot

    @bot.setter
    def bot(self, bot):
        self.__bot = bot

    def boas_vindas(self):
        ##mostra mensagem de boas vindas do sistema
        print(f'Olá esse é o sistema de chatbots da empresa {self.empresa}')

    def mostra_menu(self):
        print('\nOs bots disponiveis no momento são:')
        for number, bot in enumerate(self.lista_bots):
            print(f'{number} - Bot: {bot.nome} - Mensagem de apresentação: {bot.apresentacao()}')
        ##mostra o menu de escolha de bots
    
    def escolhe_bot(self):
        escolha = int(input('\nDigite o número do chat bot desejado: '))
        while True:
            try:
                self.bot = self.lista_bots[escolha]
                print(f'\n--> {self.bot.nome} diz: {self.bot.boas_vindas()}')
                break
            except IndexError as e:
                print(f'Erro: {e}', file=sys.stderr)
                print('Por favor, selecione um Bot disponível.', file=sys.stderr)
                escolha = int(input('\nDigite o número do chat bot desejado: '))


        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

    def mostra_comandos_bot(self):
        self.bot.mostra_comandos()

    def le_envia_comando(self):
        escolha = int(input('\nDigite o comando desejado (ou -1 fechar o programa e sair): '))
        if escolha == -1:
            return '-1'
        else:
            self.bot.executa_comando(escolha)
            time.sleep(1)
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        ##mostra mensagem de boas-vindas do sistema
        self.boas_vindas()
        ##mostra o menu ao usuário
        self.mostra_menu()
        ##escolha do bot
        self.escolhe_bot()
        ##mostra mensagens de boas-vindas do bot escolhido
        self.bot.boas_vindas()
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        while True:
            self.mostra_comandos_bot()
            escolha = self.le_envia_comando()
            if escolha == "-1":
                print(f'--> {self.bot.nome} diz: {self.bot.despedida()}')
                time.sleep(1)
                break
        ##ao sair mostrar a mensagem de despedida do bot
