__all__ = ["NameProvider", "Provider"]

from typing import TYPE_CHECKING, Iterable, Union

from java.util import Locale

if TYPE_CHECKING:
    from org.joda.time import DateTimeZone


class NameProvider(object):
    def getName(
        self,
        locale,  # type: Locale
        id_,  # type: Union[str, unicode]
        nameKey,  # type: Union[str, unicode]
    ):
        # type: (...) -> Union[str, unicode]
        raise NotImplementedError

    def getShortName(
        self,
        locale,  # type: Locale
        id_,  # type: Union[str, unicode]
        nameKey,  # type: Union[str, unicode]
    ):
        # type: (...) -> Union[str, unicode]
        raise NotImplementedError


class Provider(object):
    def getAvailableIDs(self):
        # type: () -> Iterable[Union[str, unicode]]
        raise NotImplementedError

    def getZone(self, id_):
        # type: (Union[str, unicode]) -> DateTimeZone
        raise NotImplementedError
