from random import choice
import re

def get_response(user_input: str, username: str) -> str:
    rand_responses = ['saying goodbye is painful', 'mirrors are more fun than television', 
                    'your past has a way of speaking up on you.  youll hear broken echoes of it everywhere, like a bad replay'
                    'legitimate?  youre stealing peoples organs.', '*takes pills* they had their body armor, i had mine', 
                    '*takes pills* breakfast of champions >;)', 'your past could destroy you, drive you mad.  it could set you free',
                    'after y2k, the end of the world had become a cliche.  everything was subjective, there were only personal apocalypses']

    hey_responses = [f'hey {username}', 'hi', 'sup', 'good day?']


    usrmsg: str = user_input.lower()
    if usrmsg == '':
        return "cool"
    elif re.search(r'\b(hello+|hi+|hey+)\b', usrmsg):
        return choice(hey_responses)
    else:
        return choice(rand_responses)