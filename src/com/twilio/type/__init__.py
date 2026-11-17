from __future__ import print_function

__all__ = ["PhoneNumber"]

from typing import Union

from java.lang import Object


class PhoneNumber(Object):
    def __init__(self, number):
        # type: (Union[str, unicode]) -> None
        super(PhoneNumber, self).__init__()
        print(number)

    def getEndPoint(self):
        # type: () -> Union[str, unicode]
        pass
