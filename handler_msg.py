from telebot import *
from main_telegrambot import *

global info_message
info_message = ""
user_details2 = {}


def handle_message(message, bot):
    product_key = get_product_key()
    username = message.from_user.username
    chat_id = message.chat.id
    text = message.text

    if username is None:
        bot.send_message(chat_id, "You don't have a username")
    else:
        user_details2[chat_id] = {
            "username": username
        }

    if text == "About":
        bot.send_message(chat_id, "This bot was created by 'Sobhan Hassanzadeh' ")
    elif text == "Contact us":
        email = "sobhanhsnzde4579@gmail.com"
        website = "www.google.com"
        LinkedIn_account = "https://www.linkedin.com/in/sobhan-hasanzade-24b6a5251?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BCoG%2B44v6TSWsZlt7M2HbCA%3D%3D"
        git_account = "https://github.com/sobhanhz4579"
        Contact_info = f"Email:{email}\nWebsite:{website}\nLinkedIn_account:{LinkedIn_account}\n Git_account:{git_account}"
        bot.send_message(chat_id, Contact_info)
    elif text == "⬅":
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(chat_id, "You are back in the main menu.",
                         reply_markup=markup)
    elif text == "Enter your information:":
        bot.send_message(chat_id, "Please type your first name and last name:")
        user_details[chat_id] = {'step': 'name'}
    elif chat_id in user_details:
        if user_details[chat_id]['step'] == 'name':
            user_details[chat_id]['name'] = text
            bot.send_message(chat_id, "Please type your address:")
            user_details[chat_id]['step'] = 'address'
        elif user_details[chat_id]['step'] == 'address':
            user_details[chat_id]['address'] = text
            bot.send_message(chat_id, "Please type your mobile_number:")
            user_details[chat_id]['step'] = 'mobile_number'
        elif user_details[chat_id]['step'] == 'mobile_number':
            user_details[chat_id]['mobile_number'] = text
            bot.send_message(chat_id,
                             f"Your information:\nName:{user_details[chat_id]['name']}\nAddress:{user_details[chat_id]['address']}"
                             f"\nMobile_number:{user_details[chat_id]['mobile_number']}")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_y = types.KeyboardButton("Yes")
            item_n = types.KeyboardButton("No")
            item_b = types.KeyboardButton("⬅")
            markup.add(item_y, item_n, item_b)
            bot.send_message(
                chat_id, "Are you sure about your information?", reply_markup=markup)
            user_details[chat_id]['step'] = 'confirm'
        elif user_details[chat_id]['step'] == 'confirm':
            if text == "Yes":
                markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item_1 = types.KeyboardButton("Bank1's portal")
                item_2 = types.KeyboardButton("Bank2's portal")
                item_3 = types.KeyboardButton("⬅")
                markup2.add(item_1, item_2, item_3)
                bot.send_message(
                    chat_id, "Please select your banking portal:", reply_markup=markup2)
                user_details[chat_id]['step'] = 'Payment receipt'
            else:
                bot.send_message(
                    chat_id, "Please enter your information again.")
                user_details[chat_id]['step'] = 'name'
        elif user_details[chat_id]['step'] == 'Payment receipt':
            if text == "Bank1's portal":
                user_details[chat_id]['Payment receipt'] = "Bank1's portal"
            elif text == "Bank2's portal":
                user_details[chat_id]['Payment receipt'] = "Bank2's portal"

            bot.send_message(
                chat_id,
                "Your payment has been processed successfully. Your information along with the payment receipt has been sent.")

            bot.send_message(chat_id,
                             f"Your information:\n "
                             f"Name:\t{user_details[chat_id]['name']}\n "
                             f"Address:\t{user_details[chat_id]['address']}"
                             f"\nMobile_number:\t{user_details[chat_id]['mobile_number']}"
                             f"\nPayment receipt:\t{user_details[chat_id]['Payment receipt']}")
            send_product_info(chat_id, product_key)
            global info_message

            info_message = (f"Your information:\n"
                            f"Name:\t{user_details[chat_id]['name']}\n"
                            f"Address:\t{user_details[chat_id]['address']}"
                            f"\nMobile_number:\t{user_details[chat_id]['mobile_number']}"
                            f"\nPayment receipt:\t{user_details[chat_id]['Payment receipt']}"
                            f"\nUsername:\t@{user_details2[chat_id]['username']}")

            try:
                bot.reply_to(
                    message,
                    "Thank you for your purchase."
                    " Your information has now been sent to the Support-Team for shipping and registration.")
                bot.send_message(SUPPORT_CHAT_ID, info_message)
                bot.send_message(SUPPORT_CHAT_ID, [listtN[i] for i in range(0, len(listtN))])

            except telebot.apihelper.ApiTelegramException as e:
                print(f"Error sending the message to support: {e}")
                bot.reply_to(
                    message, f"Message to support could not be sent. Error!!! : {e.description}")


def send_product_info(chat_id, product_key):
    message = f"Produkt Key: {product_key}"
    bot.send_message(SUPPORT_CHAT_ID, message)
