#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotMarombeiro import BotMarombeiro

###construa a lista de bots disponíveis aqui
lista_bots = [BotMarombeiro("Bambam")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
