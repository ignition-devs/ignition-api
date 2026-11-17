from __future__ import print_function

__all__ = ["PyResource"]

from typing import Any, List, Mapping, Optional, Union

from java.util import Date

from org.python.core import PyObject, PyTuple


class PyResource(PyObject):
    def __init__(self, resource=None):
        # type: (Any) -> None
        super(PyResource, self).__init__()
        print(resource)

    def getCollection(self):
        # type: () -> Union[str, unicode]
        pass

    def getDefiningCollection(self):
        # type: () -> Union[str, unicode]
        pass

    def getName(self):
        # type: () -> Optional[Union[str, unicode]]
        pass

    def getResourceType(self):
        # type: () -> PyTuple
        pass

    def getDocumentation(self):
        # type: () -> Optional[Union[str, unicode]]
        pass

    def getFiles(self):
        # type: () -> Mapping[Union[str, unicode], Any]
        pass

    def getFile(self, key):
        # type: (Union[str, unicode]) -> Any
        pass

    def getConfig(self):
        # type: () -> Any
        pass

    def getBackupConfig(self):
        # type: () -> Any
        pass

    def getFileNames(self):
        # type: () -> List[Union[str, unicode]]
        pass

    def getAttributes(self):
        # type: () -> PyObject
        pass

    def getAttribute(self, key):
        # type: (Union[str, unicode]) -> PyObject
        pass

    def getId(self):
        # type: () -> Optional[Union[str, unicode]]
        pass

    def getLastModificationActor(self):
        # type: () -> Optional[Union[str, unicode]]
        pass

    def getLastModificationTime(self):
        # type: () -> Optional[Date]
        pass

    def getResource(self):
        # type: () -> Any
        pass

    def isEnabled(self):
        # type: () -> bool
        pass

    def isSingleton(self):
        # type: () -> bool
        pass
