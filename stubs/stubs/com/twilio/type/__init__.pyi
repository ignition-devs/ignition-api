from typing import Union

from java.lang import Object

class PhoneNumber(Object):
    def __init__(self, number: Union[str, unicode]) -> None: ...
    def getEndPoint(self) -> Union[str, unicode]: ...
