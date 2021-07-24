from abc import ABCMeta, abstractmethod

#  Nota: Esta es la explicación de por qué las clases abstractas ahorran código
#       El concepto de clase abstracta está muy ligada a la herencia
#       Cuando un método es útil en 2 clases hijas, podemos definirlo 
#       e implmentarlo en la clase abstracta, de forma que nos ahorramos implmentarlo 
#       en cada clase hija (childrens_alpha(self))
#       Es es útil cuando por ejemplo la diferencia de las clases hijas es que obtienen datos
#       de forma diferente
#       No hay problema en llamar a un método implementado en el padre desde un objeto instanciado en el hijo
#       En Python la diferencia entre interfaz y clase abstracta es muy difusa, no como en Java
#       --> Un hijo se puede hacer pasar por un padre pero un padre no por un hijo <--
#                   Los hijos heredan las implementaciones de los padres

class ClassRoom(metaclass=ABCMeta):

    @abstractmethod
    def get_childrens(self):
        pass
    
    def childrens_alpha(self)
        return sorted(self.get_childrens().keys())


class ClassRoomPrimary(ClassRoom):

    def get_childrens(self):
        return {
            "manolo": {"age": 10},
            "pedro": {"age": 10},
        }
    

class ClassRoomSecundary(ClassRoom):

    def get_childrens(self):
        return {
            "maria": {"age": 10},
            "marta": {"age": 10},
        }

    def pepito():
        return 1
    


print(ClassRoomPrimary().childrens_alpha())
print(ClassRoomSecundary().childrens_alpha())