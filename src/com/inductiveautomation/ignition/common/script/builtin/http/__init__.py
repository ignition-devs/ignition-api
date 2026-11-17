from __future__ import print_function

__all__ = ["CookieManager", "JythonHttpClient", "Promise", "Response"]

from typing import Any, Callable, Dict, Optional, Union

from java.lang import Object
from java.net import CookieManager as JCookieManager
from java.net.http import HttpClient, HttpRequest, HttpResponse
from java.nio.charset import Charset
from java.util.concurrent import CompletableFuture

from com.inductiveautomation.ignition.common.gson import Gson
from org.python.core import PyObject


class CookieManager(JCookieManager):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(CookieManager, self).__init__()
        print(args)


class JythonHttpClient(Object):
    """A Jython-optimized wrapper around the base HttpClient available
    in Java 11+.

    Mostly, through convenience functions that make things easier to use
    from Jython.
    """

    def delete(self, *args, **kwargs):
        # type: (*Any, **Union[str, unicode]) -> Response
        pass

    def deleteAsync(self, *args, **kwargs):
        # type: (*Any, **Union[str, unicode]) -> Promise
        pass

    def get(self, *args, **kwargs):
        # type: (*Any, **Union[str, unicode]) -> Response
        pass

    def getAsync(self, *args, **kwargs):
        # type: (*Any, **Union[str, unicode]) -> Promise
        pass

    def getConnectTimeout(self):
        # type: () -> long
        pass

    def getCookieManager(self):
        # type: () -> CookieManager
        pass

    def getJavaClient(self):
        # type: () -> HttpClient
        pass

    def getRedirectPolicy(self):
        # type: () -> Union[str, unicode]
        pass

    def getVersion(self):
        # type: () -> Union[str, unicode]
        pass

    def head(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Response
        pass

    def headAsync(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Promise
        pass

    def options(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Response
        pass

    def optionsAsync(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Promise
        pass

    def parseChart(self, contentType):
        # type: (Union[str, unicode]) -> Optional[Charset]
        pass

    def patch(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Response
        pass

    def patchAsync(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Promise
        pass

    def post(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Response
        pass

    def postAsync(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Promise
        pass

    def put(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Response
        pass

    def putAsync(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Promise
        pass

    def request(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Response
        pass

    def requestAsync(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Promise
        pass

    def setGson(self, gson):
        # type: (Gson) -> None
        pass

    def trace(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Response
        pass

    def traceAsync(
        self,
        url,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        data=None,  # type: Optional[Any]
        file=None,  # type: Union[str, unicode, None]
        headers=None,  # type: Optional[Dict[Union[str, unicode], Any]]
        username=None,  # type: Union[str, unicode, None]
        password=None,  # type: Union[str, unicode, None]
        timeout=None,  # type: Optional[long]
    ):
        # type: (...) -> Promise
        pass

    def __call__(
        self,
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

        Usage requires creating a JythonHttpClient object with a call to
        system.net.httpClient, then calling a method (such as get(),
        post()) on the JythonHttpClient to actually issue a request. In
        Ignition 8.3, system.net.httpClient may also be used directly as
        a JythonHttpClient instance, so a call such as
        system.net.httpClient.get(parameters) is equivalent to
        system.net.httpClient().get(parameters).

        Args:
            timeout: A value, in milliseconds, to set the client's
                connect timeout setting to. Defaults to 60000. Optional.
            bypass_cert_validation: A boolean indicating whether the
                client should attempt to validate the certificates of
                remote servers, if connecting via HTTPS/SSL. Defaults to
                False. Optional.
            username: A string indicating the username to use for
                authentication if the remote server requests
                authentication; specifically, by responding with a
                WWW-Authenticate or Proxy-Authenticate header. Only
                supports Basic authentication. If username is specified
                but not password, an empty string will be used for the
                password in the Basic Authentication response. Defaults
                to None. Optional.
            password: A string indicating the password to use for
                authentication. Defaults to None. Optional.
            proxy: The address of a proxy server, which will be used for
                HTTP and HTTPS traffic. If a port is not specified as
                part of that address, it will be assumed from the
                protocol in the URL, i.e. 80/443. Defaults to None.
                Optional.
            cookie_policy: A string representing this client's cookie
                policy. Accepts values "ACCEPT_ALL", "ACCEPT_NONE", and
                "ACCEPT_ORIGINAL_SERVER". Defaults to
                "ACCEPT_ORIGINAL_SERVER". Optional.
            redirect_policy: A string representing this client's
                redirect policy. Acceptable values are listed below.
                Defaults to "Normal". Optional.
            version: A string specifying either HTTP_2 or HTTP_1_1 for
                the HTTP protocol. When omitted, the previous default of
                HTTP_2 is implied. Optional.
            customizer: A reference to a function. This function will be
                called with one argument (an instance of
                HttpClient.Builder). The function should operate on that
                builder instance, which allows for customization of the
                created HTTP client. Defaults to None. Optional.

        Returns:
            An object wrapped around an instance of Java's HttpClient
            class. The httpClient object has methods that can be called
            to execute HTTP requests against a server.
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


class Promise(Object):
    def cancel(self):
        # type: () -> bool
        return True

    def get(self, *args, **kwargs):
        # type: (*Any, **Union[str, unicode]) -> Any
        pass

    def getFuture(self):
        # type: () -> CompletableFuture
        pass

    def handleException(self, callback):
        # type: (PyObject) -> Promise
        pass

    def isDone(self):
        # type: () -> bool
        return True

    def then(self, callback):
        # type: (PyObject) -> Promise
        pass

    def whenComplete(self, callback):
        # type: (PyObject) -> None
        pass


class Response(Object):
    class RequestWrapper(Object):
        def __init__(self, *args):
            # type: (*Any) -> None
            super(Response.RequestWrapper, self).__init__()
            print(args)

        def getHeaders(self):
            # type: () -> Any
            pass

        def getJavaRequest(self):
            # type: () -> HttpRequest
            pass

        def getMethod(self):
            # type: () -> Union[str, unicode]
            pass

        def getTimeout(self):
            # type: () -> long
            pass

        def getUrl(self):
            # type: () -> Union[str, unicode]
            pass

        def getVersion(self):
            # type: () -> Union[str, unicode]
            pass

    def __init__(self, httpResponse, client):
        # type: (HttpResponse, JythonHttpClient) -> None
        super(Response, self).__init__()
        print(httpResponse, client)

    @property
    def body(self):
        # type: () -> Any
        pass

    @property
    def clientError(self):
        # type: () -> bool
        return True

    @property
    def cookieManager(self):
        # type: () -> CookieManager
        return self.getCookieManager()

    @property
    def good(self):
        # type: () -> bool
        return True

    @property
    def headers(self):
        # type: () -> Dict[Union[str, unicode], Any]
        return self.getHeaders()

    @property
    def javaResponse(self):
        # type: () -> HttpResponse
        return self.getJavaResponse()

    @property
    def json(self):
        # type: () -> Dict[Union[str, unicode], Any]
        return self.getJson()

    @property
    def request(self):
        # type: () -> Response.RequestWrapper
        return self.getRequest()

    @property
    def serverError(self):
        # type: () -> bool
        return self.isServerError()

    @property
    def statusCode(self):
        # type: () -> int
        return self.getStatusCode()

    @property
    def text(self):
        # type: () -> Union[str, unicode]
        return self.getText()

    @property
    def url(self):
        # type: () -> Union[str, unicode]
        return self.getUrl()

    def getBody(self):
        # type: () -> Any
        pass

    def getCookieManager(self):
        # type: () -> CookieManager
        pass

    def getHeaders(self):
        # type: () -> Dict[Union[str, unicode], Any]
        pass

    def getJavaResponse(self):
        # type: () -> HttpResponse
        pass

    def getJson(self, *args, **kwargs):
        # type: (*Any, **Any) -> Dict[Union[str, unicode], Any]
        pass

    def getRequest(self):
        # type: () -> Response.RequestWrapper
        pass

    def getStatusCode(self):
        # type: () -> int
        pass

    def getText(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, unicode]
        pass

    def getUrl(self):
        # type: () -> Union[str, unicode]
        pass

    def isClientError(self):
        # type: () -> bool
        return True

    def isGood(self):
        # type: () -> bool
        return True

    def isServerError(self):
        # type: () -> bool
        return True
