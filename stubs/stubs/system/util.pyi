from typing import Any, Callable, Dict, Iterable, List, Optional, Union

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.model import Version
from com.inductiveautomation.ignition.common.script.builtin import (
    DatasetUtilities,
    SystemUtilities,
)
from com.inductiveautomation.ignition.common.util import LoggerEx
from java.lang import Thread
from java.util import Date

APPLET_FLAG: int
CLIENT_FLAG: int
DESIGNER_FLAG: int
FULLSCREEN_FLAG: int
MOBILE_FLAG: int
PREVIEW_FLAG: int
SSL_FLAG: int
WEBSTART_FLAG: int
globals: Dict[Union[str, unicode], Any]

def audit(
    action: Union[str, unicode, None] = ...,
    actionValue: Union[str, unicode, None] = ...,
    auditProfile: Union[str, unicode] = ...,
    actor: Union[str, unicode, None] = ...,
    actorHost: Union[str, unicode] = ...,
    originatingSystem: Optional[List[Union[str, unicode]]] = ...,
    eventTimestamp: Optional[Date] = ...,
    originatingContext: int = ...,
    statusCode: int = ...,
) -> None: ...
def execute(commands: List[Union[str, unicode]]) -> None: ...
def getGatewayStatus(
    gatewayAddress: Union[str, unicode],
    connectTimeoutMillis: Optional[int] = ...,
    socketTimeoutMillis: Optional[int] = ...,
    bypassCertValidation: bool = ...,
) -> unicode: ...
def getGlobals() -> Dict[Union[str, unicode], Any]: ...
def getLogger(name: Union[str, unicode]) -> LoggerEx: ...
def getModules() -> BasicDataset: ...
def getProjectName() -> Union[str, unicode]: ...
def getProperty(propertyName: Union[str, unicode]) -> Optional[unicode]: ...
def getSessionInfo(
    usernameFilter: Union[str, unicode, None] = ...,
    projectFilter: Union[str, unicode, None] = ...,
) -> DatasetUtilities.PyDataSet: ...
def getVersion() -> Version: ...
def invokeAsynchronous(
    function: Callable[..., Any],
    args: Optional[Iterable[Any]] = ...,
    kwargs: Optional[Dict[Union[str, unicode], Any]] = ...,
    description: Union[str, unicode, None] = ...,
) -> Thread: ...
def jsonDecode(jsonString: Union[str, unicode]) -> Any: ...
def jsonEncode(
    pyObj: Iterable[Any], indentFactor: int = ...
) -> Union[str, unicode]: ...
def modifyTranslation(
    term: Union[str, unicode],
    translation: Union[str, unicode],
    locale: Union[str, unicode] = ...,
) -> None: ...
def queryAuditLog(
    auditProfileName: Union[str, unicode, None] = ...,
    startDate: Optional[Date] = ...,
    endDate: Optional[Date] = ...,
    actorFilter: Union[str, unicode, None] = ...,
    actionFilter: Union[str, unicode, None] = ...,
    targetFilter: Union[str, unicode, None] = ...,
    valueFilter: Union[str, unicode, None] = ...,
    systemFilter: Union[str, unicode, None] = ...,
    contextFilter: Optional[int] = ...,
) -> BasicDataset: ...
def sendMessage(
    project: Union[str, unicode],
    messageHandler: Union[str, unicode],
    payload: Optional[Dict[Union[str, unicode], Any]] = ...,
    scope: Union[str, unicode, None] = ...,
    clientSessionId: Union[str, unicode, None] = ...,
    user: Union[str, unicode, None] = ...,
    hasRole: Union[str, unicode, None] = ...,
    hostName: Union[str, unicode, None] = ...,
    remoteServers: Optional[List[Union[str, unicode]]] = ...,
) -> List[Union[str, unicode]]: ...
def sendRequest(
    project: Union[str, unicode],
    messageHandler: Union[str, unicode],
    payload: Optional[Dict[Union[str, unicode], Any]] = ...,
    hostName: Union[str, unicode, None] = ...,
    remoteServer: Union[str, unicode, None] = ...,
    timeoutSec: Union[str, unicode, None] = ...,
) -> Any: ...
def sendRequestAsync(
    project: Union[str, unicode],
    messageHandler: Union[str, unicode],
    payload: Optional[Dict[Union[str, unicode], Any]] = ...,
    hostName: Union[str, unicode, None] = ...,
    remoteServer: Union[str, unicode, None] = ...,
    timeoutSec: Optional[int] = ...,
    onSuccess: Optional[Callable[..., Any]] = ...,
    onError: Optional[Callable[..., Any]] = ...,
) -> SystemUtilities.RequestImpl: ...
def setLoggingLevel(
    loggerName: Union[str, unicode], loggerLevel: Union[str, unicode]
) -> None: ...
def threadDump() -> unicode: ...
def translate(
    term: Union[str, unicode],
    locale: Union[str, unicode] = ...,
    strict: Optional[bool] = ...,
) -> Union[str, unicode]: ...
