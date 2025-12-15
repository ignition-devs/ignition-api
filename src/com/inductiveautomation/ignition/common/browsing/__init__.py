from __future__ import print_function

__all__ = ["BrowseResults", "Result", "TagInfoResult"]

from typing import Any

from com.inductiveautomation.ignition.common.sqltags.model import TagInfo
from java.lang import Object


class BrowseResults(Object):
    def __init__(self, *args):
        # type: (Any) -> None
        pass

    def getContinuationPoint(self):
        pass

    def getResultQuality(self):
        pass

    def getResults(self):
        print(self)
        return [TagInfoResult(TagInfo())]

    def getReturnedSize(self):
        pass

    def getTotalAvailableSize(self):
        pass

    def setContinuationPoint(self, continuationPoint):
        pass

    def setResultQuality(self, value):
        pass

    def setResults(self, results):
        pass

    def setTotalAvailableResults(self, totalAvailableResults):
        pass


class Result(object):
    def getDisplayPath(self):
        raise NotImplementedError

    def getPath(self):
        raise NotImplementedError

    def getType(self):
        raise NotImplementedError

    def hasChildren(self):
        raise NotImplementedError


class TagInfoResult(Object, Result):
    def __init__(self, value):
        # type: (TagInfo) -> None
        pass

    def getDisplayPath(self):
        pass

    def getPath(self):
        pass

    def getType(self):
        pass

    def hasChildren(self):
        pass
