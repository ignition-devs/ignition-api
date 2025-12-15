"""Net Functions.

The following functions give you access to interact with http services.
"""

from __future__ import print_function

__all__ = [
    "getHostName",
    "getIpAddress",
    "getRemoteServers",
    "httpClient",
    "sendEmail",
]

import socket
from typing import Any, Callable, List, Optional, Union

from java.lang import IllegalArgumentException

from com.inductiveautomation.ignition.common.script.builtin.http import JythonHttpClient


def getHostName():
    # type: () -> Union[str, unicode]
    """Returns the host name of the computer that the script was ran on.

    When run in the Gateway scope, returns the Gateway hostname. When
    run in the Client scope, returns the Client hostname. On Windows,
    this is typically the "computer name". For example, might return
    EAST_WING_WORKSTATION or bobs-laptop.

    Returns:
        The hostname of the local machine.
    """
    return socket.gethostname()


def getIpAddress():
    # type: () -> Union[str, unicode]
    """Returns the IP address of the computer that the script was ran
    on.

    Returns:
        Returns the IP address of the local machine, as it sees it.
    """
    return socket.gethostbyname(str(getHostName()))


def getRemoteServers(runningOnly=True):
    # type: (Optional[bool]) -> List[Union[str, unicode]]
    """This function returns a List of Gateway Network servers that are
    visible from the local Gateway.

    Args:
        runningOnly: If set to True, only servers on the Gateway Network
            that are running will be returned. Servers that have lost
            contact with the Gateway Network will be filtered out.
            Optional.

    Returns:
        A List of strings representing Gateway Network Server IDs.
    """
    print(runningOnly)
    return []


def httpClient(
    timeout=60000,  # type: int
    bypass_cert_validation=False,  # type: bool
    username=None,  # type: Union[str, unicode, None]
    password=None,  # type: Union[str, unicode, None]
    proxy=None,  # type: Union[str, unicode, None]
    cookie_policy="ACCEPT_ORIGINAL_SERVER",  # type: Union[str, unicode]
    redirect_policy="NORMAL",  # type: Union[str, unicode]
    version="HTTP_2",  # type: Union[str, unicode]
    customizer=None,  # type: Optional[Callable[..., Any]]
):
    # type: (...) -> JythonHttpClient
    """Provides a general use object that can be used to send and
    receive HTTP requests.

    The object created by this function is a wrapper around Java's
    HttpClient class. Usage requires creating a JythonHttpClient object
    with a call to system.net.httpClient, then calling a method (such as
    get(), post()) on the JythonHttpClient to actually issue a request.

    Args:
        timeout: A value, in milliseconds, to set the client's connect
            timeout setting to. Defaults to 60000. Optional.
        bypass_cert_validation: A boolean indicating whether the client
            should attempt to validate the certificates of remote
            servers, if connecting via HTTPS/SSL. Defaults to False.
            Optional.
        username: A string indicating the username to use for
            authentication if the remote server requests authentication;
            specifically, by responding with a WWW-Authenticate or
            Proxy-Authenticate header. Only supports Basic
            authentication. If username is specified but not password,
            an empty string will be used for the password in the Basic
            Authentication response. Defaults to None. Optional.
        password: A string indicating the password to use for
            authentication. Defaults to None. Optional.
        proxy: The address of a proxy server, which will be used for
            HTTP and HTTPS traffic. If a port is not specified as part
            of that address, it will be assumed from the protocol in the
            URL, i.e. 80/443. Defaults to None. Optional.
        cookie_policy: A string representing this client's cookie
            policy. Accepts values "ACCEPT_ALL", "ACCEPT_NONE", and
            "ACCEPT_ORIGINAL_SERVER". Defaults to
            "ACCEPT_ORIGINAL_SERVER". Optional.
        redirect_policy: A string representing this client's redirect
            policy. Acceptable values are listed below. Defaults to
            "Normal". Optional.
        version: A string specifying either HTTP_2 or HTTP_1_1 for the
            HTTP protocol. When omitted, the previous default of HTTP_2
            is implied. Optional.
        customizer: A reference to a function. This function will be
            called with one argument (an instance of
            HttpClient.Builder). The function should operate on that
            builder instance, which allows for customization of the
            created HTTP client. Defaults to None. Optional.

    Returns:
        An object wrapped around an instance of Java's HttpClient class.
        The httpClient object has methods that can be called to execute
        HTTP requests against a server.
    """
    print(
        timeout,
        bypass_cert_validation,
        username,
        password,
        proxy,
        cookie_policy,
        redirect_policy,
        version,
        customizer,
    )
    return JythonHttpClient()


def _sendEmail(
    smtpSettings,  # type: Union[str, unicode, None]
    fromAddr,  # type: Union[str, unicode]
    subject=None,  # type: Union[str, unicode, None]
    body=None,  # type: Union[str, unicode, None]
    html=False,  # type: bool
    to=None,  # type: Optional[List[Union[str, unicode]]]
    attachmentNames=None,  # type: Optional[List[object]]
    attachmentData=None,  # type: Optional[List[object]]
    timeout=300000,  # type: int
    username=None,  # type: Union[str, unicode, None]
    password=None,  # type: Union[str, unicode, None]
    priority="3",  # type: Union[str, unicode]
    cc=None,  # type: Optional[List[Union[str, unicode]]]
    bcc=None,  # type: Optional[List[Union[str, unicode]]]
    retries=0,  # type: int
    replyTo=None,  # type: Optional[List[Union[str, unicode]]]
):
    # type: (...) -> None
    _to = [] if to is None else to
    _cc = [] if cc is None else cc
    _bcc = [] if bcc is None else bcc
    recipients = _to + _cc + _bcc
    if smtpSettings and fromAddr and len(recipients) > 0:
        print(
            smtpSettings,
            fromAddr,
            subject,
            body,
            html,
            to,
            attachmentNames,
            attachmentData,
            timeout,
            username,
            password,
            priority,
            cc,
            bcc,
            retries,
            replyTo,
        )
    else:
        raise IllegalArgumentException(
            "Cannot send email without SMTP host, from address and recipient list."
        )


def sendEmail(
    smtp=None,  # type: Union[str, unicode, None]
    fromAddr="",  # type: Union[str, unicode]
    subject=None,  # type: Union[str, unicode, None]
    body=None,  # type: Union[str, unicode, None]
    html=False,  # type: bool
    to=None,  # type: Optional[List[Union[str, unicode]]]
    attachmentNames=None,  # type: Optional[List[object]]
    attachmentData=None,  # type: Optional[List[object]]
    timeout=300000,  # type: int
    username=None,  # type: Union[str, unicode, None]
    password=None,  # type: Union[str, unicode, None]
    priority="3",  # type: Union[str, unicode]
    smtpProfile=None,  # type: Union[str, unicode, None]
    cc=None,  # type: Optional[List[Union[str, unicode]]]
    bcc=None,  # type: Optional[List[Union[str, unicode]]]
    retries=0,  # type: int
    replyTo=None,  # type: Optional[List[Union[str, unicode]]]
):
    # type: (...) -> None
    """Sends an email through the given SMTP server.

    Note that this email is relayed first through the Gateway - the
    client host machine doesn't need network access to the SMTP server.

    Args:
        smtp: The address of an SMTP server to send the email through,
            like "mail.example.com". A port can be specified, like
            "mail.example.com:25". SSL can also be forced, like
            "mail.example.com:25:tls".
        fromAddr: An email address to have the email come from.
        subject: The subject line for the email. Optional.
        body: The body text of the email. Optional.
        html: A flag indicating whether or not to send the email as an
            HTML email. Will auto-detect if omitted. Optional.
        to: A list of email addresses to send to.
        attachmentNames: A list of attachment names. Attachment names
            must have the correct extension for the file type or an
            error will occur. Optional.
        attachmentData: A list of attachment data, in binary format.
        timeout: A timeout for the email, specified in milliseconds.
            Defaults to 5 minutes (60,000*5). Optional.
        username: If specified, will be used to authenticate with the
            SMTP host. Optional.
        password: If specified, will be used to authenticate with the
            SMTP host. Optional.
        priority: Priority for the message, from "1" to "5", with "1"
            being highest priority. Defaults to "3" (normal) priority.
            Optional.
        smtpProfile: If specified, the named SMTP profile defined
            in the Gateway will be used. If this keyword is present, the
            smtp, username, and password keywords will be ignored.
            Optional.
        cc: A list of email addresses to carbon copy. Only available if
            a smtpProfile is used. Optional.
        bcc: A list of email addresses to blind carbon copy. Only
            available if a smtpProfile is used. Optional.
        retries: The number of additional times to retry sending on
            failure. Defaults to 0. Only available if a smtpProfile is
            used. Optional.
        replyTo: An optional list of addresses to have the recipients
            reply to. If omitted, this defaults to the from address.
            Optional.
    """
    if not smtpProfile:
        _sendEmail(
            smtp,
            fromAddr,
            subject,
            body,
            html,
            to,
            attachmentNames,
            attachmentData,
            timeout,
            username,
            password,
            priority,
            retries=retries,
            replyTo=replyTo,
        )
    else:
        _sendEmail(
            smtpProfile,
            fromAddr,
            subject,
            body,
            html,
            to,
            attachmentNames,
            attachmentData,
            timeout,
            priority=priority,
            cc=cc,
            bcc=bcc,
            retries=retries,
            replyTo=replyTo,
        )
