from __future__ import print_function

__all__ = [
    "Chronology",
    "DateTime",
    "DateTimeField",
    "DateTimeFieldType",
    "DateTimeZone",
    "Days",
    "Duration",
    "DurationField",
    "DurationFieldType",
    "Hours",
    "Instant",
    "Interval",
    "LocalDate",
    "LocalDateTime",
    "LocalTime",
    "Minutes",
    "MutableDateTime",
    "MutableInterval",
    "MutablePeriod",
    "Period",
    "PeriodType",
    "ReadWritableInstant",
    "ReadWritablePeriod",
    "ReadableDuration",
    "ReadableInstant",
    "ReadableInterval",
    "ReadablePartial",
    "ReadablePeriod",
    "Seconds",
    "Weeks",
]

from typing import Any, List, Optional, Union

from java.lang import Comparable, Object
from java.math import RoundingMode
from java.util import Calendar, Date, Locale, TimeZone

from org.joda.time.base import (
    AbstractInstant,
    BaseDateTime,
    BaseDuration,
    BaseInterval,
    BaseLocal,
    BasePeriod,
    BaseSingleFieldPeriod,
)
from org.joda.time.field import AbstractReadableInstantFieldProperty
from org.joda.time.format import DateTimeFormatter, PeriodFormatter
from org.joda.time.tz import NameProvider, Provider


class ReadableInstant(Comparable):
    def compareTo(self, o):
        # type: (Any) -> int
        pass

    def equals(self, readableInstant):
        # type: (Object) -> bool
        pass

    def get(self, type_):
        # type: (DateTimeFieldType) -> int
        pass

    def getChronology(self):
        # type: () -> Chronology
        pass

    def getMillis(self):
        # type: () -> long
        pass

    def getZone(self):
        # type: () -> DateTimeZone
        pass

    def hashCode(self):
        # type: () -> int
        pass

    def isAfter(self, instant):
        # type: (Union[long, ReadableInstant]) -> bool
        pass

    def isBefore(self, instant):
        # type: (ReadableInstant) -> bool
        pass

    def isEqual(self, instant):
        # type: (ReadableInstant) -> bool
        pass

    def isSupported(self, field):
        # type: (DateTimeFieldType) -> bool
        pass

    def toInstant(self):
        # type: () -> Instant
        pass


class ReadableDateTime(ReadableInstant):
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

    def toDateTime(self):
        # type: () -> DateTime
        pass

    def toMutableDateTime(self):
        # type: () -> MutableDateTime
        pass


class ReadableDuration(Comparable):
    def compareTo(self, o):
        # type: (Any) -> int
        pass

    def equals(self, readableDuration):
        # type: (ReadableDuration) -> bool
        pass

    def getMillis(self):
        # type: () -> long
        pass

    def hashCode(self):
        # type: () -> int
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

    def toString(self):
        # type: () -> Union[str, unicode]
        pass


class ReadableInterval(object):
    def contains(self, instant):
        # type: (Union[ReadableInterval, ReadableInstant]) -> bool
        pass

    def equals(self, readableInterval):
        # type: (Object) -> bool
        pass

    def getChronology(self):
        # type: () -> Chronology
        pass

    def getEnd(self):
        # type: () -> DateTime
        pass

    def getEndMillis(self):
        # type: () -> long
        pass

    def getStart(self):
        # type: () -> DateTime
        pass

    def getStartMillis(self):
        # type: () -> long
        pass

    def hashCode(self):
        # type: () -> int
        pass

    def isAfter(self, instant):
        # type: (Union[ReadableInterval, ReadableInstant]) -> bool
        pass

    def isBefore(self, instant):
        # type: (Union[ReadableInterval, ReadableInstant]) -> bool
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

    def toString(self):
        # type: () -> Union[str, unicode]
        pass


class ReadablePartial(Comparable):
    def compareTo(self, o):
        # type: (Any) -> int
        pass

    def equals(self, partial):
        # type: (Object) -> bool
        pass

    def get(self, field):
        # type: (DateTimeFieldType) -> int
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

    def getValue(self):
        # type: () -> int
        pass

    def hashCode(self):
        # type: () -> int
        pass

    def isSupported(self, field):
        # type: (DateTimeFieldType) -> bool
        pass

    def size(self):
        # type: () -> int
        pass

    def toDateTime(self, baseInstant):
        # type: (ReadableInstant) -> DateTime
        pass

    def toString(self):
        # type: (*Any) -> Union[str, unicode]
        pass


class ReadablePeriod(object):
    def equals(self, readablePeriod):
        # type: (Object) -> bool
        pass

    def get(self, arg):
        # type: (DurationFieldType) -> int
        pass

    def getFieldType(self, index):
        # type: (int) -> DurationFieldType
        pass

    def getPeriodType(self):
        # type: () -> PeriodType
        pass

    def getValue(self, index):
        # type: (int) -> int
        pass

    def hashCode(self):
        # type: () -> int
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

    def toString(self):
        # type: () -> Union[str, unicode]
        pass


class ReadWritableInstant(ReadableInstant):
    def add(self, *args):
        # type: (*Any) -> None
        pass

    def set(self, type_, value):
        # type: (DateTimeFieldType, int) -> None
        pass

    def setChronology(self, chronology):
        # type: (Chronology) -> None
        pass

    def setMillis(self, instant):
        # type: (Union[ReadableInstant, long]) -> None
        pass

    def setZone(self, zone):
        # type: (DateTimeZone) -> None
        pass

    def setZoneRetainFields(self, zone):
        # type: (DateTimeZone) -> None
        pass


class ReadWritableDateTime(ReadableDateTime, ReadWritableInstant):
    def addDays(self, days):
        # type: (int) -> None
        pass

    def addHours(self, hours):
        # type: (int) -> None
        pass

    def addMillis(self, millis):
        # type: (int) -> None
        pass

    def addMinutes(self, minutes):
        # type: (int) -> None
        pass

    def addMonths(self, months):
        # type: (int) -> None
        pass

    def addSeconds(self, seconds):
        # type: (int) -> None
        pass

    def addWeeks(self, weeks):
        # type: (int) -> None
        pass

    def addWeekyears(self, weekyears):
        # type: (int) -> None
        pass

    def addYears(self, years):
        # type: (int) -> None
        pass

    def setDate(self, year, monthOfYear, dayOfMonth):
        # type: (int, int, int) -> None
        pass

    def setDateTime(
        self,
        year,  # type: int
        monthOfYear,  # type: int
        dayOfMonth,  # type: int
        hourOfDay,  # type: int
        minuteOfHour,  # type: int
        secondOfMinute,  # type: int
        millisOfSecond,  # type: int
    ):
        # type: (...) -> None
        pass

    def setDayOfMonth(self, dayOfMonth):
        # type: (int) -> None
        pass

    def setDayOfWeek(self, dayOfWeek):
        # type: (int) -> None
        pass

    def setDayOfYear(self, dayOfYear):
        # type: (int) -> None
        pass

    def setHourOfDay(self, hourOfDay):
        # type: (int) -> None
        pass

    def setMillisOfDay(self, millisOfDay):
        # type: (int) -> None
        pass

    def setMillisOfSecond(self, millisOfSecond):
        # type: (int) -> None
        pass

    def setMinuteOfDay(self, minuteOfDay):
        # type: (int) -> None
        pass

    def setMinuteOfHour(self, minuteOfHour):
        # type: (int) -> None
        pass

    def setMonthOfYear(self, monthOfYear):
        # type: (int) -> None
        pass

    def setSecondOfDay(self, secondOfDay):
        # type: (int) -> None
        pass

    def setSecondOfMinute(self, secondOfMinute):
        # type: (int) -> None
        pass

    def setTime(self, hour, minuteOfHour, secondOfMinute, millisOfSecond):
        # type: (int, int, int, int) -> None
        pass

    def setWeekOfWeekyear(self, weekOfWeekyear):
        # type: (int) -> None
        pass

    def setWeekyear(self, weekyear):
        # type: (int) -> None
        pass

    def setYear(self, year):
        # type: (int) -> None
        pass


class ReadWritablePeriod(ReadablePeriod):
    def add(self, *args):
        # type: (*Any) -> None
        pass

    def addDays(self, days):
        # type: (int) -> None
        pass

    def addHours(self, hours):
        # type: (int) -> None
        pass

    def addMillis(self, millis):
        # type: (int) -> None
        pass

    def addMinutes(self, minutes):
        # type: (int) -> None
        pass

    def addMonths(self, months):
        # type: (int) -> None
        pass

    def addSeconds(self, seconds):
        # type: (int) -> None
        pass

    def addWeeks(self, weeks):
        # type: (int) -> None
        pass

    def addYears(self, years):
        # type: (int) -> None
        pass

    def clear(self):
        # type: () -> None
        pass

    def set(self, field, value):
        # type: (DurationFieldType, int) -> None
        pass

    def setDays(self, days):
        # type: (int) -> None
        pass

    def setHours(self, hours):
        # type: (int) -> None
        pass

    def setMillis(self, millis):
        # type: (int) -> None
        pass

    def setMinutes(self, minutes):
        # type: (int) -> None
        pass

    def setPeriod(self, *args):
        # type: (*Any) -> None
        pass

    def setSeconds(self, seconds):
        # type: (int) -> None
        pass

    def setValue(self, index, value):
        # type: (int, int) -> None
        pass

    def setWeek(self, weeks):
        # type: (int) -> None
        pass

    def setYears(self, years):
        # type: (int) -> None
        pass


class Chronology(Object):
    def __init__(self):
        # type: () -> None
        super(Chronology, self).__init__()

    def add(self, *args):
        # type: (*Any) -> long
        pass

    def centuries(self):
        # type: () -> DurationField
        pass

    def centuryOfEra(self):
        # type: () -> DateTimeField
        pass

    def clockhourOfDay(self):
        # type: () -> DateTimeField
        pass

    def clockhourOfHalfday(self):
        # type: () -> DateTimeField
        pass

    def dayOfMonth(self):
        # type: () -> DateTimeField
        pass

    def dayOfWeek(self):
        # type: () -> DateTimeField
        pass

    def dayOfYear(self):
        # type: () -> DateTimeField
        pass

    def days(self):
        # type: () -> DateTimeField
        pass

    def era(self):
        # type: () -> DateTimeField
        pass

    def eras(self):
        # type: () -> DurationField
        pass

    def get(self, *args):
        # type: (*Any) -> Any
        pass

    def getDateTimeMillis(self, *args):
        # type: (*Any) -> long
        pass

    def getZone(self):
        # type: () -> DateTimeZone
        pass

    def halfdayOfDay(self):
        # type: () -> DateTimeField
        pass

    def halfdays(self):
        # type: () -> DurationField
        pass

    def hourOfDay(self):
        # type: () -> DateTimeField
        pass

    def hours(self):
        # type: () -> DurationField
        pass

    def millis(self):
        # type: () -> DurationField
        pass

    def millisOfDay(self):
        # type: () -> DateTimeField
        pass

    def millisOfSecond(self):
        # type: () -> DateTimeField
        pass

    def minuteOfDay(self):
        # type: () -> DateTimeField
        pass

    def minuteOfHour(self):
        # type: () -> DateTimeField
        pass

    def minutes(self):
        # type: () -> DurationField
        pass

    def monthOfYear(self):
        # type: () -> DateTimeField
        pass

    def months(self):
        # type: () -> DurationField
        pass

    def secondOfDay(self):
        # type: () -> DateTimeField
        pass

    def secondOfMinute(self):
        # type: () -> DateTimeField
        pass

    def seconds(self):
        # type: () -> DurationField
        pass

    def set(self, partial, instant):
        # type: (ReadablePartial, long) -> long
        pass

    def validate(self, partial, values):
        # type: (ReadablePartial, List[int]) -> None
        pass

    def wekOfWeekyear(self):
        # type: () -> DateTimeField
        pass

    def weeks(self):
        # type: () -> DurationField
        pass

    def weekyear(self):
        # type: () -> DateTimeField
        pass

    def weekyearOfCentury(self):
        # type: () -> DateTimeField
        pass

    def weekyears(self):
        # type: () -> DurationField
        pass

    def withUTC(self):
        # type: () -> Chronology
        pass

    def withZone(self, zone):
        # type: (DateTimeZone) -> Chronology
        pass

    def year(self):
        # type: () -> DateTimeField
        pass

    def yearOfCentury(self):
        # type: () -> DateTimeField
        pass

    def yearOfEra(self):
        # type: () -> DateTimeField
        pass

    def years(self):
        # type: () -> DurationField
        pass


class DateTime(BaseDateTime):
    class Property(AbstractReadableInstantFieldProperty):
        def addToCopy(self, value):
            # type: (Union[float, int, long]) -> DateTime
            pass

        def addWrapFieldToCopy(self, value):
            # type: (int) -> DateTime
            pass

        def getLocalDate(self):
            # type: () -> LocalDate
            pass

        def roundCeilingCopy(self):
            # type: () -> DateTime
            pass

        def roundFloorCopy(self):
            # type: () -> DateTime
            pass

        def roundHalfCeilingCopy(self):
            # type: () -> DateTime
            pass

        def roundHalfEvenCopy(self):
            # type: () -> DateTime
            pass

        def roundHalfFloorCopy(self):
            # type: () -> DateTime
            pass

        def setCopy(self, *args):
            # type: (*Any) -> DateTime
            pass

        def withMaximumValue(self):
            # type: () -> DateTime
            pass

        def withMinimumValue(self):
            # type: () -> DateTime
            pass

    def __init__(self, *args):
        # type: (*Any) -> None
        super(DateTime, self).__init__()
        print(args)

    def centuryOfEra(self):
        # type: () -> DateTime.Property
        pass

    def dayOfMonth(self):
        # type: () -> DateTime.Property
        pass

    def dayOfWeek(self):
        # type: () -> DateTime.Property
        pass

    def dayOfYear(self):
        # type: () -> DateTime.Property
        pass

    def era(self):
        # type: () -> DateTime.Property
        pass

    def hourOfDay(self):
        # type: () -> DateTime.Property
        pass

    def millisOfDay(self):
        # type: () -> DateTime.Property
        pass

    def millisOfSecond(self):
        # type: () -> DateTime.Property
        pass

    def minus(
        self,
        arg,  # type: Union[long, ReadableDuration, ReadablePeriod]
    ):
        # type: (...) -> DateTime
        pass

    def minusDays(self, days):
        # type: (int) -> DateTime
        pass

    def minusHours(self, hours):
        # type: (int) -> DateTime
        pass

    def minusMillis(self, millis):
        # type: (int) -> DateTime
        pass

    def minusMinutes(self, minutes):
        # type: (int) -> DateTime
        pass

    def minusMonths(self, months):
        # type: (int) -> DateTime
        pass

    def minusSeconds(self, seconds):
        # type: (int) -> DateTime
        pass

    def minusWeeks(self, weeks):
        # type: (int) -> DateTime
        pass

    def minusYears(self, years):
        # type: (int) -> DateTime
        pass

    def minuteOfDay(self):
        # type: () -> DateTime.Property
        pass

    def minuteOfHour(self):
        # type: () -> DateTime.Property
        pass

    def monthOfYear(self):
        # type: () -> DateTime.Property
        pass

    @staticmethod
    def now(arg=None):
        # type: (Union[Chronology, DateTimeZone, None]) -> DateTime
        pass

    @staticmethod
    def parse(
        str_,  # type: Union[str, unicode]
        formatter=None,  # type: Optional[DateTimeFormatter]
    ):
        # type: (...) -> DateTime
        pass

    def plus(
        self,
        arg,  # type: Union[long, ReadableDuration, ReadablePeriod]
    ):
        # type: (...) -> DateTime
        pass

    def plusDays(self, days):
        # type: (int) -> DateTime
        pass

    def plusHours(self, hours):
        # type: (int) -> DateTime
        pass

    def plusMillis(self, millis):
        # type: (int) -> DateTime
        pass

    def plusMinutes(self, minutes):
        # type: (int) -> DateTime
        pass

    def plusMonths(self, months):
        # type: (int) -> DateTime
        pass

    def plusSeconds(self, seconds):
        # type: (int) -> DateTime
        pass

    def plusWeeks(self, weeks):
        # type: (int) -> DateTime
        pass

    def plusYears(self, years):
        # type: (int) -> DateTime
        pass

    def property(self, type_):
        # type: (DateTimeFieldType) -> DateTime.Property
        pass

    def secondOfDay(self):
        # type: () -> DateTime.Property
        pass

    def secondOfMinute(self):
        # type: () -> DateTime.Property
        pass

    def toLocalDate(self):
        # type: () -> LocalDate
        pass

    def toLocalDateTime(self):
        # type: () -> LocalDateTime
        pass

    def toLocalTime(self):
        # type: () -> LocalTime
        pass

    def weekOfWeekyear(self):
        # type: () -> DateTime.Property
        pass

    def weekyear(self):
        # type: () -> DateTime.Property
        pass

    def withCenturyOfEra(self, centuryOfEra):
        # type: (int) -> DateTime
        pass

    def withChronology(self, newChronology):
        # type: (Chronology) -> DateTime
        pass

    def withDate(self, *args):
        # type: (*Any) -> DateTime
        pass

    def withDayOfMonth(self, dayOfMonth):
        # type: (int) -> DateTime
        pass

    def withDayOfWeek(self, dayOfWeek):
        # type: (int) -> DateTime
        pass

    def withDayOfYear(self, dayOfYear):
        # type: (int) -> DateTime
        pass

    def withDurationAdded(self, durationToAdd, scalar):
        # type: (Union[long, ReadableDuration], int) -> DateTime
        pass

    def withEarlierOffsetAtOverlap(self):
        # type: () -> DateTime
        pass

    def withEra(self, era):
        # type: (int) -> DateTime
        pass

    def withField(self, fieldType, value):
        # type: (DateTimeFieldType, int) -> DateTime
        pass

    def withFieldAdded(self, fieldType, amount):
        # type: (DateTimeFieldType, int) -> DateTime
        pass

    def withFields(self, partial):
        # type: (ReadablePartial) -> DateTime
        pass

    def withHourOfDay(self, hour):
        # type: (int) -> DateTime
        pass

    def withLaterOffsetAtOverlap(self):
        # type: () -> DateTime
        pass

    def withMillis(self, newMillis):
        # type: (long) -> DateTime
        pass

    def withMillisOfDay(self, millis):
        # type: (int) -> DateTime
        pass

    def withMillisOfSecond(self, millis):
        # type: (int) -> DateTime
        pass

    def withMinuteOfHour(self, minute):
        # type: (int) -> DateTime
        pass

    def withMonthOfYear(self, month):
        # type: (int) -> DateTime
        pass

    def withPeriodAdded(self, periodToAdd, scalar):
        # type: (ReadablePeriod, int) -> DateTime
        pass

    def withSecondOfMinute(self, second):
        # type: (int) -> DateTime
        pass

    def withTime(self, *args):
        # type: (*Any) -> DateTime
        pass

    def withTimeAtStartOfDay(self):
        # type: () -> DateTime
        pass

    def withWeekOfWeekyear(self, weekOfWeekyear):
        # type: (int) -> DateTime
        pass

    def withWeekyear(self, weekyear):
        # type: (int) -> DateTime
        pass

    def withYear(self, year):
        # type: (int) -> DateTime
        pass

    def withYearOfCentury(self, yearOfCentury):
        # type: (int) -> DateTime
        pass

    def withYearOfEra(self, yearOfEra):
        # type: (int) -> DateTime
        pass

    def withZone(self, newZone):
        # type: (DateTimeZone) -> DateTime
        pass

    def withZoneRetainFields(self, newZone):
        # type: (DateTimeZone) -> DateTime
        pass

    def year(self):
        # type: () -> DateTime.Property
        pass

    def yearOfCentury(self):
        # type: () -> DateTime.Property
        pass

    def yearOfEra(self):
        # type: () -> DateTime.Property
        pass


class DateTimeField(Object):
    def __init__(self):
        # type: () -> None
        super(DateTimeField, self).__init__()

    def add(self, *args):
        # type: (*Any) -> Union[long, List[int]]
        pass

    def addWrapField(self, *args):
        # type: (*Any) -> Union[long, List[int]]
        pass

    def addWrapPartial(self, instant, fieldIndex, values, valueToAdd):
        # type: (ReadablePartial, int, List[int], int) -> List[int]
        pass

    def get(self, instant):
        # type: (long) -> int
        pass

    def getAsShortText(self, *args):
        # type: (*Any) -> Union[str, unicode]
        pass

    def getAsText(self, *args):
        # type: (*Any) -> Union[str, unicode]
        pass

    def getDifference(self, minuendInstant, subtrahendInstant):
        # type: (long, long) -> int
        pass

    def getDurationField(self):
        # type: () -> DurationField
        pass

    def getLeapAmount(self, instant):
        # type: (long) -> int
        pass

    def getLeapDurationField(self):
        # type: () -> DurationField
        pass

    def getMaximumShortTextLength(self, locale):
        # type: (Locale) -> int
        pass

    def getMaximumTextLength(self, locale):
        # type: (Locale) -> int
        pass

    def getMaximumValue(self, *args):
        # type: (*Any) -> int
        pass

    def getMinimumValue(self, *args):
        # type: (*Any) -> int
        pass

    def getName(self):
        # type: () -> Union[str, unicode]
        pass

    def getRangeDurationField(self):
        # type: () -> DurationField
        pass

    def getType(self):
        # type: () -> DateTimeFieldType
        pass

    def isLeap(self, instant):
        # type: (long) -> bool
        pass

    def isLenient(self):
        # type: () -> bool
        pass

    def isSupported(self):
        # type: () -> bool
        pass

    def remainder(self, instant):
        # type: (long) -> long
        pass

    def roundCeiling(self, instant):
        # type: (long) -> long
        pass

    def roundFloor(self, instant):
        # type: (long) -> long
        pass

    def roundHalfCeiling(self, instant):
        # type: (long) -> long
        pass

    def roundHalfEven(self, instant):
        # type: (long) -> long
        pass

    def roundHalfFloor(self, instant):
        # type: (long) -> long
        pass

    def set(self, *args):
        # type: (*Any) -> Union[long, List[int]]
        pass

    def setExtended(self, instant, value):
        # type: (long, int) -> long
        pass


class DateTimeFieldType(Object):
    @staticmethod
    def centuryOfEra():
        # type: () -> DateTimeFieldType
        pass

    @staticmethod
    def clockhourOfDay():
        # type: () -> DateTimeFieldType
        pass

    @staticmethod
    def clockhourOfHalfday():
        # type: () -> DateTimeFieldType
        pass

    @staticmethod
    def dayOfMonth():
        # type: () -> DateTimeFieldType
        pass

    @staticmethod
    def dayOfWeek():
        # type: () -> DateTimeFieldType
        pass

    @staticmethod
    def dayOfYear():
        # type: () -> DateTimeFieldType
        pass

    @staticmethod
    def era():
        # type: () -> DateTimeFieldType
        pass

    def getDurationType(self):
        # type: () -> DurationFieldType
        pass

    @staticmethod
    def halfdayOfDay():
        # type: () -> DateTimeFieldType
        pass

    @staticmethod
    def hourOfDay():
        # type: () -> DateTimeFieldType
        pass

    @staticmethod
    def hourOfHalfday():
        # type: () -> DateTimeFieldType
        pass

    def isSupported(self, chronology):
        # type: (Chronology) -> bool
        return True

    @staticmethod
    def millisOfDay():
        # type: () -> DateTimeFieldType
        pass

    @staticmethod
    def millisOfSecond():
        # type: () -> DateTimeFieldType
        pass

    @staticmethod
    def minuteOfDay():
        # type: () -> DateTimeFieldType
        pass

    @staticmethod
    def minuteOfHour():
        # type: () -> DateTimeFieldType
        pass

    @staticmethod
    def monthOfYear():
        # type: () -> DateTimeFieldType
        pass

    @staticmethod
    def secondOfDay():
        # type: () -> DateTimeFieldType
        pass

    @staticmethod
    def secondOfMinute():
        # type: () -> DateTimeFieldType
        pass

    @staticmethod
    def weekOfWeekyear():
        # type: () -> DateTimeFieldType
        pass

    @staticmethod
    def weekyear():
        # type: () -> DateTimeFieldType
        pass

    @staticmethod
    def weekyearOfCentury():
        # type: () -> DateTimeFieldType
        pass

    @staticmethod
    def year():
        # type: () -> DateTimeFieldType
        pass

    @staticmethod
    def yearOfCentury():
        # type: () -> DateTimeFieldType
        pass

    @staticmethod
    def yearOfEra():
        # type: () -> DateTimeFieldType
        pass


class DateTimeZone(Object):
    DEFAULT_TZ_DATA_PATH = None  # type: Union[str, unicode]
    UTC = None  # type: DateTimeZone

    def adjustOffset(self, instant, earlierOrLater):
        # type: (long, bool) -> long
        pass

    def convertLocalToUTC(
        self,
        instantLocal,  # type: long
        strict=False,  # type: bool
        originalInstantUTC=None,  # type: Optional[long]
    ):
        # type: (...) -> long
        pass

    @staticmethod
    def forID(id_):
        # type: (Union[str, unicode]) -> DateTimeZone
        pass

    @staticmethod
    def forOffsetHours(hoursOffset):
        # type: (int) -> DateTimeZone
        pass

    @staticmethod
    def forOffsetHoursMinutes(hoursOffset, minutesOffset):
        # type: (int, int) -> DateTimeZone
        pass

    @staticmethod
    def forOffsetMillis(millisOffset):
        # type: (int) -> DateTimeZone
        pass

    @staticmethod
    def forTimeZOne(zone):
        # type: (TimeZone) -> DateTimeZone
        pass

    @staticmethod
    def getAvailableIDs():
        # type: () -> List[Union[str, unicode]]
        pass

    @staticmethod
    def getDefault():
        # type: () -> DateTimeZone
        pass

    def getID(self):
        # type: () -> Union[str, unicode]
        pass

    def getMillisKeepLocal(self, newZone, oldInstant):
        # type: (DateTimeZone, long) -> long
        pass

    def getName(self, instant):
        # type: (long) -> Union[str, unicode]
        pass

    def getNameKey(self, instant):
        # type: (long) -> Union[str, unicode]
        pass

    @staticmethod
    def getNameProvider():
        # type: () -> NameProvider
        pass

    def getOffset(self, instant):
        # type: (long) -> int
        pass

    def getOffsetFromLocal(self, instantLocal):
        # type: (long) -> int
        pass

    @staticmethod
    def getProvider():
        # type: () -> Provider
        pass

    def getShortName(self, instant, locale=None):
        # type: (long, Optional[Locale]) -> Union[str, unicode]
        pass

    def getStandardOffset(self, instant):
        # type: (long) -> int
        pass

    def isFixed(self):
        # type: () -> bool
        pass

    def isLocalDateTimeGap(self, localDateTime):
        # type: (LocalDateTime) -> bool
        pass

    def isStandardOffset(self, instant):
        # type: (long) -> bool
        pass

    def nextTransition(self, instant):
        # type: (long) -> long
        pass

    def previousTransition(self, instant):
        # type: (long) -> long
        pass

    @staticmethod
    def setDefault(zone):
        # type: (DateTimeZone) -> None
        pass

    @staticmethod
    def setNameProvider(nameProvider):
        # type: (NameProvider) -> None
        pass

    @staticmethod
    def setProvider(provider):
        # type: (Provider) -> None
        pass

    def toTimeZone(self):
        # type: () -> TimeZone
        pass


class Days(BaseSingleFieldPeriod):
    FIVE = None  # type: Days
    FOUR = None  # type: Days
    MAX_VALUE = None  # type: Days
    MIN_VALUE = None  # type: Days
    ONE = None  # type: Days
    SEVEN = None  # type: Days
    SIX = None  # type: Days
    THREE = None  # type: Days
    TWO = None  # type: Days
    ZERO = None  # type: Days

    @staticmethod
    def days(days):
        # type: (int) -> Days
        pass

    @staticmethod
    def daysBetwwen(
        start,  # type: Union[ReadableInstant, ReadablePartial]
        end,  # type: Union[ReadableInstant, ReadablePartial]
    ):
        # type: (...) -> Days
        pass

    @staticmethod
    def daysIn(interval):
        # type: (ReadableInterval) -> Days
        pass

    def dividedBy(self, divisor):
        # type: (int) -> Days
        pass

    def getDays(self):
        # type: () -> int
        pass

    def isGreaterThan(self, other):
        # type: (Days) -> bool
        pass

    def isLessThan(self, other):
        # type: (Days) -> bool
        pass

    def minus(self, days):
        # type: (Union[Days, int]) -> Days
        pass

    def multipliedBy(self, scalar):
        # type: (int) -> Days
        pass

    def negated(self):
        # type: () -> Days
        pass

    @staticmethod
    def parseDays(periodStr):
        # type: (Union[str, unicode]) -> Days
        pass

    def plus(self, days):
        # type: (Union[Days, int]) -> Days
        pass

    @staticmethod
    def standardDaysIn(period):
        # type: (ReadablePeriod) -> Days
        pass

    def toStandardDuration(self):
        # type: () -> Duration
        pass

    def toStandardHours(self):
        # type: () -> Hours
        pass

    def toStandardMinutes(self):
        # type: () -> Minutes
        pass

    def toStandardSeconds(self):
        # type: () -> Seconds
        pass

    def toStandardWeeks(self):
        # type: () -> Weeks
        pass


class Duration(BaseDuration):
    ZERO = None  # type: Duration

    def __init__(self, *args):
        # type: (*Any) -> None
        super(Duration, self).__init__()
        print(args)

    def abs(self):
        # type: () -> Duration
        pass

    def dividedBy(self, divisor, roundingMode=None):
        # type: (long, Optional[RoundingMode]) -> Duration
        pass

    def getStandardDays(self):
        # type: () -> int
        pass

    def getStandardHours(self):
        # type: () -> int
        pass

    def getStandardMinutes(self):
        # type: () -> int
        pass

    def getStandardSeconds(self):
        # type: () -> int
        pass

    @staticmethod
    def millis(millis):
        # type: (long) -> Duration
        pass

    def minus(self, amount):
        # type: (Union[long, ReadableDuration]) -> Duration
        pass

    def multipliedBy(self, multiplicand):
        # type: (long) -> Duration
        pass

    def negated(self):
        # type: () -> Duration
        pass

    @staticmethod
    def parse(str_):
        # type: (Union[str, unicode]) -> Duration
        pass

    def plus(self, amount):
        # type: (Union[long, ReadableDuration]) -> Duration
        pass

    @staticmethod
    def standardDays(days):
        # type: (long) -> Duration
        pass

    @staticmethod
    def standardHours(hours):
        # type: (long) -> Duration
        pass

    @staticmethod
    def standardMinutes(minutes):
        # type: (long) -> Duration
        pass

    @staticmethod
    def standardSeconds(seconds):
        # type: (long) -> Duration
        pass

    def toStandardDays(self):
        # type: () -> Days
        pass

    def toStandardHours(self):
        # type: () -> Hours
        pass

    def toStandardMinutes(self):
        # type: () -> Minutes
        pass

    def toStandardSeconds(self):
        # type: () -> Seconds
        pass

    def withDurationAdded(self, durationToAdd, scalar):
        # type: (Union[long, ReadableDuration], int) -> Duration
        pass

    def withMillis(self, duration):
        # type: (long) -> Duration
        pass


class DurationField(Object):
    def __init__(self):
        # type: () -> None
        super(DurationField, self).__init__()

    def add(
        self,
        instant,  # type: Union[float, int, long]
        value,  # type: Union[float, int, long]
    ):
        # type: (...) -> long
        pass

    def getDifference(self, minuendInstant, subtrahendInstant):
        # type: (long, long) -> int
        pass

    def getDifferenceAsLong(self, minuendInstant, subtrahendInstant):
        # type: (long, long) -> long
        pass

    def getMillis(self, *args):
        # type: (*Union[float, int, long]) -> long
        pass

    def getName(self):
        # type: () -> Union[str, unicode]
        pass

    def getType(self):
        # type: () -> DurationFieldType
        pass

    def getUnitMillis(self):
        # type: () -> long
        pass

    def isPrecise(self):
        # type: () -> bool
        pass

    def isSupported(self):
        # type: () -> bool
        pass

    def subtract(
        self,
        instant,  # type: Union[float, int, long]
        value,  # type: Union[float, int, long]
    ):
        # type: (...) -> long
        pass


class DurationFieldType(Object):
    @staticmethod
    def centuries():
        # type: () -> DurationFieldType
        pass

    @staticmethod
    def days():
        # type: () -> DurationFieldType
        pass

    @staticmethod
    def eras():
        # type: () -> DurationFieldType
        pass

    @staticmethod
    def getField(chronology):
        # type: (Chronology) -> DurationField
        pass

    def getName(self):
        # type: () -> Union[str, unicode]
        pass

    @staticmethod
    def halfdays():
        # type: () -> DurationFieldType
        pass

    @staticmethod
    def hours():
        # type: () -> DurationFieldType
        pass

    def isSupported(self, chronology):
        # type: (Chronology) -> bool
        pass

    @staticmethod
    def millis():
        # type: () -> DurationFieldType
        pass

    @staticmethod
    def minutes():
        # type: () -> DurationFieldType
        pass

    @staticmethod
    def months():
        # type: () -> DurationFieldType
        pass

    @staticmethod
    def seconds():
        # type: () -> DurationFieldType
        pass

    @staticmethod
    def weeks():
        # type: () -> DurationFieldType
        pass

    @staticmethod
    def weekyears():
        # type: () -> DurationFieldType
        pass

    @staticmethod
    def years():
        # type: () -> DurationFieldType
        pass


class Hours(BaseSingleFieldPeriod):
    EIGHT = None  # type: Hours
    FIVE = None  # type: Hours
    FOUR = None  # type: Hours
    MAX_VALUE = None  # type: Hours
    MIN_VALUE = None  # type: Hours
    ONE = None  # type: Hours
    SEVEN = None  # type: Hours
    SIX = None  # type: Hours
    THREE = None  # type: Hours
    TWO = None  # type: Hours
    ZERO = None  # type: Hours

    def dividedBy(self, divisor):
        # type: (int) -> Hours
        pass

    def getHours(self):
        # type: () -> int
        pass

    @staticmethod
    def hours(hours):
        # type: (int) -> Hours
        pass

    @staticmethod
    def hoursBetween(
        start,  # type: Union[ReadableInstant, ReadablePartial]
        end,  # type: Union[ReadableInstant, ReadablePartial]
    ):
        # type: (...) -> Hours
        pass

    @staticmethod
    def hoursIn(interval):
        # type: (ReadableInterval) -> Hours
        pass

    def isGreaterThan(self, other):
        # type: (Hours) -> bool
        pass

    def isLessThan(self, other):
        # type: (Hours) -> bool
        pass

    def minus(self, hours):
        # type: (Union[Hours, int]) -> Hours
        pass

    def multipliedBy(self, scalar):
        # type: (int) -> Hours
        pass

    def negated(self):
        # type: () -> Hours
        pass

    @staticmethod
    def parseHours(periodStr):
        # type: (Union[str, unicode]) -> Hours
        pass

    def plus(self, hours):
        # type: (Union[Hours, int]) -> Hours
        pass

    @staticmethod
    def standardHoursIn(period):
        # type: (ReadablePeriod) -> Hours
        pass

    def toStandardDays(self):
        # type: () -> Days
        pass

    def toStandardDuration(self):
        # type: () -> Duration
        pass

    def toStandardMinutes(self):
        # type: () -> Minutes
        pass

    def toStandardSeconds(self):
        # type: () -> Seconds
        pass

    def toStandardWeeks(self):
        # type: () -> Weeks
        pass


class Instant(AbstractInstant):
    def __init__(self, instant=None):
        # type: (Union[long, Object, None]) -> None
        super(Instant, self).__init__()
        print(instant)

    def getChronology(self):
        # type: () -> Chronology
        pass

    def getMillis(self):
        # type: () -> long
        pass

    def minus(self, duration):
        # type: (Union[long, ReadableDuration]) -> Instant
        pass

    @staticmethod
    def now():
        # type: () -> Instant
        pass

    @staticmethod
    def ofEpochMilli(epochMilli):
        # type: (long) -> Instant
        pass

    @staticmethod
    def ofEpochSecond(epochSecond):
        # type: (long) -> Instant
        pass

    @staticmethod
    def parse(
        str_,  # type: Union[str, unicode]
        formatter=None,  # type: Optional[DateTimeFormatter]
    ):
        # type: (...) -> Instant
        pass

    def plus(self, duration):
        # type: (Union[long, ReadableDuration]) -> Instant
        pass

    def withDurationAdded(self, durationToAdd, scalar):
        # type: (Union[long, ReadableDuration], int) -> Instant
        pass

    def withMillis(self, newMillis):
        # type: (long) -> Instant
        pass


class Interval(BaseInterval):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(Interval, self).__init__()
        print(args)

    def abuts(self, interval):
        # type: (ReadableInterval) -> bool
        pass

    def gap(self, interval):
        # type: (ReadableInterval) -> Interval
        pass

    def overlap(self, interval):
        # type: (ReadableInterval) -> bool
        pass

    @staticmethod
    def parse(str_):
        # type: (Union[str, unicode]) -> Interval
        pass

    @staticmethod
    def parseWithOffset(str_):
        # type: (Union[str, unicode]) -> Interval
        pass

    def withChronology(self, chronology):
        # type: (Chronology) -> Interval
        pass

    def withDurationAfterStart(self, duration):
        # type: (ReadableDuration) -> Interval
        pass

    def withDurationBeforeEnd(self, duration):
        # type: (ReadableDuration) -> Interval
        pass

    def withEnd(self, end):
        # type: (ReadableInstant) -> Interval
        pass

    def withEndMillis(self, endInstant):
        # type: (ReadableInstant) -> Interval
        pass

    def withPeriodAfterStart(self, period):
        # type: (ReadablePeriod) -> Interval
        pass

    def withPeriodBeforeEnd(self, period):
        # type: (ReadablePeriod) -> Interval
        pass

    def withStart(self, start):
        # type: (ReadableInstant) -> Interval
        pass

    def withStartMillis(self, startInstant):
        # type: (ReadableInstant) -> Interval
        pass


class LocalDate(BaseLocal):
    class Property(AbstractReadableInstantFieldProperty):
        def addToCopy(self, value):
            # type: (Union[float, int, long]) -> LocalDate
            pass

        def addWrapFieldToCopy(self, value):
            # type: (int) -> LocalDate
            pass

        def roundCeilingCopy(self):
            # type: () -> LocalDate
            pass

        def roundFloorCopy(self):
            # type: () -> LocalDate
            pass

        def roundHalfCeilingCopy(self):
            # type: () -> LocalDate
            pass

        def roundHalfEvenCopy(self):
            # type: () -> LocalDate
            pass

        def roundHalfFloorCopy(self):
            # type: () -> LocalDate
            pass

        def setCopy(self, *args):
            # type: (*Any) -> LocalDate
            pass

        def withMaximumValue(self):
            # type: () -> LocalDate
            pass

        def withMinimumValue(self):
            # type: () -> LocalDate
            pass

    def __init__(self, *args):
        # type: (*Any) -> None
        super(LocalDate, self).__init__()
        print(args)

    def centuryOfEra(self):
        # type: () -> LocalDate.Property
        pass

    def dayOfMonth(self):
        # type: () -> LocalDate.Property
        pass

    def dayOfWeek(self):
        # type: () -> LocalDate.Property
        pass

    def dayOfYear(self):
        # type: () -> LocalDate.Property
        pass

    def era(self):
        # type: () -> LocalDate.Property
        pass

    @staticmethod
    def fromCalendarFields(calendar):
        # type: (Calendar) -> LocalDate
        pass

    @staticmethod
    def fromDateFields(date):
        # type: (Date) -> LocalDate
        pass

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

    def getMonthOfYear(self):
        # type: () -> int
        pass

    def getWeekOfYear(self):
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

    def minus(self, period):
        # type: (ReadablePeriod) -> LocalDate
        pass

    def minusDays(self, days):
        # type: (int) -> LocalDate
        pass

    def minusMonths(self, months):
        # type: (int) -> LocalDate
        pass

    def minusWeeks(self, weeks):
        # type: (int) -> LocalDate
        pass

    def minusYears(self, years):
        # type: (int) -> LocalDate
        pass

    def monthOfYear(self):
        # type: () -> LocalDate.Property
        pass

    @staticmethod
    def now(arg=None):
        # type: (Union[Chronology, DateTimeZone, None]) -> LocalDate
        pass

    @staticmethod
    def parse(
        str_,  # type: Union[str, unicode]
        formatter=None,  # type: Optional[DateTimeFormatter]
    ):
        # type: (...) -> LocalDate
        pass

    def plus(self, period):
        # type: (ReadablePeriod) -> LocalDate
        pass

    def plusDays(self, days):
        # type: (int) -> LocalDate
        pass

    def plusMonths(self, months):
        # type: (int) -> LocalDate
        pass

    def plusWeeks(self, weeks):
        # type: (int) -> LocalDate
        pass

    def plusYears(self, years):
        # type: (int) -> LocalDate
        pass

    def property(self, fieldType):
        # type: (DateTimeFieldType) -> LocalDate.Property
        pass

    def toDate(self):
        # type: () -> Date
        pass

    def toDateTimeAtCurrentTime(self, zone=None):
        # type: (Optional[DateTimeZone]) -> DateTime
        pass

    def toDateTimeAtStartOfDay(self, zone=None):
        # type: (Optional[DateTimeZone]) -> DateTime
        pass

    def toInterval(self, zone=None):
        # type: (Optional[DateTimeZone]) -> Interval
        pass

    def toLocalDateTime(self, time):
        # type: (LocalTime) -> LocalDateTime
        pass

    def weekOfWeekyear(self):
        # type: () -> LocalDate.Property
        pass

    def weekyear(self):
        # type: () -> LocalDate.Property
        pass

    def withCenturyOfEra(self, centuryOfEra):
        # type: (int) -> LocalDate
        pass

    def withDayOfMonth(self, dayOfMonth):
        # type: (int) -> LocalDate
        pass

    def withDayOfWeek(self, dayOfWeek):
        # type: (int) -> LocalDate
        pass

    def withDayOfYear(self, dayOfYear):
        # type: (int) -> LocalDate
        pass

    def withEra(self, era):
        # type: (int) -> LocalDate
        pass

    def withField(self, fieldType, value):
        # type: (DateTimeFieldType, int) -> LocalDate
        pass

    def withFieldAdded(self, fieldType, amount):
        # type: (DateTimeFieldType, int) -> LocalDate
        pass

    def withFields(self, partial):
        # type: (ReadablePartial) -> LocalDate
        pass

    def withMonthOfYear(self, month):
        # type: (int) -> LocalDate
        pass

    def withPeriodAdded(self, periodToAdd, scalar):
        # type: (ReadablePeriod, int) -> LocalDate
        pass

    def withWeekOfWeekyear(self, weekOfWeekyear):
        # type: (int) -> LocalDate
        pass

    def withWeekyear(self, weekyear):
        # type: (int) -> LocalDate
        pass

    def withYear(self, year):
        # type: (int) -> LocalDate
        pass

    def withYearOfCentury(self, yearOfCentury):
        # type: (int) -> LocalDate
        pass

    def withYearOfEra(self, yearOfEra):
        # type: (int) -> LocalDate
        pass

    def year(self):
        # type: () -> LocalDate.Property
        pass

    def yearOfCentury(self):
        # type: () -> LocalDate.Property
        pass

    def yearOfEra(self):
        # type: () -> LocalDate.Property
        pass


class LocalDateTime(BaseLocal):
    class Property(AbstractReadableInstantFieldProperty):
        def addToCopy(self, value):
            # type: (Union[float, int, long]) -> LocalDateTime
            pass

        def addWrapFieldToCopy(self, value):
            # type: (int) -> LocalDateTime
            pass

        def roundCeilingCopy(self):
            # type: () -> LocalDateTime
            pass

        def roundFloorCopy(self):
            # type: () -> LocalDateTime
            pass

        def roundHalfCeilingCopy(self):
            # type: () -> LocalDateTime
            pass

        def roundHalfEvenCopy(self):
            # type: () -> LocalDateTime
            pass

        def roundHalfFloorCopy(self):
            # type: () -> LocalDateTime
            pass

        def setCopy(self, *args):
            # type: (*Any) -> LocalDateTime
            pass

        def withMaximumValue(self):
            # type: () -> LocalDateTime
            pass

        def withMinimumValue(self):
            # type: () -> LocalDateTime
            pass

    def __init__(self, *args):
        # type: (*Any) -> None
        super(LocalDateTime, self).__init__()
        print(args)

    def centuryOfEra(self):
        # type: () -> LocalDateTime.Property
        pass

    def dayOfMonth(self):
        # type: () -> LocalDateTime.Property
        pass

    def dayOfWeek(self):
        # type: () -> LocalDateTime.Property
        pass

    def dayOfYear(self):
        # type: () -> LocalDateTime.Property
        pass

    def era(self):
        # type: () -> LocalDateTime.Property
        pass

    @staticmethod
    def fromCalendarFields(calendar):
        # type: (Calendar) -> LocalDateTime
        pass

    @staticmethod
    def fromDateFields(date):
        # type: (Date) -> LocalDateTime
        pass

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

    def getMillisOfDay(self):
        # type: () -> int
        pass

    def getMillisOfSecond(self):
        # type: () -> int
        pass

    def getMinuteOfHour(self):
        # type: () -> int
        pass

    def getMonthOfYear(self):
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

    def hshCode(self):
        # type: () -> int
        pass

    def hourOfDay(self):
        # type: () -> LocalDateTime.Property
        pass

    def millisOfDay(self):
        # type: () -> LocalDateTime.Property
        pass

    def millisOfSecond(self):
        # type: () -> LocalDateTime.Property
        pass

    def minus(
        self,
        period,  # type: Union[ReadableDuration, ReadablePeriod]
    ):
        # type: (...) -> LocalDateTime
        pass

    def minusDays(self, days):
        # type: (int) -> LocalDateTime
        pass

    def minusHours(self, hours):
        # type: (int) -> LocalDateTime
        pass

    def minusMillis(self, millis):
        # type: (int) -> LocalDateTime
        pass

    def minusMinutes(self, minutes):
        # type: (int) -> LocalDateTime
        pass

    def minusMonths(self, months):
        # type: (int) -> LocalDateTime
        pass

    def minusSeconds(self, seconds):
        # type: (int) -> LocalDateTime
        pass

    def minusWeeks(self, weeks):
        # type: (int) -> LocalDateTime
        pass

    def minusYears(self, years):
        # type: (int) -> LocalDateTime
        pass

    def minuteOfHour(self):
        # type: () -> LocalDateTime.Property
        pass

    def monthOfYear(self):
        # type: () -> LocalDateTime.Property
        pass

    @staticmethod
    def now(arg=None):
        # type: (Union[Chronology, DateTimeZone, None]) -> LocalDateTime
        pass

    @staticmethod
    def parse(
        str_,  # type: Union[str, unicode]
        formatter=None,  # type: Optional[DateTimeFormatter]
    ):
        # type: (...) -> LocalDateTime
        pass

    def plus(
        self,
        period,  # type: Union[ReadableDuration, ReadablePeriod]
    ):
        # type: (...) -> LocalDateTime
        pass

    def plusDays(self, days):
        # type: (int) -> LocalDateTime
        pass

    def plusHours(self, hours):
        # type: (int) -> LocalDateTime
        pass

    def plusMillis(self, millis):
        # type: (int) -> LocalDateTime
        pass

    def plusMinutes(self, minutes):
        # type: (int) -> LocalDateTime
        pass

    def plusMonths(self, months):
        # type: (int) -> LocalDateTime
        pass

    def plusSeconds(self, seconds):
        # type: (int) -> LocalDateTime
        pass

    def plusWeeks(self, weeks):
        # type: (int) -> LocalDateTime
        pass

    def plusYears(self, years):
        # type: (int) -> LocalDateTime
        pass

    def property(self, fieldType):
        # type: (DateTimeFieldType) -> LocalDateTime.Property
        pass

    def secondOfMinute(self):
        # type: () -> LocalDateTime.Property
        pass

    def toDate(self):
        # type: () -> Date
        pass

    def toLocalDate(self, time):
        # type: (LocalTime) -> LocalDate
        pass

    def weekOfWeekyear(self):
        # type: () -> LocalDateTime.Property
        pass

    def weekyear(self):
        # type: () -> LocalDateTime.Property
        pass

    def withCenturyOfEra(self, centuryOfEra):
        # type: (int) -> LocalDateTime
        pass

    def withDayOfMonth(self, dayOfMonth):
        # type: (int) -> LocalDateTime
        pass

    def withDayOfWeek(self, dayOfWeek):
        # type: (int) -> LocalDateTime
        pass

    def withDayOfYear(self, dayOfYear):
        # type: (int) -> LocalDateTime
        pass

    def withDurationAdded(self, durationToAdd, scalar):
        # type: (ReadableDuration, int) -> LocalDateTime
        pass

    def withEra(self, era):
        # type: (int) -> LocalDateTime
        pass

    def withField(self, fieldType, value):
        # type: (DateTimeFieldType, int) -> LocalDateTime
        pass

    def withFieldAdded(self, fieldType, amount):
        # type: (DateTimeFieldType, int) -> LocalDateTime
        pass

    def withFields(self, partial):
        # type: (ReadablePartial) -> LocalDateTime
        pass

    def withHourOfDay(self, hour):
        # type: (int) -> LocalDateTime
        pass

    def withMillisOfDay(self, millis):
        # type: (int) -> LocalDateTime
        pass

    def withMillisOfSecond(self, seconds):
        # type: (int) -> LocalDateTime
        pass

    def withMinuteOfHour(self, minute):
        # type: (int) -> LocalDateTime
        pass

    def withMonthOfYear(self, month):
        # type: (int) -> LocalDateTime
        pass

    def withPeriodAdded(self, periodToAdd, scalar):
        # type: (ReadablePeriod, int) -> LocalDateTime
        pass

    def withSecondOfMinute(self, second):
        # type: (int) -> LocalDateTime
        pass

    def withTime(self, hourOfDay, minuteOfHour, secondOfMinute, millisOfSecond):
        # type: (int, int, int, int) -> LocalDateTime
        pass

    def withWeekOfWeekyear(self, weekOfWeekyear):
        # type: (int) -> LocalDateTime
        pass

    def withWeekyear(self, weekyear):
        # type: (int) -> LocalDateTime
        pass

    def withYear(self, year):
        # type: (int) -> LocalDateTime
        pass

    def withYearOfCentury(self, yearOfCentury):
        # type: (int) -> LocalDateTime
        pass

    def withYearOfEra(self, yearOfEra):
        # type: (int) -> LocalDateTime
        pass

    def year(self):
        # type: () -> LocalDateTime.Property
        pass

    def yearOfCentury(self):
        # type: () -> LocalDateTime.Property
        pass

    def yearOfEra(self):
        # type: () -> LocalDateTime.Property
        pass


class LocalTime(BaseLocal):

    class Property(AbstractReadableInstantFieldProperty):
        def addCopy(self, value):
            # type: (Union[float, int, long]) -> LocalTime
            pass

        def addNoWrapToCopy(self, value):
            # type: (int) -> LocalTime
            pass

        def addWrapFieldToCopy(self, value):
            # type: (int) -> LocalTime
            pass

        def getLocalTime(self):
            # type: () -> LocalTime
            pass

        def roundCeilingCopy(self):
            # type: () -> LocalTime
            pass

        def roundFloorCopy(self):
            # type: () -> LocalTime
            pass

        def roundHalfCeilingCopy(self):
            # type: () -> LocalTime
            pass

        def roundHalfEvenCopy(self):
            # type: () -> LocalTime
            pass

        def roundHalfFloorCopy(self):
            # type: () -> LocalTime
            pass

        def setCopy(self, *args):
            # type: (*Any) -> LocalTime
            pass

        def withMaximumValue(self):
            # type: () -> LocalTime
            pass

        def withMinimumValue(self):
            # type: () -> LocalTime
            pass

    MIDNIGHT = None  # type: LocalTime

    def __init__(self, *args):
        # type: (*Any) -> None
        super(LocalTime, self).__init__()
        print(args)

    @staticmethod
    def fromCalendarFields(calendar):
        # type: (Calendar) -> LocalTime
        pass

    @staticmethod
    def fromDateFields(date):
        # type: (Date) -> LocalTime
        pass

    @staticmethod
    def fromMillisOfDay(millisOfDay, chrono=None):
        # type: (long, Optional[Chronology]) -> LocalTime
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

    def getMinuteOfHour(self):
        # type: () -> int
        pass

    def getSecondOfMinute(self):
        # type: () -> int
        pass

    def hourOfDay(self):
        # type: () -> LocalTime.Property
        pass

    def millisOfDay(self):
        # type: () -> LocalTime.Property
        pass

    def millisOfSecond(self):
        # type: () -> LocalTime.Property
        pass

    def minus(self, period):
        # type: (ReadablePeriod) -> LocalTime
        pass

    def minusHours(self, hours):
        # type: (int) -> LocalTime
        pass

    def minusMillis(self, millis):
        # type: (int) -> LocalTime
        pass

    def minusMinutes(self, minutes):
        # type: (int) -> LocalTime
        pass

    def minusSeconds(self, seconds):
        # type: (int) -> LocalTime
        pass

    def minuteOfHour(self):
        # type: () -> LocalTime.Property
        pass

    @staticmethod
    def now(arg=None):
        # type: (Union[Chronology, DateTimeZone, None]) -> LocalTime
        pass

    @staticmethod
    def parse(
        str_,  # type: Union[str, unicode]
        formatter=None,  # type: Optional[DateTimeFormatter]
    ):
        # type: (...) -> LocalTime
        pass

    def plus(self, period):
        # type: (ReadablePeriod) -> LocalTime
        pass

    def plusHours(self, hours):
        # type: (int) -> LocalTime
        pass

    def plusMillis(self, millis):
        # type: (int) -> LocalTime
        pass

    def plusMinutes(self, minutes):
        # type: (int) -> LocalTime
        pass

    def plusSeconds(self, seconds):
        # type: (int) -> LocalTime
        pass

    def property(self, fieldType):
        # type: (DateTimeFieldType) -> LocalTime.Property
        pass

    def secondOfMinute(self):
        # type: () -> LocalTime.Property
        pass

    def toDateTimeToday(self, zone=None):
        # type: (Optional[DateTimeZone]) -> DateTime
        pass

    def withField(self, fieldType, value):
        # type: (DateTimeFieldType, int) -> LocalTime
        pass

    def withFieldAdded(self, fieldType, amount):
        # type: (DateTimeFieldType, int) -> LocalTime
        pass

    def withFields(self, partial):
        # type: (ReadablePartial) -> LocalTime
        pass

    def withHourOfDay(self, hour):
        # type: (int) -> LocalTime
        pass

    def withMillisOfDay(self, millisOfDay):
        # type: (int) -> LocalTime
        pass

    def withMillisOfSecond(self, millisOfSecond):
        # type: (int) -> LocalTime
        pass

    def withMinuteOfHour(self, minute):
        # type: (int) -> LocalTime
        pass

    def withPeriodAdded(self, periodToAdd, scalar):
        # type: (ReadablePeriod, int) -> LocalTime
        pass

    def withSecondOfMinute(self, second):
        # type: (int) -> LocalTime
        pass


class Minutes(BaseSingleFieldPeriod):
    MAX_VALUE = None  # type: Minutes
    MIN_VALUE = None  # type: Minutes
    ONE = None  # type: Minutes
    THREE = None  # type: Minutes
    TWO = None  # type: Minutes
    ZERO = None  # type: Minutes

    def dividedBy(self, divisor):
        # type: (int) -> Minutes
        pass

    def getMinutes(self):
        # type: () -> int
        pass

    def isGreaterThan(self, other):
        # type: (Minutes) -> bool
        pass

    def isLessThan(self, other):
        # type: (Minutes) -> bool
        pass

    def minus(self, minutes):
        # type: (Union[Minutes, int]) -> Minutes
        pass

    @staticmethod
    def minutesBetween(
        start,  # type: Union[ReadableInstant, ReadablePartial]
        end,  # type: Union[ReadableInstant, ReadablePartial]
    ):
        # type: (...) -> Minutes
        pass

    @staticmethod
    def minutesIn(interval):
        # type: (ReadableInterval) -> Minutes
        pass

    def multipliedBy(self, scalar):
        # type: (int) -> Minutes
        pass

    def negated(self):
        # type: () -> Minutes
        pass

    @staticmethod
    def parseMinutes(periodStr):
        # type: (Union[str, unicode]) -> Minutes
        pass

    def plus(self, minutes):
        # type: (Union[Minutes, int]) -> Minutes
        pass

    @staticmethod
    def standardMinutesIn(period):
        # type: (ReadablePeriod) -> Minutes
        pass

    def toStandardDays(self):
        # type: () -> Days
        pass

    def toStandardDuration(self):
        # type: () -> Duration
        pass

    def toStandardHours(self):
        # type: () -> Hours
        pass

    def toStandardSeconds(self):
        # type: () -> Seconds
        pass

    def toStandardWeeks(self):
        # type: () -> Weeks
        pass


class MutableDateTime(BaseDateTime, ReadWritableDateTime):

    class Property(AbstractReadableInstantFieldProperty):
        def add(self, value):
            # type: (Union[float, int, long]) -> MutableDateTime
            pass

        def addWrapField(self, value):
            # type: (int) -> MutableDateTime
            pass

        def getMutableDateTime(self):
            # type: () -> MutableDateTime
            pass

        def roundCeiling(self):
            # type: () -> MutableDateTime
            pass

        def roundFloor(self):
            # type: () -> MutableDateTime
            pass

        def roundHalfCeiling(self):
            # type: () -> MutableDateTime
            pass

        def roundHalfEven(self):
            # type: () -> MutableDateTime
            pass

        def roundHalfFloor(self):
            # type: () -> MutableDateTime
            pass

        def set(self, *args):
            # type: (*Any) -> MutableDateTime
            pass

    ROUND_CEILING = None  # type: int
    ROUND_FLOOR = None  # type: int
    ROUND_HALF_CEILING = None  # type: int
    ROUND_HALF_EVEN = None  # type: int
    ROUND_HALF_FLOOR = None  # type: int
    ROUND_NONE = None  # type: int

    def __init__(self, *args):
        # type: (*Any) -> None
        super(MutableDateTime, self).__init__()
        print(args)

    def centuryOfEra(self):
        # type: () -> MutableDateTime.Property
        pass

    def copy(self):
        # type: () -> MutableDateTime
        pass

    def dayOfMonth(self):
        # type: () -> MutableDateTime.Property
        pass

    def dayOfWeek(self):
        # type: () -> MutableDateTime.Property
        pass

    def dayOfYear(self):
        # type: () -> MutableDateTime.Property
        pass

    def era(self):
        # type: () -> MutableDateTime.Property
        pass

    def getRoundingField(self):
        # type: () -> DateTimeField
        pass

    def getRoundingMode(self):
        # type: () -> int
        pass

    def hourOfDay(self):
        # type: () -> MutableDateTime.Property
        pass

    def millisOfDay(self):
        # type: () -> MutableDateTime.Property
        pass

    def millisOfSecond(self):
        # type: () -> MutableDateTime.Property
        pass

    def minuteOfDay(self):
        # type: () -> MutableDateTime.Property
        pass

    def minuteOfHour(self):
        # type: () -> MutableDateTime.Property
        pass

    def monthOfYear(self):
        # type: () -> MutableDateTime.Property
        pass

    @staticmethod
    def now(
        arg,  # type: Union[Chronology, DateTimeZone, None]
    ):
        # type: (...) -> MutableDateTime
        pass

    @staticmethod
    def parse(
        str_,  # type: Union[str, unicode]
        formatter=None,  # type: Optional[DateTimeFormatter]
    ):
        # type: (...) -> MutableDateTime
        pass

    def property(self, type_):
        # type: (DateTimeFieldType) -> MutableDateTime.Property
        pass

    def secondOfDay(self):
        # type: () -> MutableDateTime.Property
        pass

    def secondOfMinute(self):
        # type: () -> MutableDateTime.Property
        pass

    def setRounding(self, field, mode=None):
        # type: (DateTimeField, Optional[int]) -> None
        pass

    def weekOfWeekyear(self):
        # type: () -> MutableDateTime.Property
        pass

    def weekyear(self):
        # type: () -> MutableDateTime.Property
        pass

    def year(self):
        # type: () -> MutableDateTime.Property
        pass

    def yearOfCentury(self):
        # type: () -> MutableDateTime.Property
        pass

    def yearOfEra(self):
        # type: () -> MutableDateTime.Property
        pass


class MutableInterval(BaseInterval, ReadableInterval):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(MutableInterval, self).__init__()
        print(args)

    def clone(self):
        # type: () -> Object
        pass

    def copy(self):
        # type: () -> MutableInterval
        pass

    @staticmethod
    def parse(str_):
        # type: (Union[str, unicode]) -> MutableInterval
        pass

    def setChronology(self, chronology):
        # type: (Chronology) -> None
        pass

    def setDurationAfterStart(self, duration):
        # type: (Union[ReadableDuration, long]) -> None
        pass

    def setDurationBeforeEnd(self, duration):
        # type: (Union[ReadableDuration, long]) -> None
        pass

    def setEnd(self, end):
        # type: (ReadableInstant) -> None
        pass

    def setEndMillis(self, endInstant):
        # type: (long) -> None
        pass

    def setInterval(self, *args):
        # type: (*Any) -> None
        pass

    def setPeriodAfterStart(self, period):
        # type: (ReadablePeriod) -> None
        pass

    def setPeriodBeforeEnd(self, period):
        # type: (ReadablePeriod) -> None
        pass

    def setStart(self, start):
        # type: (ReadableInstant) -> None
        pass

    def setStartMillis(self, startInstant):
        # type: (long) -> None
        pass


class MutablePeriod(BasePeriod, ReadWritablePeriod):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(MutablePeriod, self).__init__()
        print(args)

    def addField(self, fieldType, value):
        # type: (DurationFieldType, int) -> None
        pass

    def addStandardDays(self, days):
        # type: (int) -> None
        pass

    def addStandardHours(self, hours):
        # type: (int) -> None
        pass

    def addStandardMinutes(self, minutes):
        # type: (int) -> None
        pass

    def addStandardSeconds(self, seconds):
        # type: (int) -> None
        pass

    def setValues(self, values):
        # type: (List[int]) -> None
        pass


class Period(BasePeriod):
    ZERO = None  # type: Period

    def __init__(self, *args):
        # type: (*Any) -> None
        super(Period, self).__init__()
        print(args)

    @staticmethod
    def days(days):
        # type: (int) -> Period
        pass

    @staticmethod
    def fieldDifference(start, end):
        # type: (ReadablePartial, ReadablePartial) -> Period
        pass

    def getDays(self):
        # type: () -> int
        pass

    def getHours(self):
        # type: () -> int
        pass

    def getMillis(self):
        # type: () -> int
        pass

    def getMinutes(self):
        # type: () -> int
        pass

    def getMonths(self):
        # type: () -> int
        pass

    def getSeconds(self):
        # type: () -> int
        pass

    def getWeeks(self):
        # type: () -> int
        pass

    def getYears(self):
        # type: () -> int
        pass

    @staticmethod
    def hours(hours):
        # type: (int) -> Period
        pass

    @staticmethod
    def millis(millis):
        # type: (int) -> Period
        pass

    def minus(self, period):
        # type: (ReadablePeriod) -> Period
        pass

    def minusDays(self, days):
        # type: (int) -> Period
        pass

    def minusHours(self, hours):
        # type: (int) -> Period
        pass

    def minusMillis(self, millis):
        # type: (int) -> Period
        pass

    def minusMinutes(self, minutes):
        # type: (int) -> Period
        pass

    def minusMonths(self, months):
        # type: (int) -> Period
        pass

    def minusSeconds(self, seconds):
        # type: (int) -> Period
        pass

    def minusWeeks(self, weeks):
        # type: (int) -> Period
        pass

    def minusYears(self, years):
        # type: (int) -> Period
        pass

    @staticmethod
    def minutes(minutes):
        # type: (int) -> Period
        pass

    @staticmethod
    def months(months):
        # type: (int) -> Period
        pass

    def multipliedBy(self, scalar):
        # type: (int) -> Period
        pass

    def negated(self):
        # type: () -> Period
        pass

    def normalizedStandard(self, periodType=None):
        # type: (Optional[PeriodType]) -> Period
        pass

    @staticmethod
    def parse(
        str_,  # type: Union[str, unicode]
        formatter=None,  # type: Optional[PeriodFormatter]
    ):
        # type: (...) -> Period
        pass

    def plus(self, period):
        # type: (ReadablePeriod) -> Period
        pass

    def plusDays(self, days):
        # type: (int) -> Period
        pass

    def plusHours(self, hours):
        # type: (int) -> Period
        pass

    def plusMillis(self, millis):
        # type: (int) -> Period
        pass

    def plusMinutes(self, minutes):
        # type: (int) -> Period
        pass

    def plusMonths(self, months):
        # type: (int) -> Period
        pass

    def plusSeconds(self, seconds):
        # type: (int) -> Period
        pass

    def plusWeeks(self, weeks):
        # type: (int) -> Period
        pass

    def plusYears(self, years):
        # type: (int) -> Period
        pass

    @staticmethod
    def seconds(seconds):
        # type: (int) -> Period
        pass

    def toStandardDays(self):
        # type: () -> Days
        pass

    def toStandardDuration(self):
        # type: () -> Duration
        pass

    def toStandardHours(self):
        # type: () -> Hours
        pass

    def toStandardMinutes(self):
        # type: () -> Minutes
        pass

    def toStandardSeconds(self):
        # type: () -> Seconds
        pass

    def toStandardWeeks(self):
        # type: () -> Weeks
        pass

    @staticmethod
    def weeks(weeks):
        # type: (int) -> Period
        pass

    def withField(self, field, value):
        # type: (DurationFieldType, int) -> Period
        pass

    def withFieldAdded(self, field, value):
        # type: (DurationFieldType, int) -> Period
        pass

    def withFields(self, period):
        # type: (ReadablePeriod) -> Period
        pass

    def withDays(self, days):
        # type: (int) -> Period
        pass

    def withHours(self, hours):
        # type: (int) -> Period
        pass

    def withMillis(self, millis):
        # type: (int) -> Period
        pass

    def withMinutes(self, minutes):
        # type: (int) -> Period
        pass

    def withMonths(self, months):
        # type: (int) -> Period
        pass

    def withSeconds(self, seconds):
        # type: (int) -> Period
        pass

    def withWeeks(self, weeks):
        # type: (int) -> Period
        pass

    def withYears(self, years):
        # type: (int) -> Period
        pass

    @staticmethod
    def years(years):
        # type: (int) -> Period
        pass


class PeriodType(Object):
    @staticmethod
    def days():
        # type: () -> PeriodType
        pass

    @staticmethod
    def dayTime():
        # type: () -> PeriodType
        pass

    @staticmethod
    def forFields(fields):
        # type: (List[DurationFieldType]) -> PeriodType
        pass

    def getFieldType(self):
        # type: () -> DurationFieldType
        pass

    def getName(self):
        # type: () -> Union[str, unicode]
        pass

    @staticmethod
    def hours():
        # type: () -> PeriodType
        pass

    def indexOf(self, type_):
        # type: (DurationFieldType) -> int
        pass

    def isSupported(self, type_):
        # type: (DurationFieldType) -> bool
        pass

    @staticmethod
    def millis():
        # type: () -> PeriodType
        pass

    @staticmethod
    def minutes():
        # type: () -> PeriodType
        pass

    @staticmethod
    def months():
        # type: () -> PeriodType
        pass

    @staticmethod
    def seconds():
        # type: () -> PeriodType
        pass

    def size(self):
        # type: () -> int
        pass

    @staticmethod
    def standard():
        # type: () -> PeriodType
        pass

    @staticmethod
    def time():
        # type: () -> PeriodType
        pass

    @staticmethod
    def weeks():
        # type: () -> PeriodType
        pass

    def withDaysRemoved(self):
        # type: () -> PeriodType
        pass

    def withHoursRemoved(self):
        # type: () -> PeriodType
        pass

    def withMillisRemoved(self):
        # type: () -> PeriodType
        pass

    def withMinutesRemoved(self):
        # type: () -> PeriodType
        pass

    def withMonthsRemoved(self):
        # type: () -> PeriodType
        pass

    def withSecondsRemoved(self):
        # type: () -> PeriodType
        pass

    def withWeeksRemoved(self):
        # type: () -> PeriodType
        pass

    def withYearsRemoved(self):
        # type: () -> PeriodType
        pass

    @staticmethod
    def yearDay():
        # type: () -> PeriodType
        pass

    @staticmethod
    def yearDayTime():
        # type: () -> PeriodType
        pass

    @staticmethod
    def yearMonthDay():
        # type: () -> PeriodType
        pass

    @staticmethod
    def yearMonthDayTime():
        # type: () -> PeriodType
        pass

    @staticmethod
    def years():
        # type: () -> PeriodType
        pass

    @staticmethod
    def yearWeekDay():
        # type: () -> PeriodType
        pass

    @staticmethod
    def yearWeekDayTime():
        # type: () -> PeriodType
        pass


class Seconds(BaseSingleFieldPeriod):
    MAX_VALUE = None  # type: Seconds
    MIN_VALUE = None  # type: Seconds
    ONE = None  # type: Seconds
    THREE = None  # type: Seconds
    TWO = None  # type: Seconds
    ZERO = None  # type: Seconds

    def dividedBy(self, divisor):
        # type: (int) -> Seconds
        pass

    def getSeconds(self):
        # type: () -> int
        pass

    def isGreaterThan(self, other):
        # type: (Seconds) -> bool
        pass

    def isLessThan(self, other):
        # type: (Seconds) -> bool
        pass

    def minus(self, seconds):
        # type: (Union[Seconds, int]) -> Seconds
        pass

    def multipliedBy(self, scalar):
        # type: (int) -> Seconds
        pass

    def negated(self):
        # type: () -> Seconds
        pass

    @staticmethod
    def parseSeconds(periodStr):
        # type: (Union[str, unicode]) -> Seconds
        pass

    def plus(self, seconds):
        # type: (Union[Seconds, int]) -> Seconds
        pass

    @staticmethod
    def seconds(seconds):
        # type: (int) -> Seconds
        pass

    @staticmethod
    def secondsBetween(
        start,  # type: Union[ReadableInstant, ReadablePartial]
        end,  # type: Union[ReadableInstant, ReadablePartial]
    ):
        # type: (...) -> Seconds
        pass

    @staticmethod
    def secondsIn(interval):
        # type: (ReadableInterval) -> Seconds
        pass

    @staticmethod
    def standardSecondsIn(period):
        # type: (ReadablePeriod) -> Seconds
        pass

    def toStandardDays(self):
        # type: () -> Days
        pass

    def toStandardDuration(self):
        # type: () -> Duration
        pass

    def toStandardHours(self):
        # type: () -> Hours
        pass

    def toStandardMinutes(self):
        # type: () -> Minutes
        pass

    def toStandardWeeks(self):
        # type: () -> Weeks
        pass


class Weeks(BaseSingleFieldPeriod):
    MAX_VALUE = None  # type: Weeks
    MIN_VALUE = None  # type: Weeks
    ONE = None  # type: Weeks
    THREE = None  # type: Weeks
    TWO = None  # type: Weeks
    ZERO = None  # type: Weeks

    def dividedBy(self, divisor):
        # type: (int) -> Weeks
        pass

    def getWeeks(self):
        # type: () -> int
        pass

    def isGreaterThan(self, other):
        # type: (Weeks) -> bool
        pass

    def isLessThan(self, other):
        # type: (Weeks) -> bool
        pass

    def minus(self, weeks):
        # type: (Union[Weeks, int]) -> Weeks
        pass

    def multipliedBy(self, scalar):
        # type: (int) -> Weeks
        pass

    def negated(self):
        # type: () -> Weeks
        pass

    @staticmethod
    def parseWeeks(periodStr):
        # type: (Union[str, unicode]) -> Weeks
        pass

    def plus(self, weeks):
        # type: (Union[Weeks, int]) -> Weeks
        pass

    @staticmethod
    def standardWeeksIn(period):
        # type: (ReadablePeriod) -> Weeks
        pass

    def toStandardDays(self):
        # type: () -> Days
        pass

    def toStandardDuration(self):
        # type: () -> Duration
        pass

    def toStandardHours(self):
        # type: () -> Hours
        pass

    def toStandardMinutes(self):
        # type: () -> Minutes
        pass

    def toStandardSeconds(self):
        # type: () -> Seconds
        pass

    @staticmethod
    def weeks(weeks):
        # type: (int) -> Weeks
        pass

    @staticmethod
    def weeksBetween(
        start,  # type: Union[ReadableInstant, ReadablePartial]
        end,  # type: Union[ReadableInstant, ReadablePartial]
    ):
        # type: (...) -> Weeks
        pass

    @staticmethod
    def weeksIn(interval):
        # type: (ReadableInterval) -> Weeks
        pass
