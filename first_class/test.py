from typing import List, Dict

"""
Implementame la clase Person y sus metodos con NamedTupled:
https://docs.python.org/3/library/collections.html#collections.namedtuple
"""

CURRENT_YEAR = 2021
JOB_NAME = ['developer', 'Software Engineer']


def suma_array(numeros: List[float]) -> float:
    suma = 0.0
    for i in numeros:
        suma = suma + i
    return suma

class Person:
    NUM_FINGERS = 20

    def __init__(self, name: str, birth_date:int, job:str) -> None:
        self.name = name
        self.birth_date = birth_date
        self.job = job

    def greetings(self, other_person: "Person") -> None:
        """
        Aqui vamos a aprender fstring
        """
        print(f"Hola soy {self.name}, soy {self.job} y tengo {2021-self.birth_date} años")
        print(f"¿Tu eres {other_person.name}?")

    def drinker(self) -> bool:
        """
        Generalmente no es bueno tener mas de un return
        Tampoco es recomendable tener operaciones en un if
        Mantenimiento del codigo:
            * El tiempo pasa, intenta usar constantes para algunos valores
            * Las leyes cambian... En USA solo se puede beber a partir de los 21
        """
        # if 2021-birth_date >= 18:
        #    print(f"Hola {name}, tu si puedes beber alcohol")
        #    return True
        # else:
        #    print(f"Hola {name}, tu no puedes beber alcohol")
        #    return False
        age = CURRENT_YEAR - self.birth_date
        can_drink = age >= 18  # Mover a constante
        msg = (
            f"Hola {self.name}, tu si puedes beber alcohol"
            if can_drink 
            else f"Hola {self.name}, tu no puedes beber alcohol"
        )
        print(msg)
        return can_drink

    def is_developer(self) -> bool:

        is_develop = self.job in JOB_NAME
        msg = (
            "Tu si eres programador"
            if is_develop
            else "Tu no eres programador"
        )
        print(msg)
        return is_develop
    


def multiply_elements(array:List[int], multiplex:int) -> List[int]:
    """
    comprehension list python
    """
    # multiplied_list = []
    # for number in array:
    #    if number % 2 != 0:
    #        multiplied_list.append(number*multiplex)
    
    # return multiplied_list
    return [n * multiplex for n in array if n % 2 != 0]

def print_keys(dictionary: Dict[str, str]) -> None:
    print(list(dictionary.keys()))






def main():
    print("hola")
    array_var = [1.23, 2.23]
    tuple_var = (1.23, 2.23)
    resultado = suma_array(array_var)
    print(resultado)
    pedro = Person('Pedro', 1985, 'Programador')
    david = Person('David', 1993, 'Programador')
    pedro.greetings(david)
    pedro.is_developer()
    pedro.drinker()
    print(multiply_elements([2, 3], 3))
    print_keys({'clave1':'valor1'})

    pedro_2 = Person('Pedro', 1985, 'Programador')
    print(f"Son iguales?: {pedro == pedro_2}")
    print(f"Cuantos dedos tiene Pedro? {pedro.NUM_FINGERS}")
    print(f"Cuantos dedos tiene una persona? {Person.NUM_FINGERS}")


if __name__ == "__main__":
    main()