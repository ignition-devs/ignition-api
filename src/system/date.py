"""Date Functions.

The following functions give you access to test and modify dates.
"""

from __future__ import print_function

__all__ = [
    "addDays",
    "addHours",
    "addMillis",
    "addMinutes",
    "addMonths",
    "addSeconds",
    "addWeeks",
    "addYears",
    "daysBetween",
    "format",
    "fromMillis",
    "getAMorPM",
    "getDate",
    "getDayOfMonth",
    "getDayOfWeek",
    "getDayOfYear",
    "getHour12",
    "getHour24",
    "getMillis",
    "getMinute",
    "getMonth",
    "getQuarter",
    "getSecond",
    "getTimezone",
    "getTimezoneOffset",
    "getTimezoneRawOffset",
    "getYear",
    "hoursBetween",
    "isAfter",
    "isBefore",
    "isBetween",
    "isDaylightTime",
    "midnight",
    "millisBetween",
    "minutesBetween",
    "monthsBetween",
    "now",
    "parse",
    "secondsBetween",
    "setTime",
    "toMillis",
    "weeksBetween",
    "yearsBetween",
]

from java.text import SimpleDateFormat
from java.time import ZoneId
from java.util import Calendar, Date, GregorianCalendar, Locale, TimeZone
from java.util.concurrent import TimeUnit


def _add(date, field, amount):
    """Adds or subtracts the specified amount of time to the given
    calendar field, based on the calendar's rules.

    Args:
        date (Date): The starting Date.
        field (int): The Calendar field.
        amount (int): The amount of date to be added to the field.

    Returns:
        Date: A new Date object offset by the integer passed into the
            function.
    """
    cal = Calendar.getInstance()
    cal.setTime(date)
    cal.add(field, amount)
    return cal.getTime()


def addDays(date, value):
    """Add or subtract an amount of days to a given date and time.

    Args:
        date (Date): The starting date.
        value (int): The number of units to add, or subtract if the
            value is negative.

    Returns:
        Date: A new date object offset by the integer passed to the
            function.
    """
    return _add(date, Calendar.DATE, value)


def addHours(date, value):
    """Add or subtract an amount of hours to a given date and time.

    Args:
        date (Date): The starting date.
        value (int): The number of units to add, or subtract if the
            value is negative.

    Returns:
        Date: A new date object offset by the integer passed to the
            function.
    """
    return _add(date, Calendar.HOUR, value)


def addMillis(date, value):
    """Add or subtract an amount of milliseconds to a given date and
    time.

    Args:
        date (Date): The starting date.
        value (int): The number of units to add, or subtract if the
            value is negative.

    Returns:
        Date: A new date object offset by the integer passed to
            the function.
    """
    return _add(date, Calendar.MILLISECOND, value)


def addMinutes(date, value):
    """Add or subtract an amount of minutes to a given date and time.

    Args:
        date (Date): The starting date.
        value (int): The number of units to add, or subtract if the
            value is negative.

    Returns:
        Date: A new date object offset by the integer passed to the
            function.
    """
    return _add(date, Calendar.MINUTE, value)


def addMonths(date, value):
    """Add or subtract an amount of months to a given date and time.

    This function is unique since each month can have a variable number
    of days. For example, if the date passed in is March 31st, and we
    add one month, April does not have a 31st day, so the returned date
    will be the proper number of months rounded down to the closest
    available day, in this case April 30th.

    Args:
        date (Date): The starting date.
        value (int): The number of units to add, or subtract if the
            value is negative.

    Returns:
        Date: A new date object offset by the integer passed to the
            function.
    """
    return _add(date, Calendar.MONTH, value)


def addSeconds(date, value):
    """Add or subtract an amount of seconds to a given date and time.

    Args:
        date (Date): The starting date.
        value (int): The number of units to add, or subtract if the
            value is negative.

    Returns:
        Date: A new date object offset by the integer passed to
            the function.
    """
    return _add(date, Calendar.SECOND, value)


def addWeeks(date, value):
    """Add or subtract an amount of weeks to a given date and time.

    Args:
        date (Date): The starting date.
        value (int): The number of units to add, or subtract if the
            value is negative.

    Returns:
        Date: A new date object offset by the integer passed to the
            function.
    """
    return _add(date, Calendar.WEEK_OF_YEAR, value)


def addYears(date, value):
    """Add or subtract an amount of years to a given date and time.

    Args:
        date (Date): The starting date.
        value (int): The number of units to add, or subtract if the
            value is negative.

    Returns:
        Date: A new date object offset by the integer passed to
            the function.
    """
    return _add(date, Calendar.YEAR, value)


def daysBetween(date_1, date_2):
    """Calculates the number of whole days between two dates.

    Daylight Saving Time changes are taken into account.

    Args:
        date_1 (Date): The first date to use.
        date_2 (Date): The second date to use.

    Returns:
        int: An integer that is representative of the difference between
            two dates.
    """
    return int(
        TimeUnit.DAYS.convert(
            date_2.getTime() - date_1.getTime(), TimeUnit.MILLISECONDS
        )
    )


def format(date, format="yyyy-MM-dd HH:mm:ss"):
    """Returns the given date as a string, formatted according to a
    pattern.

    Note:
        Not all symbols from system.date.format() have a counterpart
        directive on strftime().

    Args:
        date (Date): The date to format.
        format (str): A format string such as "yyyy-MM-dd HH:mm:ss".

    Returns:
        str: A string representing the formatted datetime
    """
    sdf = SimpleDateFormat(format)
    return sdf.format(date)


def fromMillis(millis):
    """Creates a date object given a millisecond value.

    Args:
        millis (long): The number of milliseconds elapsed since
            January 1, 1970, 00:00:00 UTC (GMT).

    Returns:
        Date: A new date object.
    """
    return Date(millis)


def getAMorPM(date):
    """Returns a 0 if the time is before noon, and a 1 if the time is
    after noon.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    cal = Calendar.getInstance()
    cal.setTime(date)
    return 1 if cal.get(Calendar.HOUR_OF_DAY) >= 12 else 0


def getDate(year, month, day):
    """Creates a new Date object given a year, month and a day.

    The time will be set to midnight of that day.

    Args:
        year (int): The year for the new date.
        month (int): The month of the new date. January is month 0.
        day (int): The day of the month for the new date. The first
            day of the month is day 1.

    Returns:
        Date: A new date, set to midnight of that day.
    """
    cal = Calendar.getInstance()
    cal.set(year, month, day, 0, 0, 0)
    return cal.getTime()


def getDayOfMonth(date):
    """Extracts the day of the month from a date.

    The first day of the month is day 1.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    cal = Calendar.getInstance()
    cal.setTime(date)
    return cal.get(Calendar.DAY_OF_MONTH)


def getDayOfWeek(date):
    """Extracts the day of the week from a date.

    Sunday is day 1, Saturday is day 7.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    cal = Calendar.getInstance()
    cal.setTime(date)
    return cal.get(Calendar.DAY_OF_WEEK)


def getDayOfYear(date):
    """Extracts the day of the year from a date.

    The first day of the year is day 1.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    cal = Calendar.getInstance()
    cal.setTime(date)
    return cal.get(Calendar.DAY_OF_YEAR)


def getHour12(date):
    """Extracts the hour from a date.

    Uses a 12 hour clock, so noon and midnight are returned as 0.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    cal = Calendar.getInstance()
    cal.setTime(date)
    return (
        cal.get(Calendar.HOUR_OF_DAY) - 12
        if cal.get(Calendar.HOUR_OF_DAY) > 12
        else cal.get(Calendar.HOUR_OF_DAY)
    )


def getHour24(date):
    """Extracts the hour from a date.

    Uses a 24 hour clock, so midnight is zero.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    cal = Calendar.getInstance()
    cal.setTime(date)
    return cal.get(Calendar.HOUR_OF_DAY)


def getMillis(date):
    """Extracts the milliseconds from a date, ranging from 0-999.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    cal = Calendar.getInstance()
    cal.setTime(date)
    return cal.get(Calendar.MILLISECOND)


def getMinute(date):
    """Extracts the minutes from a date, ranging from 0-59.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    cal = Calendar.getInstance()
    cal.setTime(date)
    return cal.get(Calendar.MINUTE)


def getMonth(date):
    """Extracts the month from a date, where January is month 0.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    cal = Calendar.getInstance()
    cal.setTime(date)
    return cal.get(Calendar.MONTH)


def getQuarter(date):
    """Extracts the quarter from a date, ranging from 1-4.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    cal = Calendar.getInstance()
    cal.setTime(date)
    return cal.get(Calendar.MONTH) // 3 + 1


def getSecond(date):
    """Extracts the seconds from a date, ranging from 0-59.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    cal = Calendar.getInstance()
    cal.setTime(date)
    return cal.get(Calendar.SECOND)


def getTimezone():
    """Returns the ID of the current timezone.

    Returns:
        str: A representation of the current timezone.
    """
    return ZoneId.systemDefault()


def getTimezoneOffset(date=Date()):
    """Returns the current timezone's offset versus UTC for a given
    instant, taking Daylight Saving Time into account.

    Args:
        date (Date): The instant in time for which to calculate
            the offset. Uses now() if omitted. Optional.

    Returns:
        float: The timezone offset compared to UTC, in hours.
    """
    cal = Calendar.getInstance()
    cal.setTime(date)
    zoff = cal.get(Calendar.ZONE_OFFSET)
    dstoff = cal.get(Calendar.DST_OFFSET)
    return (zoff + dstoff) / 3600000.0


def getTimezoneRawOffset():
    """Returns the current timezone offset versus UTC, not taking
    Daylight Saving Time into account.

    Returns:
         float: The timezone offset.
    """
    cal = Calendar.getInstance()
    cal.setTime(Date())
    return cal.get(Calendar.ZONE_OFFSET) / 3600000.0


def getYear(date):
    """Extracts the year from a date.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    cal = Calendar.getInstance()
    cal.setTime(date)
    return cal.get(Calendar.YEAR)


def hoursBetween(date_1, date_2):
    """Calculates the number of whole hours between two dates.

    Args:
        date_1 (Date): The first date to use.
        date_2 (Date): The second date to use.

    Returns:
        int: An integer that is representative of the difference
            between two dates.
    """
    return int(
        TimeUnit.HOURS.convert(
            date_2.getTime() - date_1.getTime(), TimeUnit.MILLISECONDS
        )
    )


def isAfter(date_1, date_2):
    """Compares two dates to see if date_1 is after date_2.

    Args:
        date_1 (Date): The first date.
        date_2 (Date): The second date.

    Returns:
        bool: True (1) if date_1 is after date_2, False (0) otherwise.
    """
    return date_1.after(date_2)


def isBefore(date_1, date_2):
    """Compares to dates to see if date_1 is before date_2.

    Args:
        date_1 (Date): The first date.
        date_2 (Date): The second date.

    Returns:
        bool: True (1) if date_1 is before date_2, False (0)
            otherwise.
    """
    return date_1.before(date_2)


def isBetween(target_date, start_date, end_date):
    """Compares two dates to see if a target date is between two other
    dates.

    Args:
        target_date (Date): The date to compare.
        start_date (Date): The start of a date range.
        end_date (Date): The end of a date range. This date must
            be after the start date.

    Returns:
        bool: True (1) if target_date is >= start_date and
            target_date <= end_date, False (0) otherwise.
    """
    return (
        target_date.compareTo(start_date)
        >= 0
        >= target_date.compareTo(end_date)
    )


def isDaylightTime(date=Date()):
    """Checks to see if the current timezone is using Daylight Saving
    Time during the date specified.

    Args:
        date (Date): The date you want to check if the current timezone
            is observing Daylight Saving Time. Uses now() if omitted.
            Optional.

    Returns:
        bool: True (1) if date is observing Daylight Saving Time in the
            current timezone, False (0) otherwise.
    """
    return TimeZone.getDefault().inDaylightTime(date)


def midnight(date):
    """Returns a copy of a date with the hour, minute, second, and
    millisecond fields set to zero.

    Args:
        date (Date): The starting date.

    Returns:
        Date: A new date, set to midnight of the day provided.
    """
    return setTime(date, 0, 0, 0)


def millisBetween(date_1, date_2):
    """Calculates the number of whole milliseconds between two dates.

    Args:
        date_1 (Date): The first date to use.
        date_2 (Date): The second date to use.

    Returns:
        long: An integer that is representative of the difference
            between two dates.
    """
    return TimeUnit.MILLISECONDS.convert(
        date_2.getTime() - date_1.getTime(), TimeUnit.MILLISECONDS
    )


def minutesBetween(date_1, date_2):
    """Calculates the number of whole minutes between two dates.

    Args:
        date_1 (Date): The first date to use.
        date_2 (Date): The second date to use.

    Returns:
        int: An integer that is representative of the difference
            between two dates.
    """
    return int(
        TimeUnit.MINUTES.convert(
            date_2.getTime() - date_1.getTime(), TimeUnit.MILLISECONDS
        )
    )


def monthsBetween(date_1, date_2):
    """Calculates the number of whole months between two dates.

    Daylight Saving Time changes are taken into account.

    Args:
        date_1 (Date): The first date to use.
        date_2 (Date): The second date to use.

    Returns:
        int: An integer that is representative of the difference
            between two dates.
    """
    start = GregorianCalendar()
    end = GregorianCalendar()
    start.setTime(date_1)
    end.setTime(date_2)
    return end.get(Calendar.MONTH) - start.get(Calendar.MONTH)


def now():
    """Returns a java.util.Date object that represents the current time
    according to the local system clock.

    Returns:
        Date: A new date, set to the current date and time.
    """
    return Date()


def parse(
    dateString, formatString="yyyy-MM-dd HH:mm:ss", locale=Locale.ENGLISH
):
    """Attempts to parse a string and create a Date.

    Causes ParseException if the date dateString parameter is in an
    unrecognized format.

    Args:
        dateString (str): The string to parse into a date.
        formatString (str): Format string used by the parser. Default
            is "yyyy-MM-dd HH:mm:ss". Optional.
        locale (object): Locale used for parsing. Can be the locale
            name such as 'fr', or the Java Locale such as
            'Locale.French'. Default is 'Locale.English'. Optional.

    Returns:
        Date: The parsed date.
    """
    date_format = SimpleDateFormat(formatString, locale)
    cal = Calendar.getInstance(locale)
    cal.setTime(date_format.parse(dateString))
    return cal.getTime()


def secondsBetween(date_1, date_2):
    """Calculates the number of whole seconds between two dates.

    Args:
        date_1 (Date): The first date to use.
        date_2 (Date): The second date to use.

    Returns:
        int: An integer that is representative of the difference between
            two dates.
    """
    return int(
        TimeUnit.SECONDS.convert(
            date_2.getTime() - date_1.getTime(), TimeUnit.MILLISECONDS
        )
    )


def setTime(date, hour, minute, second):
    """Takes in a date, and returns a copy of it with the time fields
    set as specified.

    Args:
        date (Date): The starting date.
        hour (int): The hours (0-23) to set.
        minute(int): The minutes (0-59) to set.
        second (int): The seconds (0-59) to set.

    Returns:
        Date: A new date, set to the appropriate time.
    """
    cal = Calendar.getInstance()
    cal.setTime(date)
    cal.set(Calendar.HOUR_OF_DAY, hour)
    cal.set(Calendar.MINUTE, minute)
    cal.set(Calendar.SECOND, second)
    return cal.getTime()


def toMillis(date):
    """Converts a Date object to its millisecond value elapsed since
    January 1, 1970, 00:00:00 UTC (GMT).

    Args:
        date (Date): The date object to convert.

    Returns:
        long: 8-byte integer representing the number of millisecond
            elapsed since January 1, 1970, 00:00:00 UTC (GMT).
    """
    return date.getTime()


def weeksBetween(date_1, date_2):
    """Calculates the number of whole weeks between two dates.

    Args:
        date_1 (Date): The first date to use.
        date_2 (Date): The second date to use.

    Returns:
        int: An integer that is representative of the difference between
            two dates.
    """
    cal = GregorianCalendar()
    cal.setTime(date_1)
    weeks = -1
    while cal.getTime().before(date_2):
        cal.add(Calendar.WEEK_OF_YEAR, 1)
        weeks += 1
    return weeks


def yearsBetween(date_1, date_2):
    """Calculates the number of whole years between two dates.

    Daylight Saving Time changes are taken into account.

    Args:
        date_1 (Date): The first date to use.
        date_2 (Date): The second date to use.

    Returns:
        int: An integer that is representative of the difference between
            two dates.
    """
    cal = GregorianCalendar()
    cal.setTime(date_1)
    years = 0
    while cal.getTime().before(date_2):
        cal.add(Calendar.YEAR, 1)
        years += 1
    return years
