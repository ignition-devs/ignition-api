from __future__ import print_function

__all__ = [
    "DateTimeFormatter",
    "DateTimeParser",
    "DateTimeParserBucket",
    "DateTimePrinter",
    "PeriodFormatter",
    "PeriodParser",
    "PeriodPrinter",
]

from typing import TYPE_CHECKING, Any, Optional, Union

from java.io import Writer
from java.lang import CharSequence, Object, String, StringBuffer
from java.util import Locale

if TYPE_CHECKING:
    from org.joda.time import (
        Chronology,
        DateTime,
        DateTimeZone,
        LocalDate,
        LocalDateTime,
        LocalTime,
        MutableDateTime,
        MutablePeriod,
        Period,
        PeriodType,
        ReadableInstant,
        ReadablePartial,
        ReadablePeriod,
        ReadWritableInstant,
        ReadWritablePeriod,
    )


class DateTimeParser(object):
    def estimatedsParsedLength(self):
        # type: () -> int
        raise NotImplementedError

    def parseInto(self, bucket, text, position):
        # type: (DateTimeParserBucket, Union[str, unicode], int) -> int
        raise NotImplementedError


class DateTimePrinter(object):
    def estimatedsPrintedLength(self):
        # type: () -> int
        raise NotImplementedError

    def printTo(self, *args):
        # type: (*Any) -> None
        raise NotImplementedError


class PeriodParser(object):

    def parseInto(
        self,
        period,  # type: ReadWritablePeriod
        periodStr,  # type: Union[str, unicode]
        position,  # type: int
        locale,  # type: Locale
    ):
        # type: (...) -> int
        raise NotImplementedError


class PeriodPrinter(object):
    def calculatePrintedLength(self, period, locale):
        # type: (ReadablePeriod, Locale) -> int
        raise NotImplementedError

    def countFieldsToPrint(self, period, stopAt, locale):
        # type: (ReadablePeriod, int, Locale) -> int
        raise NotImplementedError

    def printTo(self, *args):
        # type: (*Any) -> None
        raise NotImplementedError


class DateTimeFormatter(Object):
    def __init__(self, printer, parser):
        # type: (DateTimePrinter, DateTimeParser) -> None
        super(DateTimeFormatter, self).__init__()
        print(printer, parser)

    def getChronology(self):
        # type: () -> Chronology
        pass

    def getDefaultYear(self):
        # type: () -> int
        pass

    def getLocale(self):
        # type: () -> Locale
        pass

    def getParser(self):
        # type: () -> DateTimeParser
        pass

    def getPivotYear(self):
        # type: () -> int
        pass

    def getPrinter(self):
        # type: () -> DateTimePrinter
        pass

    def getZone(self):
        # type: () -> DateTimeZone
        pass

    def isOffsetParsed(self):
        # type: () -> bool
        pass

    def isParser(self):
        # type: () -> bool
        pass

    def isPrinter(self):
        # type: () -> bool
        pass

    def parseDateTime(self, text):
        # type: (Union[str, unicode]) -> DateTime
        pass

    def parseInto(self, instant, text, position):
        # type: (ReadWritableInstant, Union[str, unicode], int) -> int
        pass

    def parseLocalDate(self, text):
        # type: (Union[str, unicode]) -> LocalDate
        pass

    def parseLocalDateTime(self, text):
        # type: (Union[str, unicode]) -> LocalDateTime
        pass

    def parseLocalTime(self, text):
        # type: (Union[str, unicode]) -> LocalTime
        pass

    def parseMillis(self, text):
        # type: (Union[str, unicode]) -> long
        pass

    def parseMutableDateTime(self, text):
        # type: (Union[str, unicode]) -> MutableDateTime
        pass

    def print(
        self,
        arg,  # type: Union[long, ReadableInstant, ReadablePartial]
    ):
        # type: (...) -> Union[str, unicode]
        pass

    def printTo(self, *args):
        # type: (*Any) -> None
        pass

    def withChronology(self, chrono):
        # type: (Chronology) -> DateTimeFormatter
        pass

    def withDefaultYear(self, defaultYear):
        # type: (int) -> DateTimeFormatter
        pass

    def withLocale(self, locale):
        # type: (Locale) -> DateTimeFormatter
        pass

    def withOffsetParsed(self):
        # type: () -> DateTimeFormatter
        pass

    def withPivotYear(self, pivotYear):
        # type: (int) -> DateTimeFormatter
        pass

    def withZone(self, zone):
        # type: (DateTimeZone) -> DateTimeFormatter
        pass

    def withZoneUTC(self):
        # type: () -> DateTimeFormatter
        pass


class DateTimeParserBucket(Object):
    def __init__(
        self,
        instantLocal,  # type: long
        chrono,  # type: Chronology
        locale,  # type: Locale
        pivotYear,  # type: int
        defaultYear,  # type: int
    ):
        super(DateTimeParserBucket, self).__init__()
        print(instantLocal, chrono, locale, pivotYear, defaultYear)

    def computeMillis(
        self,
        resetFields=None,  # type: Optional[bool]
        text=None,  # type: Union[CharSequence, String, None]
    ):
        # type: (...) -> long
        pass

    def getChronology(self):
        # type: () -> Chronology
        pass

    def getLocale(self):
        # type: () -> Locale
        pass

    def getOffsetInteger(self):
        # type: () -> Optional[int]
        pass

    def getPivotYear(self):
        # type: () -> int
        pass

    def getZone(self):
        # type: () -> DateTimeZone
        pass

    def parseMillis(self, parser, text):
        # type: (DateTimeParser, CharSequence) -> long
        pass

    def reset(self):
        # type: () -> None
        pass

    def restoreState(self, savedState):
        # type: (Object) -> None
        pass

    def saveField(self, *args):
        # type: (*Any) -> None
        pass

    def saveState(self):
        # type: () -> Object
        pass

    def setOffset(self, offset):
        # type: (int) -> None
        pass

    def setZone(self, zone):
        # type: (DateTimeZone) -> None
        pass


class PeriodFormatter(Object):
    def __init__(self, printer, parser):
        # type: (PeriodPrinter, PeriodParser) -> None
        super(PeriodFormatter, self).__init__()
        print(printer, parser)

    def getLocale(self):
        # type: () -> Locale
        pass

    def getParser(self):
        # type: () -> PeriodParser
        pass

    def getParseType(self):
        # type: () -> PeriodType
        pass

    def getPrinter(self):
        # type: () -> PeriodPrinter
        pass

    def isParser(self):
        # type: () -> bool
        pass

    def isPrinter(self):
        # type: () -> bool
        pass

    def parseInto(self, period, text, position):
        # type: (ReadWritablePeriod, Union[str, unicode], int) -> int
        pass

    def parseMutablePeriod(self, text):
        # type: (Union[str, unicode]) -> MutablePeriod
        pass

    def parsePeriod(self, text):
        # type: (Union[str, unicode]) -> Period
        pass

    def print(self, period):
        # type: (ReadablePeriod) -> None
        pass

    def printTo(
        self,
        arg,  # type: Union[StringBuffer, Writer]
        period,  # type: ReadablePeriod
    ):
        # type: (...) -> PeriodFormatter
        pass

    def withLocale(self, locale):
        # type: (Locale) -> PeriodFormatter
        pass

    def withParseType(self, type_):
        # type: (Locale) -> PeriodType
        pass
