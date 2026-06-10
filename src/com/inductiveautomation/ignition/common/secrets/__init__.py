from __future__ import print_function

from typing import Union

from java.lang import Record

from com.inductiveautomation.ignition.common.script.abc import ContextManager
from com.inductiveautomation.ignition.gateway.secrets import Plaintext


class PyPlaintext(ContextManager):
    def __init__(self, plaintext):
        # type: (Plaintext) -> None
        super(PyPlaintext, self).__init__()

    def clear(self):
        # type: () -> None
        pass

    def getSecretsAsBytes(self):
        # type: () -> bytearray
        pass

    def getSecretsAsString(self, charsetName=None):
        # type: (Union[str, unicode, None]) -> Union[str, unicode]
        pass


class SecretMeta(Record):
    def __init__(
        self,
        name,  # type: Union[str, unicode]
    ):
        # type: (...) -> None
        super(SecretMeta, self).__init__()
        self._name = name

    def name(self):
        # type: () -> Union[str, unicode]
        return self._name


class SecretProviderMeta(Record):
    def __init__(
        self,
        name,  # type: Union[str, unicode]
        description,  # type: Union[str, unicode]
        type_,  # type: Union[str, unicode]
    ):
        # type: (...) -> None
        super(SecretProviderMeta, self).__init__()
        self._name = name
        self._description = description
        self._type = type_

    def description(self):
        # type: () -> Union[str, unicode]
        return self._description

    def name(self):
        # type: () -> Union[str, unicode]
        return self._name

    def type(self):
        # type: () -> Union[str, unicode]
        return self._type
