from typing import Callable

def getTalk(kind='shout') -> Callable[[str], str] :

    # We define functions on the fly
    def shout(word='yes') -> str:
        return word.upper() + '!'

    def whisper(word='yes') -> str:
        return word.lower() + '...'

    # Then we return one of them
    if kind == 'shout':
        # We don’t use '()'. We are not calling the function;
        # instead, we’re returning the function object
        return shout  
    else:
        return whisper

if __name__== "__main__":

    talk = getTalk("shout")
    print(talk("hola"))

    print(getTalk("whisper")("Hola"))
