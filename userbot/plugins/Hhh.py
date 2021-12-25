import random

import requests
import telebot
from telebot import types

token = "1465209146:AAFZShk9wfEZxZof7eED_E9s1L4T8hkW858"
bot = telebot.TeleBot(token)
r = requests.session()
co = types.InlineKeyboardButton(text="- غنيلي", callback_data="check")
# ----#


@bot.message_handler(commands=["start"])
def start(message):
    message.from_user.username
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(co)
    message.chat.id
    bot.send_message(
        message.chat.id,
        text=f"""<strong>
Hi <code>{fr}</code>, 
- - - - - - - - - - 
اهلا بك في بوت غنيلي! 
اضغط غنيلي ليتم اختيار اغنية عشوائية 
- - - - - - - - - - 
By  : @aauua 
</strong>
    """,
        parse_mode="html",
        reply_to_message_id=message.message_id,
        reply_markup=maac,
    )


@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
    if call.data == "check":
        combo(call.message)


def combo(message):
    bot.send_message(
        message.chat.id,
        "<strong>يتم العثور الرجاء الانتظار... </strong>",
        parse_mode="html",
    )
    rl = random.randint(74, 154)
    url = f"https://t.me/KVUUU/{rl}"
    bot.send_audio(
        message.chat.id, url, caption="<strong>الاغنية </strong>", parse_mode="html"
    )


# داشوفك تريد تخمط
bot.polling(True)
