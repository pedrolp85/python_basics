from typing import Dict, Any, List
import copy

CHILDRENS = [
    {"name": "Pedro", "age": 10, "teacher": "Maria", "sex": "hombre"},
    {"name": "Manolo", "age": 11, "teacher": "Juan", "sex": "hombre"},
    {"name": "Marta", "age": 11, "teacher": "Maria", "sex": "mujer"},
    {"name": "Carmen", "age": 15, "teacher": "Juan", "sex": "mujer"},
    {"name": "David", "age": 16, "teacher": "Maria", "sex": "hombre"},
    {"name": "Maria", "age": 10, "teacher": "Juan", "sex": "mujer"},
]

def childrens_by_age(childrens: List[Dict[str, Any]], age: int) -> List[Dict[str, Any]]:
    return list(filter(lambda x: x['age'] == age, childrens ))

def childrens_by_age_(childrens: List[Dict[str, Any]], age: int) -> List[Dict[str, Any]]:
    return [c for c in childrens if c['age'] == age]

#print(childrens_by_age(CHILDRENS, 10))
#print(childrens_by_age_(CHILDRENS, 10))

def childrens_by_age_and_teacher(childrens: List[Dict[str, Any]], age: int, teacher: str) -> List[Dict[str, Any]]:
    return list(filter(lambda x: x['age'] == age and x['teacher'] == teacher, childrens ))

def children_next_year(children: Dict[str, Any]) -> Dict[str, Any]:
    new_children = copy.deepcopy(children)
    new_children['age'] += 1
    return new_children

def childrens_next_year(childrens: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [children_next_year(children) for children in childrens]

print(childrens_next_year(CHILDRENS))

# Nota
# En python diccionarios y listas se pasan por referencia (por eficiencia) (objetos también)
# Por lo tanto modificar un valor de ellos cambiamos el original
# En caso de enteros, se pasan por valor (se crea una copia en memoria)
# Por eso dentro de la Comprehension list hacemos un deep copy llamando a otra función
# para no modificar los dict dentro de la lista

manolo = {"name": "Manolo", "age": 11, "teacher": "Juan", "sex": "hombre", "padres": {"madre":"Marta", "padre": "Juan"}}

def get_sex(children) -> str:
    children['name'] = "Pepe"
    children['age'] = 100
    return children['sex']

#print(manolo)
#print(get_sex(manolo))
#print(manolo)

def filter_children_teacher(childrens: List[Dict[str, Any]], age, teacher) ->List[Dict[str, Any]]:
    return [c for c in childrens if  c['teacher'] == teacher and c['age'] == age]


CHILDRENS_DICT = {
    "Pedro": {"name": "Pedro", "age": 10, "teacher": "Maria", "sex": "hombre"},
    "Manolo": {"name": "Manolo", "age": 11, "teacher": "Juan", "sex": "hombre"},
    "Marta": {"name": "Marta", "age": 11, "teacher": "Maria", "sex": "mujer"},
    "Carmen": {"name": "Carmen", "age": 15, "teacher": "Juan", "sex": "mujer"},
    "David": {"name": "David", "age": 16, "teacher": "Maria", "sex": "hombre"},
    "Maria": {"name": "Maria", "age": 10, "teacher": "Juan", "sex": "mujer"},
}

def generate_dict_by_name(childrens: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    return_dict = {}
    for c in childrens:
         return_dict[c["name"]] = c
    return return_dict

def generate_dict_by_name_(childrens: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    return {c["name"]: c for c in childrens}

print(generate_dict_by_name_(CHILDRENS))

# Nota: Recorrer diccionarios + Dict comprehension

def filter_dict_by_sex(childrens: Dict[str, Dict[str, Any]], sex: str) -> Dict[str, Dict[str, Any]]:
    return_dict = {}
    for c in children.values():
        pass
    for c in children.keys():
        pass
    for name, c in children.items():
        if c["sex"] == sex:
            return_dict[name] = c
    return return_dict

def filter_dict_by_sex_(childrens: Dict[str, Dict[str, Any]], sex: str) -> Dict[str, Dict[str, Any]]:
    return {k: v for k, v in children.items() if c['sex'] == sex}



