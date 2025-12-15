from typing import Any, Dict, List, Optional

__all__ = ["QueryResults"]

from typing import Union

from java.lang import Object
from java.util import AbstractList

from com.inductiveautomation.ignition.common import BasicDataset


class QueryResults(AbstractList):
    class Row(Object):
        def getKeys(self):
            # type: () -> List[Union[str, unicode]]
            pass

        def getKeyValue(self, aKey):
            # type: (Union[str, unicode]) -> Object
            pass

    def __init__(self, dataset, parent=None, parentRow=None):
        # type: (BasicDataset, Optional[Any], Optional[int]) -> None
        super(QueryResults, self).__init__()
        print(dataset, parent, parentRow)

    def addNestedQueryResults(self, key, results):
        # type: (Union[str, unicode], QueryResults) -> None
        print(key, results)

    def get(self, index):
        # type: (int) -> QueryResults.Row
        pass

    def getCoreResults(self):
        # type: () -> BasicDataset
        pass

    def getNestedQueryResults(self):
        # type: () -> Dict[Union[str, unicode], List[QueryResults]]
        pass

    def lookup(self, rowIndex, keyName):
        # type: (int, Union[str, unicode]) -> Object
        pass

    def size(self):
        # type: () -> int
        pass
