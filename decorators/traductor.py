from typing import Callable

def get_translate(language: str) -> Callable[[str], None]:

    def spanish(text: str) -> None:
        print(text)
    
    def magic(text: str) -> None:
        print(text[::-1])

    if language == 'magic':
        return magic
    else:
        return spanish

if __name__ == "__main__":

    traductor = get_translate("magic")
    traductor("Estamos hablando al reves")  

    get_translate("spanish")("Estamos hablando al derecho")
