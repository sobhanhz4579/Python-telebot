from product_info import *


def callback_query(call):
    d_call = {"call_message": call.message.chat.id, "call_data": call.data}
    send_product_info(d_call["call_message"], d_call["call_data"])
