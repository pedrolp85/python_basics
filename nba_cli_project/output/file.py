import json

from abc import ABCMeta, abstractmethod
from typing import Any, Dict, List

import yaml

from output.base import Output


class FileOutput(Output, metaclass=ABCMeta):

    def __init__(self, path: str) -> None:
        self.path = path

    def send(self, data: List[Dict[str, Any]], selected_keys: List[List[str]]) -> None:
        # Implementar la funcion para imprimir en un fichero
        f = open(self.path, 'w')
        f.write(self._transform_data(data))
        f.close()


    @abstractmethod
    def _transform_data(self, data: List[Dict[str, Any]]) -> str:
        pass


class JSONFileOutput(FileOutput):

    def __init__(self, path: str = "tmp/data.json") -> None:
        super().__init__(path)

    def _transform_data(self, data: List[Dict[str, Any]]) -> str:
        return json.dumps(data, indent=4, sort_keys=True)

class YAMLFileOutput(FileOutput):
    
    def __init__(self, path: str = "tmp/data.yml") -> None:
        super().__init__(path)

    def _transform_data(self, data: List[Dict[str, Any]]) -> str:
        return yaml.dump(data)


class CSVFileOutput(FileOutput):
    
    def _transform_data(self, data: List[Dict[str, Any]]) -> str:
        pass
