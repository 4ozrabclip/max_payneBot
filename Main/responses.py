from random import choice
import re

from typing import Optional

from phishkiler import pkentry



def get_response(user_input: str, username: str) -> str:
    rand_responses = ['saying goodbye is painful', 'mirrors are more fun than television', 
                    'your past has a way of speaking up on you.  youll hear broken echoes of it everywhere, like a bad replay'
                    'legitimate?  youre stealing peoples organs.', '*takes pills* they had their body armor, i had mine', 
                    '*takes pills* breakfast of champions >;)', 'your past could destroy you, drive you mad.  it could set you free',
                    'after y2k, the end of the world had become a cliche.  everything was subjective, there were only personal apocalypses']

    hey_responses = [f'hey {username}', 'hi', 'sup', 'good day?']


    usrmsg: str = user_input.lower()
    if username == '4ozmaxpayne':
        return admin_responses(usrmsg)
    else:
        if usrmsg == '':
            return "cool"
        elif re.search(r'\b(hello+|hi+|hey+)\b', usrmsg):
            return choice(hey_responses)
        else:
            return choice(rand_responses)
    
def admin_responses(usrmsg: str) -> Optional[str]:
    if usrmsg == 'floodem':
        return "what address shall we flood? (flood {address})"
    elif usrmsg.startswith('flood ') and len(usrmsg.split()) > 1:
        address = usrmsg.split(' ', 1)[1].strip()
        return pkentry(address)

    if re.search(r'\b(hello+|hi+|hey+)\b', usrmsg):
        return "my master, what do you need?"
    elif re.search(r'\b(nothing+)\b', usrmsg):
        return "no problem mane"
