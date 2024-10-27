from product_info import *

dic_p = {'product_key': 1}


def send_welcome(message, bot):
    def p_key(x):
        if x:
            global dic_p
            dic_p['product_key'] = x
            send_product_info(message.chat.id, x, bot)
        else:
            bot.send_message(message.chat.id, "No message was found")

    global product_key
    product_key = message.text.split()[1] if len(
        message.text.split()) > 1 else None
    p_key(product_key)
    bot.send_message(
        message.chat.id, r"Welcome to the bot. Tap on the 'information' tab in the menu to start.")


def get_product_key():
    product_key = dic_p['product_key']
    return product_key
