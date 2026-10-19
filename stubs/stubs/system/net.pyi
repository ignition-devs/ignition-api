from typing import List, Optional, Union

from com.inductiveautomation.ignition.common.script.builtin.http import JythonHttpClient

httpClient: JythonHttpClient

def getHostName() -> Union[str, unicode]: ...
def getIpAddress() -> Union[str, unicode]: ...
def getRemoteServers(
    runningOnly: Optional[bool] = ...,
) -> List[Union[str, unicode]]: ...
def sendEmail(
    smtp: Union[str, unicode, None] = ...,
    fromAddr: Union[str, unicode] = ...,
    subject: Union[str, unicode, None] = ...,
    body: Union[str, unicode, None] = ...,
    html: bool = ...,
    to: Optional[List[Union[str, unicode]]] = ...,
    attachmentNames: Optional[List[object]] = ...,
    attachmentData: Optional[List[object]] = ...,
    timeout: int = ...,
    username: Union[str, unicode, None] = ...,
    password: Union[str, unicode, None] = ...,
    priority: Union[str, unicode] = ...,
    smtpProfile: Union[str, unicode, None] = ...,
    cc: Optional[List[Union[str, unicode]]] = ...,
    bcc: Optional[List[Union[str, unicode]]] = ...,
    retries: int = ...,
    replyTo: Optional[List[Union[str, unicode]]] = ...,
) -> None: ...
