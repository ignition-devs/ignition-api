from typing import Optional, Union

from java.io import Closeable
from java.lang import Exception, Object, Throwable
from java.nio.charset import Charset


class Plaintext(Object, Closeable):
    def __init__(self):
        # type: () -> None
        super(Plaintext, self).__init__()

    def clear(self):
        # type: () -> None
        pass

    def close(self):
        # type: () -> None
        pass

    @staticmethod
    def fromBytes(bytes):
        # type: (bytearray) -> Plaintext
        return Plaintext()

    @staticmethod
    def fromString(str, charset=None):
        # type: (Union[str, unicode], Optional[Charset]) -> Plaintext
        return Plaintext()

    def getAsString(self):
        # type: () -> Union[str, unicode]
        pass

    def getBytes(self):
        # type: () -> bytearray
        pass


class SecretException(Exception):
    def __init__(self, message, cause=None):
        # type: (str, Optional[Throwable]) -> None
        super(SecretException, self).__init__(message, cause)
