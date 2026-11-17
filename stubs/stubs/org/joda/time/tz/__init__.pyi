from typing import Iterable, Union

from java.util import Locale
from org.joda.time import DateTimeZone

class NameProvider:
    def getName(
        self, locale: Locale, id_: Union[str, unicode], nameKey: Union[str, unicode]
    ) -> Union[str, unicode]: ...
    def getShortName(
        self, locale: Locale, id_: Union[str, unicode], nameKey: Union[str, unicode]
    ) -> Union[str, unicode]: ...

class Provider:
    def getAvailableIDs(self) -> Iterable[Union[str, unicode]]: ...
    def getZone(self, id_: Union[str, unicode]) -> DateTimeZone: ...
