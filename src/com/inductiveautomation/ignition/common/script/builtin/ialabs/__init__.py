from __future__ import print_function

__all__ = [
    "BrowseTag",
    "OPCBrowseTag",
    "TagAlarmDefinition",
    "TagAlarmProperty",
]

from typing import List, Optional

from com.inductiveautomation.ignition.common.opc import BrowseElementType
from com.inductiveautomation.ignition.common.sqltags.model.types import (
    DataType,
    TagType,
)
from java.lang import Class, Object, String


class BrowseTag(Object):
    dataType = None  # type: DataType
    name = None  # type: str
    fullPath = None  # type: str
    path = None  # type: str
    type = None  # type: TagType
    valueSource = None  # type: str

    def __init__(
        self,
        name,  # type: str
        path,  # type: str
        fullPath,  # type: str
        type_,  # type: TagType
        valueSource,  # type: str
        dataType,  # type: DataType
    ):
        self.name = name
        self.path = path
        self.fullPath = fullPath
        self.type = type_
        self.valueSource = valueSource
        self.dataType = dataType

    def getDataType(self):
        return self.dataType

    def getFullPath(self):
        return self.fullPath

    def getPath(self):
        return self.path

    def getTagType(self):
        return self.type

    def getValueSource(self):
        return self.valueSource

    def isDB(self):
        print(self)
        return True

    def isExpression(self):
        print(self)
        return True

    def isFolder(self):
        print(self)
        return True

    def isMemory(self):
        print(self)
        return True

    def isOPC(self):
        print(self)
        return True

    def isQuery(self):
        print(self)
        return True

    def isUDT(self):
        print(self)
        return True

    def toString(self):
        pass


class OPCBrowseTag(Object):
    def __init__(
        self,
        opcServer=None,  # type: Optional[str]
        type_=None,  # type: Optional[BrowseElementType]
        displayName=None,  # type: Optional[str]
        displayPath=None,  # type: Optional[str]
        dataType=None,  # type: Optional[Class]
        opcItemPath=None,  # type: Optional[str]
    ):
        # type: (...) -> None
        super(OPCBrowseTag, self).__init__()
        self.opcServer = opcServer
        self.type = type_
        self.displayName = displayName
        self.displayPath = displayPath
        self.dataType = dataType
        self.opcItemPath = opcItemPath

    def getDataType(self):
        return self.dataType

    def getDisplayName(self):
        return self.displayName

    def getDisplayPath(self):
        return self.displayPath

    def getOpcItemPath(self):
        return self.opcItemPath

    def getOpcServer(self):
        return self.opcServer

    def getType(self):
        return self.type


class TagAlarmDefinition(Object):
    def __init__(self, alarm, alarmProperties):
        # type: (String, List[TagAlarmProperty]) -> None
        self.alarm = alarm
        self.alarmProperties = alarmProperties

    def getAlarmProperties(self):
        print(self)
        return TagAlarmProperty("property", "type", Object())


class TagAlarmProperty(Object):
    def __init__(self, property, type, value):
        # type: (String, String, Object) -> None
        self.property = property
        self.type = type
        self.value = value
