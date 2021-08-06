from abc import ABCMeta, abstractmethod
from typing import Any, Dict, List

from tabulate import tabulate


class PrintOutput(metaclass=ABCMeta):
    @abstractmethod
    def print_players_output_stream(
        self, players: List[dict], output: str, order_by: str
    ):
        pass

    @abstractmethod
    def print_matches_output_stream(
        self, players: List[dict], output: str, order_by: str
    ):
        pass


class Output(metaclass=ABCMeta):
    @abstractmethod
    def send(self, data: List[Dict[str, Any]], keys: List[List[str]]) -> None:
        pass


class ConsoleOutput(Output):
    def send(self, data: List[Dict[str, Any]], selected_keys: List[List[str]]) -> None:
        for d in data:
            print(" ".join(self._extract_data(d, selected_keys)))

    @staticmethod
    def _extract_data(
        data: Dict[str, Any], selected_keys: List[List[str]]
    ) -> List[str]:
        data_extracted = []
        for k in selected_keys:
            data_extracted.append(str(ConsoleOutput._get_value(data, k)))
        return data_extracted

    @staticmethod
    def _get_value(
        data: Dict[str, Any], selected_keys: List[str], index: int = 0
    ) -> Any:
        value = data.get(selected_keys[index], "-")
        if isinstance(value, dict):
            return ConsoleOutput._get_value(value, selected_keys, index + 1)
        return value


class TableConsoleOutput(ConsoleOutput):
    def send(self, data: List[Dict[str, Any]], selected_keys: List[List[str]]) -> None:
        data_extracted = [self._extract_data(d, selected_keys) for d in data]
        headers = ["_".join(k) for k in selected_keys]
        print(tabulate(data_extracted, headers=headers))


class FileOutput(Output):
    def send(self, data: List[Dict[str, Any]], selected_keys: List[List[str]]) -> None:
        # Implementar la funcion para imprimir en un fichero
        pass


class JSONFileOutput(FileOutput):
    pass


class YAMLFileOutput(FileOutput):
    pass


class CSVFileOutput(FileOutput):
    pass


_outputs = {
    "console": ConsoleOutput,
    "tableconsole": TableConsoleOutput,
    "jsonfile": JSONFileOutput,
    "yamlfile": YAMLFileOutput,
    "csvfile": CSVFileOutput,
}


def output_options(option: str = "tableconsole") -> Output:
    return _outputs[option]()
