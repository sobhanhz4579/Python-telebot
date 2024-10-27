from telebot import types


def send_help(message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["item1", "item2", "item3"]
    buttons = [types.KeyboardButton("About") if i == "item1" else
               types.KeyboardButton("Contact us") if i == "item2" else
               types.KeyboardButton("⬅") if i == "item3" else None
               for i in btns]
    buttons = [button for button in buttons if buttons is not None]
    markup.add(*buttons)
    bot.send_message(
        message.chat.id, "Please choose an option:", reply_markup=markup)
