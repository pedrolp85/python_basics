from typing import Any, Dict, List

from tabulate import tabulate

from output.base import Output


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



class TableConsoleOutput(ConsoleOutput):
    def send(self, data: List[Dict[str, Any]], selected_keys: List[List[str]]) -> None:
        data_extracted = [self._extract_data(d, selected_keys) for d in data]
        headers = ["_".join(k) for k in selected_keys]
        print(tabulate(data_extracted, headers=headers))
