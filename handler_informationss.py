from telebot import types


def send_informationen_plans(message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns2 = ["item1", "item2"]
    buttons2 = [types.KeyboardButton("Enter your information:") if i == "item1" else
                types.KeyboardButton("⬅") if i == "item2" else None
                for i in btns2]
    buttons2 = [button for button in buttons2 if buttons2 is not None]
    markup.add(*buttons2)
    bot.send_message(
        message.chat.id, "Choose one of these options", reply_markup=markup)
