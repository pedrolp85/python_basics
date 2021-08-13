from output.base import Output
from output.console import ConsoleOutput, TableConsoleOutput
from output.file import CSVFileOutput, JSONFileOutput, YAMLFileOutput

_outputs = {
    "console": ConsoleOutput,
    "tableconsole": TableConsoleOutput,
    "jsonfile": JSONFileOutput,
    "yamlfile": YAMLFileOutput,
    "csvfile": CSVFileOutput,
}


def get_output(option: str = "tableconsole") -> Output:
    return _outputs[option]()
