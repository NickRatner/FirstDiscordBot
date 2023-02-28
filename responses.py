import random

def get_response(message):
    p_message = message.lower()

    if p_message == 'hello':
        return 'hey there'

    if p_message == 'flip a coin':
        if random.randint(0,1) == 0:
            return 'heads'
        else:
            return 'tails'

    if p_message == '!help':
        return '`This is a help message`'


    return 'I don\'t understand, try !help'