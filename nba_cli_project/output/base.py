from abc import ABCMeta, abstractmethod
from typing import Any, Dict, List


class Output(metaclass=ABCMeta):
    @abstractmethod
    def send(self, data: List[Dict[str, Any]], selected_keys: List[List[str]]) -> None:
        pass
    
    @staticmethod
    def _get_value(
        data: Dict[str, Any], selected_keys: List[str], index: int = 0
    ) -> Any:
        value = data.get(selected_keys[index], "-")
        if isinstance(value, dict):
            return ConsoleOutput._get_value(value, selected_keys, index + 1)
        return value
