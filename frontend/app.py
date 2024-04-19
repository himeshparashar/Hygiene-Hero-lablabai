
from chainlit import ChainLit
from llamas import llamandex

chainlit = ChainLit(api_key='lsk_U8KrTcBVse2-l_nLovGjZ5tYVEWDN0z-DsxSr07z56U')
llamandex = llamandex.Llamandex(api_key='GxoaE3L3CrsHp2fwVXCwO17XLlqg7mzBuefrp9HAGW4GfhM26lhrziNK3CnylmpI')

#chatbot logic

def handle_message(message):
    # Use Llamandex for natural language processing
    processed_message = llamandex.process_message(message)

    # Use ChainLit to handle conversation flow
    response = chainlit.get_response(processed_message)
    return response

#main loop to run your chatbot
if __name__ == '__main__':
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'quit':
            break
        response = handle_message(user_input)
        print('Bot:', response)
