import telebot 
import time 

token = "635347981:AAHQTSVlFLY7XL0Z3X1QbVraftoyMKuXv38"

bot.telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def start_command(message):
    chat_id = message.chat.id
    while True:
        bot.send_message(chat_id, "Бля")
        time.sleep(0.15)    
        bot.send_message(chat_id, "Хмт")

if __name__ == "__main__":
    bot.polling(none_stop = True)
