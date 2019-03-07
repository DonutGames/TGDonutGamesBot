import telebot 
import time 

bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def start_command(message):
    chat_id = message.chat.id
    
    while True:
        bot.send_message(chat_id, "одолжи 1000 рублей) ", time.sleep(0.15))

if __name__ == "__main__":
    bot.polling(none_stop = True)
