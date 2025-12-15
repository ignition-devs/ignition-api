from typing import Any

from java.lang import Class, Object, String


class Property(object):
    def getDefaultValue(self):
        # type: () -> Any
        raise NotImplementedError

    def getName(self):
        # type: () -> String
        raise NotImplementedError

    def getType(self):
        # type: () -> Class
        raise NotImplementedError


class BasicProperty(Property, Object):
    _name = None  # type: String
    _clazz = None  # type: Any
    _defaultValue = None  # type: Any
    _hcode = None  # type: int

    def __init__(self, *args):
        # type: (Any) -> None
        if not args:
            self._hcode = 0
        elif len(args) == 2:
            self._name = args[0]
            self._clazz = args[1]
        elif len(args) == 3:
            self._name = args[0]
            self._clazz = args[1]
            self._defaultValue = args[2]
        else:
            raise NotImplementedError

    def getClazz(self):
        # type: () -> Class
        pass

    def getDefaultValue(self):
        # type: () -> Any
        return self._defaultValue

    def getName(self):
        # type: () -> String
        return self._name

    def getType(self):
        # type: () -> Class
        pass

    def setClazz(self, clazz):
        # type: (Class) -> None
        pass

    def setClazz_(self, clazz):
        # type: (Class) -> BasicProperty
        pass

    def setDefaultValue(self, defaultValue):
        # type: (Any) -> None
        pass

    def setDefaultValue_(self, defaultValue):
        # type: (Any) -> BasicProperty
        pass

    def setName(self, name):
        # type: (String) -> None
        pass

    def setName_(self, name):
        # type: (String) -> BasicProperty
        pass
