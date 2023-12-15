import telebot

API_KEY = api_key

bot = telebot.TeleBot(API_KEY)

def checking(msg):
  return True

# @bot.message_handler(func=checking)
# def answer(msg):
#   bot.reply_to(msg, "Olá seja bem vindo(a) ao Bot do Fábio!")

@bot.message_handler(commands=["pedir"])
def pedir(msg):
  bot.reply_to(msg, "Seu pedido está sendo processado!")

@bot.message_handler(commands=["menu"])
def pedir(msg):
  bot.reply_to(msg, "Temos bastante coisa no nosso menu confira")

@bot.message_handler(commands=["reclamar"])
def pedir(msg):
  bot.send_message(msg.chat.id, "Recebemos sua reclamação agradecemos por isso")

@bot.message_handler(func=checking)
def answer(msg):
  defaultText = """
  Você pode escolher uma dessas opções de comando abaixo
    /pedir    Fazer pedido
    /menu     Verificar opções ofercidas
    /reclamar Registrar uma reclamação pelo serviço prestado
  """ 
  bot.reply_to(msg, defaultText)

bot.polling()