__all__ = ["UIResponse"]

from java.lang import Object
from java.util import Locale


class UIResponse(Object):
    def __init__(self, locale):
        # type: (Locale) -> None
        self.locale = locale

    def attempt(self, method):
        pass

    def error(self, message, args):
        pass

    def getErrors(self):
        pass

    def getInfos(self):
        pass

    def getLocale(self):
        pass

    def getWarns(self):
        pass

    def info(self, message, args):
        pass

    def warn(self, message, args):
        pass

    def wrap(self, locale, fx):
        pass
