from typing import Any, Union

ISO8859_1: str
US_ASCII: str
UTF_8: str
UTF_16: str
UTF_16BE: str
UTF_16LE: str

def fileExists(filepath: Union[str, unicode]) -> bool: ...
def getTempFile(extension: Union[str, unicode]) -> Union[str, unicode]: ...
def readFileAsBytes(filepath: Union[str, unicode]) -> Any: ...
def readFileAsString(
    filepath: Union[str, unicode], encoding: Union[str, unicode] = ...
) -> Union[str, unicode]: ...
def writeFile(
    filepath: Union[str, unicode],
    data: Any,
    append: bool = ...,
    encoding: Union[str, unicode] = ...,
) -> None: ...
