from __future__ import print_function

__all__ = [
    "AbstractDateTime",
    "AbstractDuration",
    "AbstractInstant",
    "AbstractInterval",
    "AbstractPartial",
    "BaseDateTime",
    "BaseDuration",
    "BaseInterval",
    "BaseLocal",
    "BasePeriod",
    "BaseSingleFieldPeriod",
]


from typing import TYPE_CHECKING, Any, List, Optional, Union

from java.lang import Comparable, Object
from java.util import Calendar, Date, GregorianCalendar, Locale

if TYPE_CHECKING:
    from org.joda.time import (
        Chronology,
        DateTime,
        DateTimeField,
        DateTimeFieldType,
        DateTimeZone,
        Duration,
        DurationFieldType,
        Instant,
        Interval,
        MutableDateTime,
        MutableInterval,
        MutablePeriod,
        Period,
        PeriodType,
        ReadableDuration,
        ReadableInstant,
        ReadableInterval,
        ReadablePartial,
    )


class AbstractDuration(Object, Comparable):
    def compareTo(self, o):
        # type: (Any) -> int
        pass

    def getMillis(self):
        # type: () -> long
        pass

    def isEqual(self, duration):
        # type: (ReadableDuration) -> bool
        pass

    def isLongerThan(self, duration):
        # type: (ReadableDuration) -> bool
        pass

    def isShorterThan(self, duration):
        # type: (ReadableDuration) -> bool
        pass

    def toDuration(self):
        # type: () -> Duration
        pass

    def toPeriod(self):
        # type: () -> Period
        pass


class AbstractInstant(Object, Comparable):
    def compareTo(self, o):
        # type: (Any) -> int
        pass

    def get(self, arg):
        # type: (Union[DateTimeField, DateTimeFieldType]) -> int
        pass

    def getZone(self):
        # type: () -> DateTimeZone
        pass

    def isAfter(self, instant):
        # type: (Union[long, ReadableInstant]) -> bool
        pass

    def isAfterNow(self):
        # type: () -> bool
        pass

    def isBefore(self, instant):
        # type: (Union[long, ReadableInstant]) -> bool
        pass

    def isBeforeNow(self):
        # type: () -> bool
        pass

    def isEqual(self, instant):
        # type: (Union[long, ReadableInstant]) -> bool
        pass

    def isEqualNow(self):
        # type: () -> bool
        pass

    def isSupported(self, arg):
        # type: (DateTimeFieldType) -> bool
        pass

    def toDate(self):
        # type: () -> Date
        pass

    def toDateTimeISO(self):
        # type: () -> DateTime
        pass

    def toInstant(self):
        # type: () -> Instant
        pass

    def toMutableDateTime(
        self,
        arg=None,  # type: Union[Chronology, DateTimeZone, None]
    ):
        # type: (...) -> MutableDateTime
        pass

    def toMutableDateTimeISO(self):
        # type: () -> MutableDateTime
        pass


class AbstractInterval(Object):
    def contains(self, arg):
        # type: (Union[long, ReadableInstant, ReadableInterval]) -> bool
        pass

    def containsNow(self):
        # type: () -> bool
        pass

    def getEnd(self):
        # type: () -> DateTime
        pass

    def getStart(self):
        # type: () -> DateTime
        pass

    def isAfter(self, arg):
        # type: (Union[long, ReadableInstant, ReadableInterval]) -> bool
        pass

    def isAfterNow(self):
        # type: () -> bool
        pass

    def isBefore(self, arg):
        # type: (Union[long, ReadableInstant, ReadableInterval]) -> bool
        pass

    def isBeforeNow(self):
        # type: () -> bool
        pass

    def isEqual(self, other):
        # type: (ReadableInterval) -> bool
        pass

    def overlaps(self, interval):
        # type: (ReadableInterval) -> bool
        pass

    def toDuration(self):
        # type: () -> Duration
        pass

    def toDurationMillis(self):
        # type: () -> long
        pass

    def toInterval(self):
        # type: () -> Interval
        pass

    def toMutableInterval(self):
        # type: () -> MutableInterval
        pass

    def toPeriod(self, type_=None):
        # type: (Optional[PeriodType]) -> Period
        pass


class AbstractDateTime(AbstractInstant):
    def getCenturyOfEra(self):
        # type: () -> int
        pass

    def getDayOfMonth(self):
        # type: () -> int
        pass

    def getDayOfWeek(self):
        # type: () -> int
        pass

    def getDayOfYear(self):
        # type: () -> int
        pass

    def getEra(self):
        # type: () -> int
        pass

    def getHourOfDay(self):
        # type: () -> int
        pass

    def getMillisOfDay(self):
        # type: () -> int
        pass

    def getMillisOfSecond(self):
        # type: () -> int
        pass

    def getMinuteOfDay(self):
        # type: () -> int
        pass

    def getMinuteOfHour(self):
        # type: () -> int
        pass

    def getMonthOfYear(self):
        # type: () -> int
        pass

    def getSecondOfDay(self):
        # type: () -> int
        pass

    def getSecondOfMinute(self):
        # type: () -> int
        pass

    def getWeekOfWeekyear(self):
        # type: () -> int
        pass

    def getWeekyear(self):
        # type: () -> int
        pass

    def getYear(self):
        # type: () -> int
        pass

    def getYearOfCentury(self):
        # type: () -> int
        pass

    def getYearOfEra(self):
        # type: () -> int
        pass

    def toCalendar(self, locale):
        # type: (Locale) -> Calendar
        pass

    def toGregorianCalendar(self):
        # type: () -> GregorianCalendar
        pass


class AbstractPartial(Object, Comparable):
    def compareTo(self, o):
        # type: (Any) -> int
        pass

    def get(self, arg):
        # type: (Union[DateTimeField, DateTimeFieldType]) -> int
        pass

    def getChronology(self):
        # type: () -> Chronology
        pass

    def getField(self, index):
        # type: (int) -> DateTimeField
        pass

    def getFieldType(self, index):
        # type: (int) -> DateTimeFieldType
        pass

    def getFieldTypes(self):
        # type: () -> List[DateTimeFieldType]
        pass

    def getFields(self):
        # type: () -> List[DateTimeField]
        pass

    def getValue(self, index):
        # type: (int) -> int
        pass

    def getValues(self):
        # type: () -> List[int]
        pass

    def indexOf(self, type_):
        # type: (DateTimeFieldType) -> int
        pass

    def isAfter(self, partial):
        # type: (ReadablePartial) -> bool
        pass

    def isBefore(self, partial):
        # type: (ReadablePartial) -> bool
        pass

    def isEqual(self, partial):
        # type: (ReadablePartial) -> bool
        pass

    def isSupported(self, arg):
        # type: (DateTimeFieldType) -> bool
        pass

    def size(self):
        # type: () -> int
        pass

    def toDateTime(self, baseInstant):
        # type: (ReadableInstant) -> DateTime
        pass


class AbstractPeriod(Object):
    def get(self, arg):
        # type: (DurationFieldType) -> int
        pass

    def getFieldType(self, index):
        # type: (int) -> DurationFieldType
        pass

    def getFieldTypes(self):
        # type: () -> List[DurationFieldType]
        pass

    def getValues(self):
        # type: () -> List[int]
        pass

    def indexOf(self, type_):
        # type: (DurationFieldType) -> int
        pass

    def isSupported(self, type_):
        # type: (DurationFieldType) -> bool
        pass

    def size(self):
        # type: () -> int
        pass

    def toMutablePeriod(self):
        # type: () -> MutablePeriod
        pass

    def toPeriod(self):
        # type: () -> Period
        pass


class BaseDateTime(AbstractDateTime):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(BaseDateTime, self).__init__()
        print(args)

    def getChronology(self):
        # type: () -> Chronology
        pass

    def getMillis(self):
        # type: () -> long
        pass


class BaseDuration(AbstractDuration):
    def toIntervalFrom(self, startInstant):
        # type: (ReadableInstant) -> Interval
        pass

    def toIntervalTo(self, endInstant):
        # type: (ReadableInstant) -> Interval
        pass

    def toPeriodFrom(self, startInstant, type_=None):
        # type: (ReadableInstant, Optional[PeriodType]) -> Period
        pass

    def toPeriodTo(self, endInstant, type_=None):
        # type: (ReadableInstant, Optional[PeriodType]) -> Period
        pass


class BaseInterval(AbstractInterval):
    def getChronology(self):
        # type: () -> Chronology
        pass

    def getEndMillis(self):
        # type: () -> long
        pass

    def getStartMillis(self):
        # type: () -> long
        pass


class BaseLocal(AbstractPartial):
    pass


class BasePeriod(AbstractPeriod):
    def getPeriodType(self):
        # type: () -> PeriodType
        pass

    def getValue(self, index):
        # type: (int) -> int
        pass

    def toDurationFrom(self, startInstant):
        # type: (ReadableInstant) -> Duration
        pass

    def toDurationTo(self, endInstant):
        # type: (ReadableInstant) -> Duration
        pass


class BaseSingleFieldPeriod(Object, Comparable):
    def compareTo(self, o):
        # type: (Any) -> int
        pass

    def get(self, type_):
        # type: (DateTimeFieldType) -> int
        pass

    def getFieldType(self):
        # type: () -> DateTimeFieldType
        pass

    def getPeriodType(self):
        # type: () -> PeriodType
        pass

    def getValue(self, index):
        # type: (int) -> int
        pass

    def isSupported(self, type_):
        # type: (DateTimeFieldType) -> bool
        pass

    def size(self):
        # type: () -> int
        pass

    def toMutablePeriod(self):
        # type: () -> MutablePeriod
        pass

    def toPeriod(self):
        # type: () -> Period
        pass
