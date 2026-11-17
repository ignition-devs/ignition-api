from __future__ import print_function

__all__ = [
    "Call",
    "CallCreator",
    "CallDeleter",
    "CallFetcher",
    "CallReader",
    "CallUpdater",
]

from typing import Any, List, Union

from java.lang import Enum
from java.net import URI

from com.twilio.base import Creator, Deleter, Fetcher, Reader, Resource, Updater
from com.twilio.http import HttpMethod
from com.twilio.type import PhoneNumber
from org.joda.time import DateTime


class CallCreator(Creator):
    def __init__(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        super(CallCreator, self).__init__()
        print(args, kwargs)

    def setApplicationSid(self, applicationSid):
        # type: (Union[str, unicode]) -> CallCreator
        pass

    def setFallbackMethod(self, fallbackMethod):
        # type: (HttpMethod) -> CallCreator
        pass

    def setFallbackUrl(self, fallbackUrl):
        # type: (Union[str, unicode, URI]) -> CallCreator
        pass

    def setIfMachine(self, ifMachine):
        # type: (Union[str, unicode]) -> CallCreator
        pass

    def setMachineDetection(self, machineDetection):
        # type: (Union[str, unicode]) -> CallCreator
        pass

    def setMachineDetectionTimeout(self, machineDetectionTimeout):
        # type: (int) -> CallCreator
        pass

    def setMethod(self, method):
        # type: (HttpMethod) -> CallCreator
        pass

    def setRecord(self, record):
        # type: (bool) -> CallCreator
        pass

    def setRecordingChannels(self, recordingChannels):
        # type: (Union[str, unicode]) -> CallCreator
        pass

    def setRecordingStatusCallback(self, recordingStatusCallback):
        # type: (Union[str, unicode]) -> CallCreator
        pass

    def setRecordingStatusCallbackMethod(self, recordingStatusCallbackMethod):
        # type: (HttpMethod) -> CallCreator
        pass

    def setSendDigits(self, sendDigits):
        # type: (Union[str, unicode]) -> CallCreator
        pass

    def setSipAuthPassword(self, sipAuthPassword):
        # type: (Union[str, unicode]) -> CallCreator
        pass

    def setSipAuthUsername(self, sipAuthUsername):
        # type: (Union[str, unicode]) -> CallCreator
        pass

    def setStatusCallback(self, statusCallback):
        # type: (Union[str, unicode, URI]) -> CallCreator
        pass

    def setStatusCallbacEvent(
        self,
        statusCallbackEvent,  # type: Union[str, unicode, List[Union[str, unicode]]]
    ):
        # type: (...) -> CallCreator
        pass

    def setStatusCallbackMethod(self, statusCallbackMethod):
        # type: (HttpMethod) -> CallCreator
        pass

    def setTimeout(self, timeout):
        # type: (int) -> CallCreator
        pass

    def setUrl(self, url):
        # type: (Union[str, unicode, URI]) -> CallCreator
        pass


class Call(Resource):
    class Status(Enum):
        BUSY = "busy"
        CANCELED = "canceled"
        COMPLETED = "completed"
        FAILED = "failed"
        IN_PROGRESS = "in-progress"
        NO_ANSWER = "no-answer"
        QUEUED = "queued"
        RINGING = "ringing"

    class UpdateStatus(Enum):
        CANCELED = "canceled"
        COMPLETED = "completed"

        @staticmethod
        def forValue(value):
            # type: (Union[str, unicode]) -> Call.UpdateStatus
            pass

        @staticmethod
        def values():
            # type: () -> List[Call.UpdateStatus]
            pass

    @staticmethod
    def forValue(value):
        # type: (Union[str, unicode]) -> Call.Status
        pass

    @staticmethod
    def values():
        # type: () -> List[Call.Status]
        pass

    @staticmethod
    def creator(*args, **kwargs):
        # type: (*Any, **Any) -> CallCreator
        print(args, kwargs)
        return CallCreator()

    @staticmethod
    def deleter(*args):
        # type: (*Union[str, unicode]) -> CallDeleter
        pass

    @staticmethod
    def fetcher(*args):
        # type: (*Union[str, unicode]) -> CallFetcher
        pass

    @staticmethod
    def fromJson(*args):
        # type: (*Any) -> Call
        pass

    def getAccountSid(self):
        # type: () -> Union[str, unicode]
        pass

    def getAnnotation(self):
        # type: () -> Union[str, unicode]
        pass

    def getAnsweredBy(self):
        # type: () -> Union[str, unicode]
        pass

    def getApiVersion(self):
        # type: () -> Union[str, unicode]
        pass

    def getCallerName(self):
        # type: () -> Union[str, unicode]
        pass

    def getDateCreated(self):
        # type: () -> DateTime
        pass

    def getDateUpdated(self):
        # type: () -> DateTime
        pass

    def getDuration(self):
        # type: () -> Union[str, unicode]
        pass

    def getEndTime(self):
        # type: () -> DateTime
        pass

    def getForwardedFrom(self):
        # type: () -> Union[str, unicode]
        pass

    def getFrom(self):
        # type: () -> Union[str, unicode]
        pass

    def getFromFormatted(self):
        # type: () -> Union[str, unicode]
        pass

    def getGroupSid(self):
        # type: () -> Union[str, unicode]
        pass

    def getParentCallSid(self):
        # type: () -> Union[str, unicode]
        pass

    def getPhoneNumberSid(self):
        # type: () -> Union[str, unicode]
        pass

    def getSid(self):
        # type: () -> Union[str, unicode]
        pass

    def getStartTime(self):
        # type: () -> DateTime
        pass

    def getStatus(self):
        # type: () -> Call.Status
        pass

    def getTo(self):
        # type: () -> Union[str, unicode]
        pass

    def getUri(self):
        # type: () -> Union[str, unicode]
        pass

    @staticmethod
    def reader(pathAccountSid=None):
        # type: (Union[str, unicode, None]) -> CallReader
        pass

    @staticmethod
    def updater(*args):
        # type: (*Union[str, unicode]) -> CallUpdater
        pass


class CallDeleter(Deleter):
    def __init__(self, *args):
        # type: (*Union[str, unicode]) -> None
        print(args)
        super(CallDeleter, self).__init__()


class CallFetcher(Fetcher):
    def __init__(self, *args):
        # type: (*Union[str, unicode]) -> None
        print(args)
        super(CallFetcher, self).__init__()


class CallReader(Reader):
    def __init__(self, pathAccountSid=None):
        # type: (Union[str, unicode, None]) -> None
        super(CallReader, self).__init__()
        print(pathAccountSid)

    def setEndTime(self, absoluteEndTime):
        # type: (DateTime) -> CallReader
        pass

    def setFrom(self, from_):
        # type: (PhoneNumber) -> CallReader
        pass

    def setParentCallSid(self, parentCallSid):
        # type: (Union[str, unicode]) -> CallReader
        pass

    def setStartTime(self, absoluteStartTime):
        # type: (DateTime) -> CallReader
        pass

    def setStatus(self, status):
        # type: (Call.Status) -> CallReader
        pass

    def setTo(self, to):
        # type: (PhoneNumber) -> CallReader
        pass


class CallUpdater(Updater):
    def __init__(self, *args):
        # type: (*Union[str, unicode]) -> None
        print(args)
        super(CallUpdater, self).__init__()

    def setFallbackMethod(self, fallbackMethod):
        # type: (HttpMethod) -> CallUpdater
        pass

    def setFallbackUrl(self, fallbackUrl):
        # type: (Union[str, unicode, URI]) -> CallUpdater
        pass

    def setMethod(self, method):
        # type: (HttpMethod) -> CallUpdater
        pass

    def setStatus(self, status):
        # type: (Call.UpdateStatus) -> CallUpdater
        pass

    def setStatusCallback(self, statusCallback):
        # type: (Union[str, unicode, URI]) -> CallUpdater
        pass

    def setUrl(self, url):
        # type: (Union[str, unicode, URI]) -> CallUpdater
        pass
