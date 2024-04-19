import os
from chainlit import ChainLit
from llamas import llamandex

from llama_index import SimpleDirectoryReader
from llama_index.indices import VectaraIndex

chainlit = ChainLit(api_key='lsk_U8KrTcBVse2-l_nLovGjZ5tYVEWDN0z-DsxSr07z56U')
llamandex = llamandex.Llamandex(api_key='GxoaE3L3CrsHp2fwVXCwO17XLlqg7mzBuefrp9HAGW4GfhM26lhrziNK3CnylmpI')

def before_chainlit_hook(message):
 
    print(f'Before ChainLit: {message}')
    return message

def after_chainlit_hook(response):

    print(f'After ChainLit: {response}')
    return response
# Set the hook functions in ChainLit
chainlit.before_message_send(before_chainlit_hook)
chainlit.after_message_receive(after_chainlit_hook)

#chatbot logic

def handle_message(message):
    # Use Llamandex for natural language processing
    processed_message = llamandex.process_message(message)

    # Use ChainLit to handle conversation flow
    response = chainlit.get_response(processed_message)
    return response

