__all__ = ["BasicUser", "ContactInfo", "PyUser", "User"]

from typing import Any, List, Optional, Union

from com.inductiveautomation.ignition.common import QualifiedPath
from com.inductiveautomation.ignition.common.config import BasicProperty, Property
from com.inductiveautomation.ignition.common.user.schedule import ScheduleAdjustment
from java.lang import Object, String


class ContactInfo(Object):
    contactType = ""  # type: String
    value = ""  # type: String

    def __init__(self, *args):
        # type: (Any) -> None
        if len(args) == 2:
            self.contactType = args[0]
            self.value = args[1]

    def getContactType(self):
        # type: () -> String
        return self.contactType

    def getValue(self):
        # type: () -> String
        return self.value

    def setContactType(self, contactType):
        # type: (String) -> None
        self.contactType = contactType

    def setValue(self, value):
        # type: (String) -> None
        self.value = value


class User(object):
    Badge = BasicProperty("badge", str)  # type: BasicProperty
    DEFAULT_SCHEDULE_NAME = "Always"
    FirstName = BasicProperty("firstname", str)  # type: BasicProperty
    Language = BasicProperty("language", str, "en")  # type: BasicProperty
    LastName = BasicProperty("firstname", str)  # type: BasicProperty
    Notes = BasicProperty("notes", str)  # type: BasicProperty
    Password = BasicProperty("password", str)  # type: BasicProperty
    Schedule = BasicProperty("schedule", str, "Always")  # type: BasicProperty
    Username = BasicProperty("username", str)  # type: BasicProperty
    USERNAME_PATTERN = r"[\p{Alnum}][ @\w.\s\-]{1, 49}"

    def getContactInfo(self):
        # type: () -> List[ContactInfo]
        raise NotImplementedError

    def getId(self):
        # type: () -> Any
        raise NotImplementedError

    def getPath(self):
        # type: () -> QualifiedPath
        raise NotImplementedError

    def getProfileName(self):
        # type: () -> String
        raise NotImplementedError

    def getRoles(self):
        # type: () -> List[String]
        raise NotImplementedError

    def getScheduleAdjustments(self):
        # type: () -> List[ScheduleAdjustment]
        raise NotImplementedError


class BasicUser(User):
    def __init__(self, profileName, id, roles, contactInfo=None):
        self.profileName = profileName
        self.id = id
        self.roles = roles
        self.contactInfo = contactInfo

    def getContactInfo(self):
        pass

    def getId(self):
        pass

    def getPath(self):
        pass

    def getProfileName(self):
        pass

    def getRoles(self):
        pass

    def getScheduleAdjustments(self):
        pass


class PyUser(User):
    """A User implementation that delegates to another user object, but
    has some methods that are more scripting friendly.
    """

    _user = None  # type: Optional[User]

    def __init__(self, user=None):
        # type: (Optional[User]) -> None
        self._user = user

    def addContactInfo(self, *args):
        print(self, args)

    def addRole(self, role):
        print(self, role)

    def addRoles(self, roles):
        print(self, roles)

    def addScheduleAdjustment(self, start, end, available=True, note=None):
        print(self, start, end, available, note)

    def addScheduleAdjustments(self, scheduleAdjustments):
        print(self, scheduleAdjustments)

    def contains(self, prop):
        pass

    def get(self, propertyName):
        # type: (Union[Property, String]) -> Any
        print(self)
        return propertyName

    def getContactInfo(self):
        # type: () -> List[ContactInfo]
        ci_email = ContactInfo("email", "johdoe@mycompany.com")
        ci_phone = ContactInfo("phone", "+1 5551324567")
        ci_sms = ContactInfo("sms", "+1 5557654321")
        return [ci_email, ci_phone, ci_sms]

    def getCount(self):
        print(self)
        return 1

    def getId(self):
        pass

    def getOrDefault(self, prop):
        # type: (Property) -> Any
        print(self, prop)

    def getOrElse(self, property, value):
        # type: (Property, Any) -> Any
        pass

    def getPath(self):
        # type: () -> QualifiedPath
        pass

    def getProfileName(self):
        pass

    def getProperties(self):
        pass

    def getRoles(self):
        # type: () -> List[String]
        return ["Administrator", "Developer"]

    def getScheduleAdjustments(self):
        pass

    def getValues(self):
        pass

    def isExtended(self, prop):
        pass

    def isInherited(self, prop):
        pass

    def iterator(self):
        pass

    def merge(self, other, localOnly):
        pass

    def remove(self, prop):
        pass

    def removeContactInfo(self, contactType, value):
        # type: (String, String) -> None
        pass

    def removeRole(self, role):
        # type: (String) -> None
        pass

    def removeScheduleAdjustment(self, start, end, available=True, note=None):
        pass

    def set(self, *args):
        pass

    def setContactInfo(self, contactInfo):
        # type: (List[ContactInfo]) -> None
        pass

    def setRoles(self, roles):
        # type: (List[String]) -> None
        pass

    def setScheduleAdjustments(self, scheduleAdjustments):
        pass
