__all__ = ["ShelvedPath"]

from typing import Any

from java.lang import Object


class ShelvedPath(Object):
    def __init__(self, *args):
        # type: (Any) -> None
        print(args)

    def getExpiration(self):
        pass

    def getHitCount(self):
        pass

    def getPath(self):
        pass

    def getShelveTime(self):
        pass

    def getUser(self):
        pass

    def isExpired(self):
        pass
