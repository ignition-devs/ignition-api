"""User Functions.

The following functions give you access to view and edit users in the
Gateway.
"""

from __future__ import print_function

__all__ = [
    "addHoliday",
    "addRole",
    "addSchedule",
    "editHoliday",
    "editRole",
    "editSchedule",
    "getHoliday",
    "getHolidayNames",
    "getHolidays",
    "getRoles",
    "getSchedule",
    "getScheduleNames",
    "getScheduledUsers",
    "getSchedules",
    "getUser",
    "getUsers",
    "isUserScheduled",
    "removeHoliday",
    "removeRole",
    "removeSchedule",
]

from typing import List, Optional, Union

from com.inductiveautomation.ignition.client.util.gui.scheduling import ScheduleModel
from com.inductiveautomation.ignition.common.messages import UIResponse
from com.inductiveautomation.ignition.common.user import PyUser
from com.inductiveautomation.ignition.common.user.schedule import (
    AbstractScheduleModel,
    HolidayModel,
)
from java.lang import String
from java.util import Date, Locale


def addHoliday(holiday):
    # type: (HolidayModel) -> UIResponse
    """Allows a holiday to be added.

    Args:
        holiday: The holiday to add.

    Returns:
        An object with lists of warnings, errors, and info about the
        success or failure of the add.
    """
    print(holiday)
    return UIResponse(Locale.ENGLISH)


def addRole(userSource, role):
    # type: (String, String) -> UIResponse
    """Allows a role to the specified user source.

    When altering the Gateway System User Source, the Allow User Admin
    setting must be enabled.

    Args:
        userSource: The user source to add a role to. Blank will use the
            default user source.
        role: The role to add. Role must not be blank and must not
            already exist.

    Returns:
        An object with lists of warnings, errors, and info about the
        success or failure of the add.
    """
    print(userSource, role)
    return UIResponse(Locale.ENGLISH)


def addSchedule(schedule):
    # type: (AbstractScheduleModel) -> UIResponse
    """Allows a schedule to be added.

    Args:
        schedule: The schedule to add.

    Returns:
        An object with lists of warnings, errors, and info about the
        success or failure of the add.
    """
    print(schedule)
    return UIResponse(Locale.ENGLISH)


def editHoliday(holidayName, holiday):
    # type: (String, HolidayModel) -> UIResponse
    """Allows a holiday to be edited.

    Args:
        holidayName: The name of the holiday to edit. Name is
            case-sensitive.
        holiday: The edited holiday.

    Returns:
        An object with lists of warnings, errors, and info about the
        success or failure of the edit.
    """
    print(holidayName, holiday)
    return UIResponse(Locale.ENGLISH)


def editRole(
    userSource,  # type: String
    oldName,  # type: String
    newName,  # type: String
):
    # type: (...) -> UIResponse
    """Renames a role in the specified user source.

    When altering the Gateway System User Source, the Allow User Admin
    setting must be enabled.

    Args:
        userSource: The user source in which the role is found. Blank
            will use the default user source.
        oldName: The role to edit. Role must not be blank and must
            exist.
        newName: The new name for the role. Must not be blank.

    Returns:
        An object with lists of warnings, errors, and info about the
        success or failure of the edit.
    """
    print(userSource, oldName, newName)
    return UIResponse(Locale.ENGLISH)


def editSchedule(scheduleName, schedule):
    # type: (String, AbstractScheduleModel) -> UIResponse
    """Allows a schedule to be edited.

    Args:
        scheduleName: The name of the schedule to edit. Name is
            case-sensitive.
        schedule: The edited schedule.

    Returns:
        An object with lists of warnings, errors, and info about the
        success or failure of the edit.
    """
    print(scheduleName, schedule)
    return UIResponse(Locale.ENGLISH)


def getHoliday(holidayName):
    # type: (String) -> HolidayModel
    """Returns a specific holiday.

    Args:
        holidayName: The name of the holiday to return. Case-sensitive.

    Returns:
        The holiday, or None if not found.
    """
    print(holidayName)
    return HolidayModel(holidayName, Date(), True)


def getHolidayNames():
    # type: () -> List[String]
    """Returns a collection of Strings of all holiday names.

    Returns:
        A list of all holiday names, or an empty list if no holidays are
        defined.
    """
    return ["Cinco de mayo", "Labor Day", "Groundhog Day"]


def getHolidays():
    # type: () -> List[HolidayModel]
    """Returns a sequence of all of the holidays available.

    Returns:
        A list of holidays.
    """
    return [HolidayModel("Cinco de mayo", Date(), True)]


def getRoles(userSource):
    # type: (String) -> List[String]
    """Returns a sequence of strings representing all of the roles
    configured in a specific user source.

    Args:
        userSource: The user source to fetch the roles for.

    Returns:
        A List of Strings that holds all the roles in the user source.
    """
    print(userSource)
    return ["Administrator", "Designer", "Developer"]


def getSchedule(scheduleName):
    # type: (String) -> AbstractScheduleModel
    """Returns a specific schedule.

    Args:
        scheduleName: The name of the schedule to return.
            Case-sensitive.

    Returns:
         The schedule, which can be a BasicSchedule, CompositeSchedule,
         or another type registered by a module, or None if not found.
    """
    print(scheduleName)
    return AbstractScheduleModel()


def getScheduleNames():
    # type: () -> List[String]
    """Returns a sequence of strings representing the names of all of
    the schedules available.

    Returns:
        A List of Strings that holds the names of all the available
        schedules.
    """
    return ["A", "Always", "B", "C", "Example", "MyComposite", "MySchedule"]


def getScheduledUsers(
    userSource,  # type: String
    date=None,  # type: Optional[Union[Date, int]]
):
    # type: (...) -> List[PyUser]
    """Returns a list of users that are scheduled on.

    If no users are scheduled, it will return an empty list.

    Args:
        userSource: The name of the user source to check for scheduled
            users.
        date: The date to check schedules for. May be a Java Date or
        Unix Time in ms.. If omitted, the current date and time will be
        used. Optional.

    Returns:
        List of all Users scheduled for the given date, taking schedule
        adjustments into account.
    """
    print(userSource, date)
    return [PyUser()]


def getSchedules():
    # type: () -> List[ScheduleModel]
    """Returns a sequence of all available schedule models, which can be
    used to return configuration information on the schedule, such as
    time for each day of the week.

    Returns:
        A list of ScheduleModel objects. ScheduleModel objects can be a
        Basic Schedule, Composite Schedule (composed of exactly two
        other schedules), or another type registered by a module.
    """
    return [ScheduleModel()]


def getUser(userSource, username):
    # type: (String, String) -> PyUser
    """Looks up a specific user in a user source, by username.

    The full User object is returned except for the user's password.

    Args:
        userSource: The name of the user source to search for the user
            in.
        username: The username of the user to search for.

    Returns:
        A User object.
    """
    print(userSource, username)
    return PyUser()


def getUsers(userSource):
    # type: (String) -> List[PyUser]
    """Retrieves the list of users in a specific user source.

    The User objects that are returned contain all of the information
    about that user, except for the user's password.

    Args:
        userSource: The name of the user source to find the users in.

    Returns:
        A list of User objects.
    """
    print(userSource)
    return [PyUser()]


def isUserScheduled(user, date=None):
    # type: (PyUser, Optional[Union[Date, int]]) -> bool
    """Will check if a specified User is scheduled currently or on a
    specified date/time.

    Args:
        user: The user object to check the schedule for.
        date: The date to check schedules for. May be a Java Date or
            Unix Time in ms. If omitted, the current date and time
            will be used. Optional.

    Returns:
        True if the user is scheduled for the specified date, False if
        not.
    """
    print(user, date)
    return True


def removeHoliday(holidayName):
    # type: (String) -> UIResponse
    """Allows a holiday to be deleted.

    Args:
        holidayName: The name of the holiday to delete. Name is
            case-sensitive.

    Returns:
        An object with lists of warnings, errors, and info about the
        success or failure of the deletion.
    """
    print(holidayName)
    return UIResponse(Locale.ENGLISH)


def removeRole(userSource, role):
    # type: (String, String) -> UIResponse
    """Removes a role from the specified user source.

    When altering the Gateway System User Source, the Allow User Admin
    setting must be enabled.

    Args:
        userSource: The user source in which the role is found. Blank
            will use the default user source.
        role: The role to remove. The role must exist.

    Returns:
        An object with lists of warnings, errors, and info about the
        success or failure of the deletion.
    """
    print(userSource, role)
    return UIResponse(Locale.ENGLISH)


def removeSchedule(scheduleName):
    # type: (String) -> UIResponse
    """Allows a schedule to be deleted.

    Note that schedules which are used in Composite Schedules can not be
    deleted until they are removed from the Composite Schedule.

    Args:
        scheduleName: The name of the schedule to delete. Name is
            case-sensitive.

    Returns:
        An object with lists of warnings, errors, and info about the
        success or failure of the deletion.
    """
    print(scheduleName)
    return UIResponse(Locale.ENGLISH)
