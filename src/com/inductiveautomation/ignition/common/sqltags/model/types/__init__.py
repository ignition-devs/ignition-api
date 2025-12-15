__all__ = ["DataQuality", "DataType", "TagType"]

from java.lang import Enum


class DataQuality(Enum):
    @staticmethod
    def fromIntValue(value):
        pass

    def getDescription(self):
        pass

    def getIntValue(self):
        pass

    def getLevel(self):
        pass

    def getName(self):
        pass

    @staticmethod
    def getQualityFor(arg):
        pass

    def isDataUsed(self):
        pass

    def isGood(self):
        pass

    def isGoodData(self):
        pass

    def isOPCBadData(self):
        pass

    @staticmethod
    def values():
        pass

    @staticmethod
    def worstOf(q1, q2):
        pass

    @staticmethod
    def worstOfAll(*args):
        pass


class DataType(Enum):
    def fromIntValue(self, val):
        pass

    def getComponentDataType(self):
        pass

    def getIntValue(self):
        pass

    def getJavaType(self):
        pass

    def getTypeClass(self):
        pass

    def getTypeForClass(self, clazz):
        pass

    def getTypeForValue(self, val):
        pass

    def isArray(self):
        pass

    def isFloatingPoint(self):
        pass

    def isNumeric(self):
        pass

    def legacyDataType(self):
        pass

    def values(self):
        pass


class TagType(Enum):
    def getBindableProperties(self, tag):
        pass

    def getCoreType(self):
        pass

    def getDefaultMeta(self):
        pass

    def getIntValue(self):
        pass

    def getSubType(self):
        pass

    def getTypeForValue(self, val):
        pass

    def getUUID(self):
        pass

    def hasSubTags(self):
        pass

    def isComplex(self):
        pass

    def supportsAlarming(self):
        pass

    def valueOfCaseInsensitive(self, name):
        pass

    def values(self):
        pass
