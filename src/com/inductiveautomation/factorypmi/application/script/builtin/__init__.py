from __future__ import print_function

__all__ = [
    "ClientDatasetUtilities",
    "ClientPrintUtilities",
    "ClientSystemUtilities",
    "INavUtilities",
    "NavUtilities",
    "VisionUtilities",
    "WindowUtilities",
]

from typing import Any, Dict, List, Optional, Tuple, Union

from java.awt import Color, Component, Graphics
from java.awt.event import ActionEvent, ComponentEvent, MouseEvent
from java.awt.image import BufferedImage
from java.awt.print import PageFormat
from java.lang import Number, Object
from java.util import EventObject, Locale
from javax.swing import JComponent, JFrame, JPopupMenu

from com.inductiveautomation.factorypmi.application import FPMIApp, FPMIWindow
from com.inductiveautomation.factorypmi.application.script import PyComponentWrapper
from com.inductiveautomation.ignition.common.i18n.keyboard import KeyboardLayout
from com.inductiveautomation.ignition.common.model.values import QualityCode
from org.python.core import PyObject, PySequence, PyTuple


class INavUtilities(object):
    """Parent interface to coordinate the functions between NavUtilities
    and NavUtilitiesDispatcher.
    """

    def centerWindow(self, arg):
        # type: (Union[str, unicode, FPMIWindow]) -> None
        raise NotImplementedError

    def closeParentWindow(self, event):
        # type: (EventObject) -> None
        raise NotImplementedError

    def closeWindow(self, arg):
        # type: (Union[str, unicode, FPMIWindow]) -> None
        raise NotImplementedError

    def getCurrentWindow(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def goBack(self):
        # type: () -> PyObject
        raise NotImplementedError

    def goForward(self):
        # type: () -> PyObject
        raise NotImplementedError

    def goHome(self):
        # type: () -> PyObject
        raise NotImplementedError

    def openWindow(
        self,
        path,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    ):
        # type: (...) -> PyObject
        raise NotImplementedError

    def openWindowImpl(
        self,
        path,  # type: Union[str, unicode]
        params,  # type: Dict[Union[str, unicode], Any]
        openAdditional,  # type: bool
    ):
        # type: (...) -> PyObject
        raise NotImplementedError

    def openWindowInstance(
        self,
        path,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    ):
        # type: (...) -> PyObject
        raise NotImplementedError

    def swapTo(
        self,
        name,  # type: Union[str, unicode]
        params,  # type: Dict[Union[str, unicode], Any]
    ):
        # type: (...) -> PyObject
        raise NotImplementedError

    def swapWindow(self, *args):
        # type: (*Any) -> PyObject
        raise NotImplementedError


class ClientDatasetUtilities(Object):
    def __init__(self, app):
        # type: (FPMIApp) -> None
        super(ClientDatasetUtilities, self).__init__()
        print(app)


class ClientSystemUtilities(Object):
    def __init__(self):
        # type: () -> None
        super(ClientSystemUtilities, self).__init__()


class NavUtilities(INavUtilities):
    def centerWindow(self, arg):
        # type: (Union[str, unicode, FPMIWindow]) -> None
        pass

    def closeParentWindow(self, event):
        # type: (EventObject) -> None
        pass

    def closeWindow(self, arg):
        # type: (Union[str, unicode, FPMIWindow]) -> None
        pass

    def getCurrentWindow(self):
        # type: () -> Union[str, unicode]
        pass

    def goBack(self):
        # type: () -> PyObject
        pass

    def goForward(self):
        # type: () -> PyObject
        pass

    def goHome(self):
        # type: () -> PyObject
        pass

    def openWindow(
        self,
        path,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    ):
        # type: (...) -> PyObject
        pass

    def openWindowImpl(
        self,
        path,  # type: Union[str, unicode]
        params,  # type: Dict[Union[str, unicode], Any]
        openAdditional,  # type: bool
    ):
        # type: (...) -> PyObject
        pass

    def openWindowInstance(
        self,
        path,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    ):
        # type: (...) -> PyObject
        pass

    def swapTo(
        self,
        name,  # type: Union[str, unicode]
        params,  # type: Dict[Union[str, unicode], Any]
    ):
        # type: (...) -> PyObject
        pass

    def swapWindow(self, *args):
        # type: (*Any) -> PyObject
        pass


class ClientPrintUtilities(Object):

    class ComponentPrinter(Object):
        def __init__(self, c, fit, zoom):
            # type: (Component, bool, float) -> None
            super(ClientPrintUtilities.ComponentPrinter, self).__init__()
            print(c, fit, zoom)

        def print(self, g, pageFormat, pageIndex):
            # type: (Graphics, PageFormat, int) -> int
            pass

    class JythonPrintJob(Object):
        def __init__(self, c):
            # type: (Component) -> None
            super(ClientPrintUtilities.JythonPrintJob, self).__init__()
            print(c)

        def getBottomMargin(self):
            # type: () -> float
            pass

        def getLeftMargin(self):
            # type: () -> float
            pass

        def getOrientation(self):
            # type: () -> int
            pass

        def getPageHeight(self):
            # type: () -> float
            pass

        def getPageWidth(self):
            # type: () -> float
            pass

        def getPrinterName(self):
            # type: () -> Union[str, unicode]
            pass

        def getRightMargin(self):
            # type: () -> float
            pass

        def getTopMargin(self):
            # type: () -> float
            pass

        def getZoomFactor(self):
            # type: () -> float
            pass

        def isFitToPage(self):
            # type: () -> bool
            return True

        def isShowPrintDialog(self):
            # type: () -> bool
            return True

        def setBottomMargin(self, bottomMargin):
            # type: (float) -> None
            pass

        def setFitToPage(self, fitToPage):
            # type: (bool) -> None
            pass

        def setLeftMargin(self, leftMargin):
            # type: (float) -> None
            pass

        def setMargins(self, m):
            # type: (float) -> None
            pass

        def setOrientation(self, orientation):
            # type: (int) -> None
            pass

        def setPageHeight(self, pageHeight):
            # type: (float) -> None
            pass

        def setPageWidth(self, pageWidth):
            # type: (float) -> None
            pass

        def setPrinterName(self, printerName):
            # type: (Union[str, unicode]) -> None
            pass

        def setRightMargin(self, rightMargin):
            # type: (float) -> None
            pass

        def setShowPrintDialog(self, showPrintDialog):
            # type: (bool) -> None
            pass

        def setZoomFactor(self, zoomFactor):
            # type: (float) -> None
            pass

    def __init__(self, app):
        # type: (Any) -> None
        super(ClientPrintUtilities, self).__init__()
        print(self, app)

    def createImage(self, c):
        # type: (Component) -> BufferedImage
        print(self, c)
        width = height = imageType = 1
        return BufferedImage(width, height, imageType)

    def createPrintJob(self, c):
        # type: (Component) -> ClientPrintUtilities.JythonPrintJob
        pass

    def printToImage(self, c, fileName=None):
        # type: (Component, Optional[str]) -> None
        pass


class VisionUtilities(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(VisionUtilities, self).__init__()
        print(self, args)

    def beep(self):
        # type: () -> None
        pass

    def centerWindow(self, win):
        # type: (PyObject) -> None
        pass

    def close(self):
        # type: () -> None
        pass

    def closeDesktop(self, handle):
        # type: (Union[str, unicode]) -> None
        pass

    def closeParentWindow(self, event):
        # type: (EventObject) -> None
        pass

    def closeWindow(self, win):
        # type: (PyObject) -> None
        pass

    def color(self, *args, **kwargs):
        # type: (*Any, **Any) -> Color
        pass

    def createImage(self, c):
        # type: (Component) -> BufferedImage
        pass

    def createPopupMenu(self, keys, functions):
        # type: (PySequence, PySequence) -> JPopupMenu
        pass

    def createPrintJob(self, c):
        # type: (Component) -> ClientPrintUtilities.JythonPrintJob
        pass

    def desktop(self, arg=None):
        # type: (Union[int, str, unicode, None]) -> VisionUtilities
        pass

    def exit(self):
        # type: () -> None
        pass

    def exportCSV(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, unicode]
        pass

    def exportExcel(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, unicode]
        pass

    def exportHTML(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, unicode]
        pass

    def findWindow(self, path):
        # type: (Union[str, unicode]) -> List[PyComponentWrapper]
        pass

    def getAvailableLocales(self):
        # type: () -> List[Union[str, unicode]]
        pass

    def getAvailableTerms(self):
        # type: () -> List[Union[str, unicode]]
        pass

    def getClientId(self):
        # type: () -> Union[str, unicode]
        pass

    def getConnectionMode(self):
        # type: () -> int
        pass

    def getConnectTimeout(self):
        # type: () -> int
        pass

    def getCurrentDesktop(self):
        # type: () -> Union[str, unicode]
        pass

    def getCurrentWindow(self):
        # type: () -> Union[str, unicode]
        pass

    def getDesktopHandles(self):
        # type: () -> List[Any]
        pass

    def getEdition(self):
        # type: () -> Union[str, unicode]
        pass

    def getExternalIpAddress(self):
        # type: () -> Union[str, unicode]
        pass

    def getGatewayAddress(self):
        # type: () -> Union[str, unicode]
        pass

    def getHandle(self):
        # type: () -> Union[str, unicode]
        pass

    def getInactivitySeconds(self):
        # type: () -> int
        return 300

    def getKeyboardLayouts(self):
        # type: () -> List[KeyboardLayout]
        pass

    def getLocale(self):
        # type: () -> Union[str, unicode]
        pass

    def getOpenedWindowNames(self):
        # type: () -> PyTuple
        pass

    def getOpenedWindows(self):
        # type: () -> PyTuple
        pass

    def getParentWindow(self, event):
        # type: (EventObject) -> PyObject
        pass

    def getReadTimeout(self):
        # type: () -> int
        pass

    def getRoles(self):
        # type: () -> List[Union[str, unicode]]
        pass

    def getScreenIndex(self):
        # type: () -> int
        pass

    def getScreens(self):
        # type: () -> PySequence
        pass

    def getSibling(self, event, name):
        # type: (EventObject, Union[str, unicode]) -> PyObject
        pass

    def getSystemFlags(self):
        # type: () -> int
        pass

    def getUsername(self):
        # type: () -> Union[str, unicode]
        pass

    def getUserRoles(self, *args, **kwargs):
        # type: (*Any, **Any) -> List[Union[str, unicode]]
        pass

    def getWindow(self, name):
        # type: (Union[str, unicode]) -> PyObject
        pass

    def getWindowNames(self):
        # type: () -> PyTuple
        pass

    def goBack(self):
        # type: () -> PyObject
        pass

    def goForward(self):
        # type: () -> PyObject
        pass

    def goHome(self):
        # type: () -> PyObject
        pass

    def invokeLater(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        pass

    def isOverlaysEnabled(self):
        # type: () -> bool
        return True

    def isScreenLocked(self):
        # type: () -> bool
        return True

    def isTouchscreenMode(self):
        # type: () -> bool
        return True

    def lockScreen(self, obscure=False):
        # type: (bool) -> None
        pass

    def logout(self):
        # type: () -> None
        pass

    def openDesktop(self, *args, **kwargs):
        # type: (*PyObject, **Union[str, unicode]) -> JFrame
        pass

    def openFile(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, unicode]
        pass

    def openFiles(self, *args, **kwargs):
        # type: (*Any, **Any) -> List[Union[str, unicode]]
        pass

    def openURL(self, url):
        # type: (Union[str, unicode]) -> None
        pass

    def openWindow(
        self,
        path,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    ):
        # type: (...) -> PyObject
        pass

    def openWindowInstance(
        self,
        path,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    ):
        # type: (...) -> PyObject
        pass

    def playSoundClip(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        pass

    def printToImage(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        pass

    def refreshBinding(self, comp, propName):
        # type: (JComponent, Union[str, unicode]) -> bool
        return True

    def retarget(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        pass

    def saveFile(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, unicode]
        pass

    def setConnectionMode(self, mode):
        # type: (int) -> None
        pass

    def setConnectTimeout(self, timeout):
        # type: (int) -> None
        pass

    def setLocale(self, locale):
        # type: (Union[str, unicode, Locale]) -> None
        pass

    def setOverlaysEnabled(self, b):
        # type: (bool) -> None
        pass

    def setReadTimeout(self, timeout):
        # type: (int) -> None
        pass

    def setScreenIndex(self, index):
        # type: (int) -> None
        pass

    def setTouchscreenMode(self, b):
        # type: (bool) -> None
        pass

    def showColorInput(self, *args, **kwargs):
        # type: (*Any, **Any) -> Color
        pass

    def showConfirm(self, *args, **kwargs):
        # type: (*Any, **Any) -> bool
        print(args, kwargs)
        return True

    def showDiagnostics(self):
        # type: () -> None
        pass

    def showError(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        pass

    def showInput(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, unicode, None]
        pass

    def showMessage(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        pass

    def showNumericKeyPad(self, *args, **kwargs):
        # type: (*Any, **Any) -> Number
        pass

    def showPasswordInput(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, unicode, None]
        pass

    def showTouchscreenKeyboard(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, unicode]
        pass

    def showWarning(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        pass

    def swapTo(
        self,
        name,  # type: Union[str, unicode]
        params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    ):
        # type: (...) -> PyObject
        pass

    def swapWindow(self, *args):
        # type: (*Any) -> PyObject
        pass

    def switchUser(self, *args, **kwargs):
        # type: (*Any, **Any) -> bool
        print(args, kwargs)
        return True

    def transform(self, *args, **kwargs):
        # type: (*Any, **Union[str, unicode]) -> PyObject
        pass

    def unlockScreen(self):
        # type: () -> None
        pass

    def updateProject(self):
        # type: () -> None
        pass

    def validateUser(self, *args, **kwargs):
        # type: (*Any, **Any) -> bool
        print(args, kwargs)
        return True


class WindowUtilities(Object):
    """These are the scripting functions mounted at system.gui.*.

    Changes to this class must be made carefully, as some of the true
    implementations actually reside in the subclass,
    WindowUtilitiesForDesktop.
    """

    class JyPopupMenu(JPopupMenu):
        def actionPerformed(self, e):
            # type: (ActionEvent) -> None
            pass

        def addJyFunction(self, name, fun):
            # type: (Union[str, unicode], PyObject) -> None
            pass

        def show(self, me, *args):
            # type: (Union[ComponentEvent, MouseEvent], *int) -> None
            pass

    class PopupContext(Object):
        def endPopup(self):
            # type: () -> None
            pass

        def startPopup(self):
            # type: () -> None
            pass

    ACCL_NONE = 0
    ACCL_CONSTANT = 1
    ACCL_FAST_TO_SLOW = 2
    ACCL_SLOW_TO_FAST = 3
    ACCL_EASE = 4
    COORD_DESIGNER = 1
    COORD_SCREEN = 0

    def chooseColor(self, initialColor, dialogTitle="Choose Color"):
        # type: (Color, Union[str, unicode, None]) -> Color
        pass

    def closeDesktop(self, handle):
        # type: (Union[str, unicode]) -> None
        pass

    @staticmethod
    def color(*args):
        # type: (*Any) -> Color
        pass

    def confirm(
        self,
        message,  # type: Union[str, unicode]
        title="Confirm",  # type: Union[str, unicode]
        allowCancel=False,  # type: bool
    ):
        # type: (...) -> Optional[bool]
        pass

    @staticmethod
    def convertPointToScreen(x, y, event):
        # type: (int, int, EventObject) -> Tuple[int, int]
        pass

    @staticmethod
    def createPopupContext():
        # type: () -> WindowUtilities.PopupContext
        pass

    @staticmethod
    def createPopupMenu(key, functions):
        # type: (PySequence, PySequence) -> JPopupMenu
        pass

    def desktop(self, arg):
        # type: (Union[int, str, unicode]) -> WindowUtilities
        pass

    def errorBox(self, message, title="Error"):
        # type: (Union[str, unicode], Union[str, unicode, None]) -> None
        pass

    @staticmethod
    def find(component):
        # type: (JComponent) -> WindowUtilities
        pass

    def findWindow(self, path):
        # type: (Union[str, unicode]) -> List[PyComponentWrapper]
        pass

    def getCurrentDesktop(self):
        # type: () -> Union[str, unicode]
        pass

    def getDesktopHandles(self):
        # type: () -> PySequence
        pass

    def getOpenedWindowNames(self):
        # type: () -> PyTuple
        pass

    def getOpenedWindows(self):
        # type: () -> PyTuple
        pass

    @staticmethod
    def getParentWindow(event):
        # type: (EventObject) -> PyObject
        pass

    def getQuality(self, comp, propertyName):
        # type: (JComponent, Union[str, unicode]) -> QualityCode
        pass

    def getScreenIndex(self):
        # type: () -> int
        pass

    @staticmethod
    def getScreens():
        # type: () -> PySequence
        pass

    @staticmethod
    def getSibling(event, name):
        # type: (EventObject, Union[str, unicode]) -> PyObject
        pass

    def getWindow(self, name):
        # type: (Union[str, unicode]) -> PyObject
        pass

    def getWindowNames(self):
        # type: () -> PyTuple
        pass

    def inputBox(
        self,
        message,  # type: Union[str, unicode]
        defaultTxt="",  # type: Union[str, unicode]
    ):
        # type: (...) -> Union[str, unicode, None]
        pass

    def isTouchscreenModeEnabled(self):
        # type: () -> bool
        return True

    def messageBox(self, message, title="Information"):
        # type: (Union[str, unicode], Union[str, unicode]) -> None
        pass

    def openDesktop(self, *args, **kwargs):
        # type: (*PyObject, **Union[str, unicode]) -> JFrame
        pass

    def openDiagnostics(self):
        # type: () -> None
        pass

    def passwordBox(
        self,
        message,  # type:Union[str, unicode]
        title="Password",  # type: Union[str, unicode]
        echoChar="*",  # type: Union[str, unicode]
    ):
        # type: (...) -> Union[str, unicode, None]
        pass

    def setTouchScreenModeEnabled(self, b):
        # type: (bool) -> None
        pass

    def showNumericKeyPad(
        self,
        initialValue,  # type: Number
        fontSize=None,  # type: Optional[int]
        usePasswordMode=False,  # type: bool
    ):
        # type: (...) -> Number
        pass

    def showTouchscreenKeyboard(
        self,
        initialText,  # type: Union[str, unicode]
        fontSize=None,  # type: Optional[int]
        password=None,  # type: Optional[bool]
    ):
        # type: (...) -> Union[str, unicode]
        pass

    def transform(self, *args, **kwargs):
        # type: (*PyObject, **Union[str, unicode]) -> PyObject
        pass

    def warningBox(self, message, title="Warning"):
        # type: (Union[str, unicode], Union[str, unicode]) -> None
        pass
