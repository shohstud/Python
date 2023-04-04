import telebot
import requests
import openai

# saytdan olingan API_KEY yozamiz
API_KEY = "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"

bot = telebot.TeleBot("6028750912:AAHRDYblM3ID3ry8h9mxoNJ_lKR0Uy6Ly3c")

# /start komandasini kiritish
@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id, "Salom! Men yangiliklarni taqdim etuvchi botman buning uchun menga o'zing istagan yangilik turini Ingliz tilida kiriting! Masalan:sport, study")

@bot.message_handler(func=lambda message: True)
def handle_message(message):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="You: What have you been up to?\nFriend: Watching old movies.\nYou: Did you watch anything interesting?\nFriend:",
    temperature=0.5,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    stop=["You:"]
)
    bot.send_message(message.chat.id,response['choices'][0]['text'] )
bot.polling()