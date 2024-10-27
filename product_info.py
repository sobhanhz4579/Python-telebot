import telebot
import logging
from functools import wraps

# logging
logging.basicConfig(
    filename=r'C:\Users\sobha\Desktop\app7.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s\n'
)

products = {
    'product1': {'name': 'product1', 'description': 'Short description of product2', 'Price': '10000'},
    'product2': {'name': 'product2', 'description': 'Short description of product2', 'Price': '20000'},
}

listtN = []


def dec_info(func):
    @wraps(func)
    def inner(chat_id, product_key, bot, *args, **kwargs):
        product = products.get(product_key)
        if product:
            message = f"description of product:\nname of product:\t{product['name']}\ndescription of product1:\t{product['description']}\n" \
                      f"Price of product:\t{product['Price']}\n"
            logging.info(f"Produkt: {product_key}, Message: {message}")
            global listtN
            listtN.append(message)
            bot.send_message(chat_id, message)

        else:
            error_message = "Sorry, this product was not found."
            logging.info(f"User ID: {chat_id}, Product: {product_key}, Error: {error_message}\n")
            bot.send_message(chat_id, error_message)
        return func(chat_id, product_key, bot, *args, **kwargs)

    return inner


@dec_info
def send_product_info(chat_id, product_key, bot):
    pass
