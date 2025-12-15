"""Vision Functions.

The following function will allow you to update your Vision Client
project using scripting.
"""

from __future__ import print_function

__all__ = [
    "ACCL_CONSTANT",
    "ACCL_EASE",
    "ACCL_FAST_TO_SLOW",
    "ACCL_NONE",
    "ACCL_SLOW_TO_FAST",
    "CLIENT_FLAG",
    "CONNECTION_MODE_DISCONNECTED",
    "CONNECTION_MODE_READ_ONLY",
    "CONNECTION_MODE_READ_WRITE",
    "COORD_DESIGNER",
    "COORD_SCREEN",
    "DESIGNER_FLAG",
    "FULLSCREEN_FLAG",
    "LANDSCAPE",
    "PORTRAIT",
    "PREVIEW_FLAG",
    "SSL_FLAG",
    "beep",
    "centerWindow",
    "closeDesktop",
    "closeParentWindow",
    "closeWindow",
    "color",
    "createImage",
    "createPopupMenu",
    "createPrintJob",
    "desktop",
    "exit",
    "exportCSV",
    "exportExcel",
    "exportHTML",
    "findWindow",
    "getAvailableLocales",
    "getAvailableTerms",
    "getClientId",
    "getConnectTimeout",
    "getConnectionMode",
    "getCurrentDesktop",
    "getCurrentWindow",
    "getDesktopHandles",
    "getEdition",
    "getExternalIpAddress",
    "getGatewayAddress",
    "getInactivitySeconds",
    "getKeyboardLayouts",
    "getLocale",
    "getOpenedWindowNames",
    "getOpenedWindows",
    "getParentWindow",
    "getReadTimeout",
    "getRoles",
    "getScreenIndex",
    "getScreens",
    "getSibling",
    "getSystemFlags",
    "getUsername",
    "getWindow",
    "getWindowNames",
    "goBack",
    "goForward",
    "goHome",
    "invokeLater",
    "isOverlaysEnabled",
    "isScreenLocked",
    "isTouchscreenMode",
    "lockScreen",
    "logout",
    "openDesktop",
    "openFile",
    "openFiles",
    "openURL",
    "openWindow",
    "openWindowInstance",
    "playSoundClip",
    "printToImage",
    "refreshBinding",
    "retarget",
    "saveFile",
    "setConnectTimeout",
    "setConnectionMode",
    "setLocale",
    "setOverlaysEnabled",
    "setReadTimeout",
    "setScreenIndex",
    "setTouchscreenMode",
    "showColorInput",
    "showConfirm",
    "showDiagnostics",
    "showError",
    "showInput",
    "showMessage",
    "showNumericKeypad",
    "showPasswordInput",
    "showTouchscreenKeyboard",
    "showWarning",
    "swapTo",
    "swapWindow",
    "switchUser",
    "transform",
    "unlockScreen",
    "updateProject",
]

import getpass
import os
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from java.awt import Color, Component, Toolkit
from java.awt.image import BufferedImage
from java.lang import IllegalArgumentException
from java.org.jdesktop.core.animation.timing import Animator
from java.util import EventObject, Locale
from javax.swing import (
    JComponent,
    JFrame,
    JLabel,
    JOptionPane,
    JPanel,
    JPopupMenu,
    JTextField,
)

from com.inductiveautomation.factorypmi.application import FPMIWindow
from com.inductiveautomation.factorypmi.application.script.builtin import (
    ClientPrintUtilities,
    VisionUtilities,
)
from com.inductiveautomation.ignition.common import Dataset
from com.inductiveautomation.ignition.common.i18n.keyboard import KeyboardLayout

# GUI constants
ACCL_NONE = 0
ACCL_CONSTANT = 1
ACCL_FAST_TO_SLOW = 2
ACCL_SLOW_TO_FAST = 3
ACCL_EASE = 4
COORD_DESIGNER = 1
COORD_SCREEN = 0

# Print constants
LANDSCAPE = 0
PORTRAIT = 1

# Util constants
CLIENT_FLAG = 4
DESIGNER_FLAG = 1
FULLSCREEN_FLAG = 32
PREVIEW_FLAG = 2
SSL_FLAG = 64

# Vision constants
CONNECTION_MODE_DISCONNECTED = 1
CONNECTION_MODE_READ_ONLY = 2
CONNECTION_MODE_READ_WRITE = 3


def beep():
    # type: () -> None
    """Tells the computer to make a "beep" sound.

    The computer must have a way of producing sound.
    """
    Toolkit.getDefaultToolkit().beep()


def centerWindow(arg):
    # type: (Union[str, unicode, FPMIWindow]) -> None
    """Given a window path, or a reference to a window itself, it will
    center the window.

    The window should be floating and non-maximized. If the window can't
    be found, this function will do nothing.

    Args:
        arg: The path of the window or a reference to the window to
            center.
    """
    print(arg)


def closeDesktop(handle):
    # type: (Union[str, unicode]) -> None
    """Allows you to close any of the open desktops associated with the
    current client.

    Args:
        handle: The handle for the desktop to close. The screen index
            cast as a string may be used instead of the handle. If
            omitted, this will default to the Primary Desktop.
            Alternatively, the handle "primary" can be used to refer to
            the Primary Desktop.
    """
    print(handle)


def closeParentWindow(event):
    # type: (EventObject) -> None
    """Closes the parent window given a component event object.

    Args:
        event: A component event object. The enclosing window for the
            component will be closed.
    """
    print(event)


def closeWindow(arg):
    # type: (Union[str, unicode, FPMIWindow]) -> None
    """Given a window path, or a reference to a window itself, it will
    close the window.

    If the window can't be found, this function will do nothing.

    Args:
        arg: The path of the window or a reference to the window to
            center.
    """
    print(arg)


def color(*args):
    # type: (*Any) -> Color
    """Creates a new color object, either by parsing a string or by
    having the RGB[A] channels specified explicitly.

    Args:
        *args: Variable length argument list.

    Returns:
        The newly created color.
    """
    print(args)
    return Color(*args)


def createImage(component):
    # type: (Component) -> BufferedImage
    """Takes a snapshot of a component and creates a Java BufferedImage
    out of it.

    You can use javax.imageio. to turn this into bytes that can be saved
    to a file or a BLOB field in a database.

    Args:
        component: The component to render.

    Returns:
        A java.awt.image.BufferedImage representing the component.
    """
    return ClientPrintUtilities("app").createImage(component)


def createPopupMenu(
    itemNames,  # type: List[Union[str, unicode]]
    itemFunctions,  # type: List[Callable[..., Any]]
):
    # type: (...) -> JPopupMenu
    """Creates a new popup menu, which can then be shown over a
    component on a mouse event.

    Args:
        itemNames: A list of names to create popup menu items with.
        itemFunctions: A list of functions to match up with the names.

    Returns:
        The javax.swing.JPopupMenu that was created.
    """
    print(itemNames, itemFunctions)
    return JPopupMenu()


def createPrintJob(component):
    # type: (Component) -> ClientPrintUtilities.JythonPrintJob
    """Provides a general printing facility for printing the contents of
    a window or component to a printer.

    The general workflow for this function is that you create the print
    job, set the options you'd like on it, and then call print() on the
    job. For printing reports or tables, use those components' dedicated
    print() functions.

    Args:
        component: The component that you'd like to print.

    Returns:
        A print job that can then be customized and started. To start
        the print job, use .print().
    """
    return ClientPrintUtilities.JythonPrintJob(component)


def desktop(handle="primary"):
    # type: (Union[str, unicode, None]) -> VisionUtilities
    """Allows for invoking system.vision functions on a specific
    desktop.

    Args:
        handle: The handle for the desktop to use. The screen index cast
            as a string may be used instead of the handle. If omitted,
            this will default to the primary desktop. Alternatively, the
            handle "primary" can be used to refer to the primary
            desktop. Optional.

    Returns:
        A copy of system.vision that will alter the desktop named by the
        given handle.
    """
    print(handle)
    return VisionUtilities()


def exit(force=False):
    # type: (bool) -> None
    """Exits the running client, as long as the shutdown intercept
    script doesn't cancel the shutdown event.

    Set force to True to not give the shutdown intercept script a chance
    to cancel the exit. Note that this will quit the Client completely.
    You can use system.security.logout() to return to the login screen.

    Args:
        force: If True, the shutdown-intercept script will be
            skipped. Default is False. Optional.
    """
    print(force)


def exportCSV(filename, showHeaders, dataset):
    # type: (Union[str, unicode], bool, Dataset) -> Union[str, unicode]
    """Exports the contents of a dataset as a CSV file, prompting the
    user to save the file to disk.

    To write silently to a file, you cannot use the `dataset.export*`
    functions. Instead, use the `toCSV()` function.

    Args:
        filename: A suggested filename to save as.
        showHeaders: If True, the CSV file will include a header
            row.
        dataset: The dataset to export.

    Returns:
        The path to the saved file, or None if the action was canceled
        by the user.
    """
    print(filename, showHeaders, dataset)
    return os.path.expanduser("~")


def exportExcel(
    filename,  # type: Union[str, unicode]
    showHeaders,  # type: bool
    dataset,  # type: Union[Dataset, List[Dataset]]
    nullsEmpty=False,  # type: bool
):
    # type: (...) -> Union[str, unicode]
    """Exports the contents of a dataset as an Excel spreadsheet,
    prompting the user to save the file to disk.

    Uses the same format as the dataSetToExcel function.

    To write silently to a file, you cannot use the `dataset.export*`
    functions. Instead, use the `toExcel()` function.

    Args:
        filename: A suggested filename to save as.
        showHeaders: If True, the spreadsheet will include a header
            row.
        dataset: Either a single dataset, or a list of datasets. When
            passing a list, each element represents a single sheet in
            the resulting workbook.
        nullsEmpty: If True, the spreadsheet will leave cells with NULL
            values empty, instead of allowing Excel to provide a default
            value like 0. Defaults to False. Optional.

    Returns:
        The path to the saved file, or None if the action was canceled
        by the user.
    """
    print(filename, showHeaders, dataset, nullsEmpty)
    return os.path.expanduser("~")


def exportHTML(
    filename,  # type: Union[str, unicode]
    showHeaders,  # type: bool
    dataset,  # type: Dataset
    title,  # type: Union[str, unicode]
):
    # type: (...) -> Union[str, unicode]
    """Exports the contents of a dataset to an HTML page.

    Prompts the user to save the file to disk.

    Args:
        filename: A suggested filename to save as.
        showHeaders: If True, the HTML table will include a header
            row.
        dataset: The dataset to export.
        title: The title for the HTML page.

    Returns:
        The path to the saved file, or None if the action was canceled
        by the user.
    """
    print(filename, showHeaders, dataset, title)
    return os.path.expanduser("~")


def findWindow(path):
    # type: (Union[str, unicode]) -> List[FPMIWindow]
    """Finds and returns a list of windows with the given path.

    If the window is not open, an empty list will be returned. Useful
    for finding all instances of an open window that were opened with
    system.gui.openWindowInstance.

    Args:
        path: The path of the window to search for.

    Returns:
        A list of window objects. May be empty if window is not open, or
        have more than one entry if multiple windows are open.
    """
    print(path)
    return [FPMIWindow("Window")]


def getAvailableLocales():
    # type: () -> List[Union[str, unicode]]
    """Returns a collection of strings representing the Locales added to
    the Translation Manager, such as 'en' for English.

    Returns:
        A collection of strings representing the Locales added to the
        Translation Manager.
    """
    return ["en_US", "es_MX"]


def getAvailableTerms():
    # type: () -> List[Union[str, unicode]]
    """Returns a collection of available terms defined in the
    translation system.

    Returns:
         A collection of all of the terms available from the Translation
         Manager, as strings.
    """
    return ["term1", "term2"]


def getClientId():
    # type: () -> unicode
    """Returns a hex-string that represents a number unique to the
    running Client's Session.

    You are guaranteed that this number is unique between all running
    clients.

    Returns:
        A special code representing the Client's Session in a unique
        way.
    """
    return unicode("F6D410AC")


def getConnectTimeout():
    # type: () -> int
    """Returns the connect timeout in milliseconds for all Client-to-
    Gateway communication.

    This is the maximum amount of time that communication operations to
    the Gateway will be given to connect. The default is 10,000 ms (10
    seconds).

    Returns:
        The current connect timeout, in milliseconds. Default is 10,000
        (10 seconds).
    """
    return 10000


def getConnectionMode():
    # type: () -> int
    """Retrieves this client session's current connection mode.

    3 is read/write, 2 is read-only, and 1 is disconnected.

    Returns:
        The current connection mode for the client.
    """
    return 3


def getCurrentDesktop():
    # type: () -> Union[str, unicode]
    """Returns the handle of the desktop this function was called from.

    Commonly used with the system.gui.desktop and system.nav.desktop
    functions.

    Returns:
        The handle of the current desktop.
    """
    return "primary"


def getCurrentWindow():
    # type: () -> Union[str, unicode]
    """Returns the path of the current "main screen" window, which is
    defined as the maximized window.

    With the typical navigation, there is only ever one maximized window
    at a time.

    Returns:
        The path of the current "main screen" window - the maximized
        window.
    """
    return "Path/To/Maximized Window"


def getDesktopHandles():
    # type: () -> List[Union[str, unicode]]
    """Gets a list of all secondary handles of the open desktops
    associated with the current client.

    In this case, secondary means any desktop frame opened by the
    original client frame.

    Example:
        If the original client opened 2 new frames ('left client' and
        'right client'), then this function would return ['left client',
        'right client'].

    Returns:
        A list of window handles of all secondary Desktop frames.
    """
    return ["left client", "right client"]


def getEdition():
    # type: () -> Union[str, unicode]
    """Returns the "edition" of the Vision Client - "standard",
    "limited", or "panel".

    Returns:
        The edition of the Vision module that is running the Client.
    """
    return "standard"


def getExternalIpAddress():
    # type: () -> Union[str, unicode]
    """Returns the client's IP address, as it is detected by the
    Gateway.

    This means that this call will communicate with the Gateway, and the
    Gateway will tell the client what IP address its incoming traffic is
    coming from. If you have a client behind a Network Address
    Translation (NAT) router, then this address will be the Wide Area
    Network (WAN) address of the router instead of the Local Area
    Network (LAN) address of the client, which is what you'd get with
    system.net.getIpAddress.

    Returns:
        A text representation of the Client's IP address, as detected by
        the Gateway.
    """
    return "52.52.32.221"


def getGatewayAddress():
    # type: () -> unicode
    """Returns the address of the gateway that the client is currently
    communicating with.

    Returns:
        The address of the Gateway that the client is communicating
        with.
    """
    return unicode("http://localhost:8088/")


def getInactivitySeconds():
    # type: () -> long
    """Returns the number of seconds since any keyboard or mouse
    activity.

    Note:
        This function will always return zero in the Designer.

    Returns:
        The number of seconds the mouse and keyboard have been inactive
        for this client.
    """
    return long(0)


def getKeyboardLayouts():
    # type: () -> List[KeyboardLayout]
    """Returns the list of keyboard layouts available on this system.

    Returns:
        A list of KeyboardLayout objects.
    """
    return [
        KeyboardLayout(
            "eac73461-ce82-4583-952a-77c68ab20254", "en_us", "English", "EN", ["en"]
        ),
        KeyboardLayout(
            "ecb36fba-8037-494f-948b-ec5f9beeeb4a",
            "en_us_compat",
            "English (Compatibility)",
            "EN",
            ["en"],
        ),
    ]


def getLocale():
    # type: () -> Union[str, unicode]
    """Returns the current string representing the user's Locale, such
    as 'en' for English.

    Returns:
        String representing the user's Locale, such as 'en' for English.
    """
    return "es_MX"


def getOpenedWindowNames():
    # type: () -> Tuple[Union[str, unicode], ...]
    """Finds all of the currently open windows and returns a tuple of
    their paths.

    Returns:
        A tuple of strings, representing the path of each window that is
        open.
    """
    return "window_1", "window_2", "window_n"


def getOpenedWindows():
    # type: () -> Tuple[FPMIWindow, ...]
    """Finds all of the currently open windows, returning a tuple of
    references to them.

    Returns:
         A tuple of the opened windows. Not their names, but the actual
         window objects themselves.
    """
    return FPMIWindow("Main Window"), FPMIWindow("Other Window")


def getParentWindow(event):
    # type: (EventObject) -> FPMIWindow
    """Finds the parent (enclosing) window for the component that fired
    an event, returning a reference to it.

    Args:
        event: A component event object.

    Returns:
        The window that contains the component that fired the event.
    """
    print(event)
    return FPMIWindow("Parent Window")


def getReadTimeout():
    # type: () -> int
    """Returns the read timeout in milliseconds for all Client-to-
    Gateway communication.

    This is the maximum amount of time allowed for a communication
    operation to complete. The default is 60,000 ms (1 minute).

    Returns:
         The current read timeout, in milliseconds. Default is 60,000 ms
         (one minute).
    """
    return 60000


def getRoles():
    # type: () -> Tuple[Union[str, unicode], ...]
    """Finds the roles that the currently logged in user has, returns
    them as a Python tuple of strings.

    Returns:
        A list of the roles (strings) that are assigned to the current
        user.
    """
    return "Administrator", "Developer"


def getScreenIndex():
    # type: () -> int
    """Returns the returns an integer value representing the current
    screen index based on the screen from which this function was
    called.

    Returns:
        The screen from which the function was called.
    """
    return 0


def getScreens():
    # type: () -> List[Tuple[Union[str, unicode], int, int]]
    """Get a list of all the monitors on the computer this client is
    open on.

    Use with system.gui.setScreenIndex() to move the client.

    Returns:
        A sequence of tuples of the form (index, width, height) for each
        screen device (monitor) available.
    """
    return [("primary", 1440, 900), ("secondary", 1920, 1080)]


def getSibling(event, name):
    # type: (EventObject, Union[str, unicode]) -> FPMIWindow
    """Given a component event object, looks up a sibling component.

    Shortcut for event.source.parent.getComponent("siblingName"). If no
    such sibling is found, the special value None is returned.

    Args:
        event: A component event object.
        name: The name of the sibling component.

    Returns:
        The sibling component itself.
    """
    print(event, name)
    return FPMIWindow("Sibling")


def getSystemFlags():
    # type: () -> int
    """Returns an integer that represents a bit field containing
    information about the currently running system.

    Each bit corresponds to a specific flag as defined in the bitmask
    below.

    The integer return will be a total of all of the bits that are
    currently active.

    Examples:
        A full-screen client launched from the gateway webpage with no
        SSL will have a value of 44 (Fullscreen flag + Webstart Flag +
        Client Flag).

    Returns:
        A total of all the bits that are currently active.
    """
    return 1


def getUsername():
    # type: () -> Union[str, unicode]
    """Returns the currently logged-in username.

    Returns:
        The current username.
    """
    return getpass.getuser()


def getWindow(name):
    # type: (Union[str, unicode]) -> FPMIWindow
    """Finds a reference to an open window with the given name.

    Throws a ValueError if the named window is not open or not found.

    Args:
        name: The path to the window to field.

    Returns:
        A reference to the window, if it was open.
    """
    print(name)
    return FPMIWindow("Main Window")


def getWindowNames():
    # type: () -> Tuple[Union[str, unicode], ...]
    """Returns a list of the paths of all windows in the current
    project, sorted alphabetically.

    Returns:
        A tuple of strings, representing the path of each window defined
        in the current project.
    """
    return "Main Window", "Main Window 1", "Main Window 2"


def goBack():
    # type: () -> FPMIWindow
    """When using the typical navigation strategy, this function will
    navigate back to the previous main screen window.

    Returns:
        A reference to window that was navigated to.
    """
    return FPMIWindow("Back")


def goForward():
    # type: () -> FPMIWindow
    """When using the typical navigation strategy, this function will
    navigate "forward" to the last main screen window the user was on
    when they executed a system.nav.goBack().

    Returns:
        A reference to window that was navigated to.
    """
    return FPMIWindow("Forward")


def goHome():
    # type: () -> FPMIWindow
    """When using the typical navigation strategy, this function will
    navigate to the "home" window.

    This is automatically detected as the first main-screen window shown
    in a project.

    Returns:
        A reference to window that was navigated to.
    """
    return FPMIWindow("Home")


def invokeLater(function, delay=0):
    # type: (Callable[..., Any], int) -> None
    """Invokes (calls) the given Python function object after all of the
    currently processing and pending events are done being processed, or
    after a specified delay.

    The function will be executed on the GUI, or event dispatch, thread.
    This is useful for events like propertyChange events, where the
    script is called before any bindings are evaluated.

    If you specify an optional time argument (number of milliseconds),
    the function will be invoked after all currently processing and
    pending events are processed plus the duration of that time.

    Args:
        function: A Python function object that will be invoked later,
            on the GUI, or event-dispatch, thread with no arguments.
        delay: A delay, in milliseconds, to wait before the function is
            invoked. The default is 0, which means it will be invoked
            after all currently pending events are processed. Optional.
    """
    print(function, delay)


def isOverlaysEnabled():
    # type: () -> bool
    """Returns whether or not the current client's quality overlay
    system is currently enabled.

    Returns:
         True if overlays are currently enabled.
    """
    return False


def isScreenLocked():
    # type: () -> bool
    """Returns whether or not the screen is currently locked.

    Returns:
        A flag indication whether or not the screen is currently locked.
    """
    return False


def isTouchscreenMode():
    # type: () -> bool
    """Checks whether or not the running client's touchscreen mode is
    currently enabled.

    Returns:
         True if the Client currently has Touch Screen mode activated.
    """
    return False


def lockScreen(obscure=False):
    # type: (bool) -> None
    """Used to put a running Client in lock-screen mode.

    The screen can be unlocked by the user with the proper credentials,
    or by scripting via the system.security.unlockScreen() function.

    Args:
        obscure: If True, the locked screen will be opaque, otherwise
            it will be partially visible. Optional.
    """
    print(obscure)


def logout():
    # type: () -> None
    """Logs out of the Client for the current user and brings the Client
    to the login screen.
    """
    pass


def openDesktop(
    screen=0,  # type: int
    handle=None,  # type: Union[str, unicode, None]
    title=None,  # type: Union[str, unicode, None]
    width=None,  # type: Optional[int]
    height=None,  # type: Optional[int]
    x=0,  # type: int
    y=0,  # type: int
    windows=None,  # type: Optional[List[Union[str, unicode]]]
):
    # type: (...) -> JFrame
    """Creates an additional Desktop in a new frame.

    Args:
        screen: The screen index of which screen to place the new frame
            on. If omitted, screen 0 will be used. Optional.
        handle: A name for the desktop. If omitted, the screen index
            will be used. Optional.
        title: The title for the new frame. If omitted, the index handle
            will be used. If the handle and title are omitted, the
            screen index will be used. Optional.
        width: The width for the new Desktop's frame. If omitted, frame
            will become maximized on the specified monitor. Optional.
        height: The width for the new desktop's frame. If omitted, frame
            will become maximized on the specified monitor. Optional.
        x: The X coordinate for the new desktop's frame. Only used if
            both width and height are specified. If omitted, defaults to
            0. Optional.
        y: The Y coordinate for the new desktop's frame. Only used if
            both width and height are specified. If omitted, defaults to
            0. Optional.
        windows: A list of window paths to open in the new Desktop
            frame. If omitted, the desktop will open without any opened
            windows. Optional.

    Returns:
        A reference to the new Desktop frame object.
    """
    print(screen, handle, title, width, height, x, y, windows)
    return JFrame()


def openFile(
    extension=None,  # type: Union[str, unicode, None]
    defaultLocation=None,  # type: Union[str, unicode, None]
):
    # type: (...) -> Union[str, unicode, None]
    r"""Shows an "Open File" dialog box, prompting the user to choose a
    file to open.

    Returns the path to the file that the user chose, or None if the
    user canceled the dialog box. An extension can optionally be passed
    in that sets the filetype filter to that extension.

    Args:
        extension: A file extension, like "pdf", to try to open.
            Optional.
        defaultLocation: A folder location, like "C:\\MyFiles", to use
            as the starting location for the file chooser. Optional.

    Returns:
        The path to the selected file, or None if canceled.
    """
    print(extension, defaultLocation)
    return ""


def openFiles(
    extension=None,  # type: Union[str, unicode, None]
    defaultLocation=None,  # type: Union[str, unicode, None]
):
    # type: (...) -> Optional[List[Union[str, unicode]]]
    r"""Shows an "Open File" dialog box, prompting the user to choose a
    file or files to open.

    Returns the paths to the files that the user chooses, or None if the
    user canceled the dialog box. An extension can optionally be passed
    in that sets the filetype filter to that extension.

    Args:
        extension: A file extension, like "pdf", to try to open.
            Optional.
        defaultLocation: A folder location, like "C:\\MyFiles", to use
            as the starting location for the file chooser. Optional.

    Returns:
        The paths to the selected files, or None if canceled.
    """
    print(extension, defaultLocation)
    return ["path/to/file"]


def openURL(url, useApplet=False):
    # type: (Union[str, unicode], Optional[bool]) -> None
    """Opens the given URL or URI scheme outside of the currently
    running Client in whatever application the host operating system
    deems appropriate.

    Args:
        url: The URL to open in a web browser.
        useApplet: If set to True, and the client is running as an
            Applet, then the browser instance that launched the applet
            will be used to open the URL. Optional.
    """
    print(url, useApplet)


def openWindow(
    path,  # type: Union[str, unicode]
    params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
):
    # type: (...) -> FPMIWindow
    """Opens the window with the given path.

    If the window is already open, brings it to the front. The optional
    params dictionary contains key:value pairs which will be used to set
    the target window's root container's dynamic variables.

    Args:
        path: The path to the window to open.
        params: A dictionary of parameters to pass into the window. The
            keys in the dictionary must match dynamic property names on
            the target window's root container. The values for each key
            will be used to set those properties. Optional.

    Returns:
        A reference to the opened window.
    """
    print(path, params)
    return FPMIWindow("Opened Window")


def openWindowInstance(
    path,  # type: Union[str, unicode]
    params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
):
    # type: (...) -> FPMIWindow
    """Operates exactly like system.nav.openWindow, except that if the
    named window is already open, then an additional instance of the
    window will be opened.

    There is no limit to the number of additional instances of a window
    that you can open.

    Args:
        path: The path to the window to open.
        params: A dictionary of parameters to pass into the window. The
            keys in the dictionary must match dynamic property names on
            the target window's root container. The values for each key
            will be used to set those properties. Optional.

    Returns:
        A reference to the opened window.
    """
    print(path, params)
    return FPMIWindow("Window Instance")


def playSoundClip(wav, volume=1.0, wait=False):
    # type: (Any, float, bool) -> None
    """Plays a sound clip from a wav file to the system's default audio
    device.

    The wav file can be specified as a filepath, a URL, or directly as a
    raw byte array.

    Args:
        wav: A byte list of a wav file or filepath or URL that
            represents a wav file.
        volume: The clip's volume, represented as a floating point
            number between 0.0 and 1.0. Optional.
        wait: A boolean flag indicating whether or not the call to
            playSoundClip should block further script execution within
            the triggering event until the clip finishes. Useful in
            cases where code on lines after the playSoundClip call
            should wait until the sound clip finishes playing. Optional.
    """
    print(wav, volume, wait)


def printToImage(component, filename=None):
    # type: (Component, Union[str, unicode, None]) -> None
    """This function prints the given component (such as a graph,
    container, entire window, etc.) to an image file, and saves the file
    where ever the operating system deems appropriate.

    A filename and path may be provided to determine the name and
    location of the saved file.

    While not required, it is highly recommended to pass in a filename
    and path. The script may fail if the function attempts to save to a
    directory that the client does not have access rights to.

    Args:
        component: The component to render.
        filename: A filename to save the image as. Optional.
    """
    print(component, filename)


def refreshBinding(component, propertyName):
    # type: (JComponent, Union[str, unicode]) -> bool
    """This function will cause a Vision component binding to execute
    immediately.

    This is most often used for bindings that are set to Polling - Off.
    In this way, you cause a binding to execute on demand, when you know
    that the results of its query will return a new result. To use it,
    you simply specify the component and name of the property on whose
    binding you'd like to refresh.

    Even though the function includes "db" in the name, the function can
    update all types of Vision component bindings, including Property
    and Expression bindings.

    Note:
        This function will only work within the Vision module. To
        manually execute bindings in Perspective, use the refreshBinding
        component method.

    Args:
        component: The component whose property you want to refresh.
        propertyName: The name of the property that has a binding that
            needs to be refreshed.

    Returns:
        True if the property was found and refreshed successfully.
    """
    print(component, propertyName)
    return True


def retarget(
    project,  # type: Union[str, unicode]
    addresses=None,  # type: Optional[Union[str, unicode, List[Union[str, unicode]]]]
    params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    windows=None,  # type: Optional[List[Union[str, unicode]]]
):
    # type: (...) -> None
    """This function allows you to programmatically 'retarget' the
    Client to a different project and/or different Gateway.

    You can have it switch to another project on the same Gateway, or
    another gateway entirely, even across a WAN. This feature makes the
    vision of a seamless, enterprise-wide SCADA application a reality.

    The retarget feature will attempt to transfer the current user
    credentials over to the new project / Gateway. If the credentials
    fail on that project, the user will be prompted for a valid username
    and password. Once valid authentication has been achieved, the
    currently running project is shut down, and the new project is
    loaded.

    You can pass any information to the other project through the
    parameters dictionary. All entries in this dictionary will be set in
    the global scripting namespace in the other project. Even if you
    don't specify any parameters, the system will set the variable
    _RETARGET_FROM_PROJECT to the name of the current project and
    _RETARGET_FROM_GATEWAY to the address of the current Gateway.

    Args:
        project: The name of the project to retarget to.
        addresses: The address of the Gateway that the project resides
            on. Format is host:port when not using SSL/TLS, or
            https://host:port when SSL/TLS is enabled on the target
            gateway. This can be a list of strings. When using a list,
            the function will try each address in order, waiting for the
            timeout period between each address attempt. Optional.
        params: A dictionary of parameters that will be passed to the
            new project. They will be set as global variables in the new
            project's Python scripting environment. Optional.
        windows: A list of window paths to use as the startup windows.
            If omitted, the project's normal startup windows will be
            opened. If specified, the project's normal startup windows
            will be ignored, and this list will be used instead.
            Optional.
    """
    print(project, addresses, params, windows)


def saveFile(
    filename,  # type: Union[str, unicode]
    extension=None,  # type: Union[str, unicode, None]
    typeDesc=None,  # type: Union[str, unicode, None]
):
    # type: (...) -> Union[str, unicode, None]
    """Prompts the user to save a new file named filename.

    The optional extension and typeDesc arguments can be added to be
    used as a type filter. If the user accepts the save, the path to
    that file will be returned. If the user cancels the save, None will
    be returned.

    Args:
        filename: A file name to suggest to the user.
        extension: The appropriate file extension, like "jpeg", for the
            file. Optional.
        typeDesc: A description of the extension, like "JPEG Image".
            Optional.

    Returns:
        The path to the file that the user decided to save to, or None
        if they canceled.
    """
    print(filename, extension, typeDesc)
    return ""


def setConnectTimeout(connectTimeout):
    # type: (int) -> None
    """Sets the connect timeout for Client-to-Gateway communication.

    Specified in milliseconds.

    Args:
        connectTimeout: The new connect timeout, specified in
            milliseconds.
    """
    print(connectTimeout)


def setConnectionMode(mode):
    # type: (int) -> None
    """Sets the connection mode for the client session.

    Normally a client runs in mode 3, which is read-write. You may wish
    to change this to mode 2, which is read-only, which will only allow
    reading and subscribing to tags, and running SELECT queries. Tag
    writes and INSERT / UPDATE / DELETE queries will not function. You
    can also set the connection mode to mode 1, which is disconnected,
    all tag and query features will not work.

    Args:
        mode: The new connection mode. 1 = Disconnected, 2 = Read-only,
            3 = Read/Write.
    """
    print(mode)


def setLocale(locale):
    # type: (Union[str, unicode, Locale]) -> None
    """Sets the user's current Locale.

    Any valid Java locale code (case-insensitive) can be used as a
    parameter, including ones that have not yet been added to the
    Translation Manager.

    Args:
        locale: A locale code, such as 'en_US' for US English, or a
            java.util.Locale object.

    Raises:
        IllegalArgumentException: If passed an invalid local code.
    """
    if not locale:
        raise IllegalArgumentException("Invalid locale code")
    print(locale)


def setOverlaysEnabled(enabled):
    # type: (bool) -> None
    """Enables or disables the component quality overlay system.

    Args:
        enabled: True to turn on Tag overlays, False to turn
            them off.
    """
    print(enabled)


def setReadTimeout(readTimeout):
    # type: (int) -> None
    """Sets the read timeout for Client-to-Gateway communication.

    Specified in milliseconds.

    Args:
        readTimeout: The new read timeout, specified in
            milliseconds.
    """
    print(readTimeout)


def setTouchscreenMode(enabled):
    # type: (bool) -> None
    """Alters a running Client's Touch Screen mode on the fly.

    Args:
        enabled: The new value for Touch Screen mode being enabled.
    """
    print(enabled)


def setScreenIndex(index):
    # type: (int) -> None
    """Moves an open client to a specific monitor.

    Use with system.gui.getScreens() to identify monitors before moving.

    Args:
        index: The new monitor index for this client to move to. 0
            based.
    """
    print(index)


def showColorInput(initialColor, dialogTitle="Choose Color"):
    # type: (Color, Union[str, unicode]) -> Color
    """Prompts the user to pick a color using the default color-chooser
    dialog box.

    Args:
        initialColor: A color to use as a starting point in the color
            choosing popup.
        dialogTitle: The title for the color choosing popup. Defaults to
            "Choose Color". Optional.

    Returns:
        The new color chosen by the user.
    """
    print(initialColor, dialogTitle)
    return Color()


def showConfirm(
    message,  # type: Union[str, unicode]
    title="Confirm",  # type: Union[str, unicode]
    allowCancel=False,  # type: bool
):
    # type: (...) -> Optional[bool]
    """Displays a confirmation dialog box to the user with "Yes", "No"
    options, and a custom message.

    Args:
        message: The message to show in the confirmation dialog.
        title: The title for the confirmation dialog. Optional.
        allowCancel: Show a cancel button in the dialog. Optional.

    Returns:
        True if the user selected "Yes", False if the user
        selected "No", None if the user selected "Cancel".
    """
    options = ["Yes", "No"]

    if allowCancel:
        options.append("Cancel")

    choice = JOptionPane.showOptionDialog(
        None,
        message,
        title,
        JOptionPane.YES_NO_CANCEL_OPTION,
        JOptionPane.QUESTION_MESSAGE,
        None,
        options,
        options[0],
    )

    return (
        not bool(choice)
        if choice in [JOptionPane.YES_OPTION, JOptionPane.NO_OPTION]
        else None
    )


def showDiagnostics():
    # type: () -> None
    """Opens the client runtime diagnostics window, which provides
    information regarding performance, logging, active threads,
    connection status, and the console.

    This provides an opportunity to open the diagnostics window in
    situations where the menu bar in the client is hidden, and the
    keyboard shortcut can not be used.
    """
    pass


def showError(message, title="Error"):
    # type: (Union[str, unicode], Union[str, unicode]) -> None
    """Displays an error-style message box to the user.

    Args:
        message: The message to display in an error box.
        title: The title for the error box. Optional.
    """
    JOptionPane.showMessageDialog(None, message, title, JOptionPane.ERROR_MESSAGE)


def showInput(
    message,  # type: Union[str, unicode]
    defaultText="",  # type: Union[str, unicode]
):
    # type: (...) -> Union[str, unicode, None]
    """Opens up a popup input dialog box.

    This dialog box will show a prompt message, and allow the user to
    type in a string. When the user is done, they can press "OK" or
    "Cancel". If OK is pressed, this function will return with the value
    that they typed in. If Cancel is pressed, this function will return
    the value None.

    Args:
        message: The message to display for the input box. Will accept
            HTML formatting.
        defaultText: The default text to initialize the input box with.
            Optional.

    Returns:
        The string value that was entered in the input box.
    """
    options = ["OK", "Cancel"]

    panel = JPanel()
    label = JLabel("{}: ".format(message))
    panel.add(label)
    text_field = JTextField(25)
    text_field.setText(defaultText)
    panel.add(text_field)

    choice = JOptionPane.showOptionDialog(
        None,
        panel,
        "Input",
        JOptionPane.OK_CANCEL_OPTION,
        JOptionPane.QUESTION_MESSAGE,
        None,
        options,
        options[0],
    )

    return text_field.getText() if choice == JOptionPane.OK_OPTION else None


def showMessage(message, title="Information"):
    # type: (Union[str, unicode], Union[str, unicode]) -> None
    """Displays an informational-style message popup box to the user.

    Args:
        message: The message to display. Will accept HTML formatting.
        title: The title for the message box. Optional.
    """
    JOptionPane.showMessageDialog(None, message, title, JOptionPane.INFORMATION_MESSAGE)


def showNumericKeypad(
    initialValue,  # type: Union[float, int, long]
    fontSize=None,  # type: Optional[int]
    usePasswordMode=False,  # type: bool
):
    # type: (...) -> Union[float, int, long]
    """Displays a modal on-screen numeric keypad, allowing for arbitrary
    numeric entry using the mouse, or a finger on a touchscreen monitor.

    Returns the number that the user entered.

    Args:
        initialValue: The value to start the on-screen keypad with.
        fontSize: The font size to display in the keypad. Optional.
        usePasswordMode: If True, display a * for each digit. Optional.

    Returns:
        The value that was entered in the keypad.
    """
    print(initialValue, fontSize, usePasswordMode)
    return 43


def showPasswordInput(
    message,  # type:Union[str, unicode]
    title="Password",  # type: Union[str, unicode]
    echoChar="*",  # type: Union[str, unicode]
):
    # type: (...) -> Union[str, unicode, None]
    """Pops up a special input box that uses a password field, so the
    text isn't echoed back in clear-text to the user.

    Returns the text they entered, or None if they canceled the dialog
    box.

    Args:
        message: The message for the password prompt. Will accept HTML
            formatting.
        title: A title for the password prompt. Optional.
        echoChar: A custom echo character. Defaults to: *. Optional.

    Returns:
        The password that was entered, or None if the prompt was
        canceled.
    """
    print(message, title, echoChar)
    return "password"


def showTouchscreenKeyboard(
    initialText,  # type: Union[str, unicode]
    fontSize=None,  # type: Optional[int]
    passwordMode=False,  # type: bool
):
    # type: (...) -> Union[str, unicode]
    """Displays a modal on-screen keyboard, allowing for arbitrary text
    entry using the mouse, or a finger on a touchscreen monitor.

    Returns the text that the user entered.

    Args:
        initialText: The text to start the on-screen keyboard with.
        fontSize: The font size to display in the keypad. Optional.
        passwordMode: True to activate password mode, where the text
            entered isn't echoed back clear-text. Optional.

    Returns:
        The text that was entered in the on-screen keyboard.
    """
    print(initialText, fontSize, passwordMode)
    return ""


def showWarning(message, title="Warning"):
    # type: (Union[str, unicode], Union[str, unicode]) -> None
    """Displays a message to the user in a warning style popup dialog.

    Args:
        message: The message to display in the warning box. Will accept
            HTML formatting.
        title: The title for the warning box. Optional.
    """
    JOptionPane.showMessageDialog(None, message, title, JOptionPane.WARNING_MESSAGE)


def swapTo(
    path,  # type: Union[str, unicode]
    params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
):
    # type: (...) -> FPMIWindow
    """Performs a window swap from the current main screen window to the
    window specified.

    Swapping means that the opened window will take the place of the
    closing window - in this case it will be maximized.

    This function works like system.nav.swapWindow except that you
    cannot specify the source for the swap.

    Args:
        path: The path to the window to open.
        params: A dictionary of parameters to pass into the window. The
            keys in the dictionary must match dynamic property names on
            the target window's root container. The values for each key
            will be used to set those properties. Optional.

    Returns:
        A reference to the swapped-to window.
    """
    print(path, params)
    return FPMIWindow("Swapped To")


def swapWindow(
    arg,  # type: Union[str, unicode, EventObject]
    swapToPath,  # type: Union[str, unicode]
    params=None,  # type: Optional[Dict[Union[str, unicode], Any]]
):
    # type: (...) -> FPMIWindow
    """Performs a window swap.

    This means that one window is closed, and another is opened and
    takes its place - assuming its size, floating state, and
    maximization state. This gives a seamless transition; one window
    seems to simply turn into another.

    This function works like system.nav.swapTo except that you can
    specify the source and destination for the swap.

    Args:
        arg: The path of the window to swap from. Must be a currently
            open window, otherwise this will act like an openWindow, or
            a component event (EventObject) whose enclosing window will
            be used as the "swap-from" window.
        swapToPath: The name of the window to swap to.
        params: A dictionary of parameters to pass into the window. The
            keys in the dictionary must match dynamic property names on
            the target window's root container. The values for each key
            will be used to set those properties. Optional.

    Returns:
        A reference to the swapped-to window.
    """
    print(arg, swapToPath, params)
    return FPMIWindow("Swapped To")


def switchUser(
    username,  # type: Union[str, unicode]
    password,  # type: Union[str, unicode]
    event,  # type: EventObject
    hideError=False,  # type: bool
):
    # type: (...) -> bool
    """Attempts to switch the current user on the fly.

    If the given username and password fail, this function will return
    False. If it succeeds, then all currently opened windows are closed,
    the user is switched, and windows are then re-opened in the states
    that they were in.

    If an event object is passed to this function, the parent window of
    the event object will not be re-opened after a successful user
    switch. This is to support the common case of having a switch-user
    screen that you want to disappear after the switch takes place.

    Args:
        username: The username to try and switch to.
        password: The password to authenticate with.
        event: If specified, the enclosing window for this event's
            component will be closed in the switch user process.
        hideError: If True, no error will be shown if the switch
            user function fails. Default is False. Optional.

    Returns:
        False if the switch user operation failed, True
        otherwise.
    """
    print(username, password, event, hideError)
    return True


def transform(
    component,  # type: JComponent
    newX=None,  # type: Optional[int]
    newY=None,  # type: Optional[int]
    newWidth=None,  # type: Optional[int]
    newHeight=None,  # type: Optional[int]
    duration=0,  # type: int
    callback=None,  # type: Optional[Callable[..., Any]]
    framesPerSecond=60,  # type: int
    acceleration=None,  # type: Optional[int]
    coordSpace=None,  # type: Optional[int]
):
    # type: (...) -> Animator
    """Sets a component's position and size at runtime.

    Additional arguments for the duration, framesPerSecond, and
    acceleration of the operation exist for animation. An optional
    callback argument will be executed when the transformation is
    complete.

    Note:
        The transformation is performed in Designer coordinate space on
        components which are centered or have more than two anchors.

    Args:
        component: The component to move or resize.
        newX: An optional x-coordinate to move to, relative to the
            upper-left corner of the component's parent container.
        newY: An optional y-coordinate to move to, relative to the
            upper-left corner of the component's parent container.
        newWidth: An optional width for the component.
        newHeight: An optional height for the component.
        duration: An optional duration over which the transformation
            will take place. If omitted or 0, the transform will take
            place immediately.
        callback: An optional function to be called when the
            transformation is complete.
        framesPerSecond: An optional frame rate argument which dictates
            how often the transformation updates over the given
            duration. The default is 60 frames per second.
        acceleration: An optional modifier to the acceleration of the
            transformation over the given duration. See system.gui
            constants for valid arguments.
        coordSpace: The coordinate space to use. When the default Screen
            Coordinates are used, the given size and position are
            absolute, as they appear in the client at runtime. When
            Designer Coordinates are used, the given size and position
            are pre-runtime adjusted values, as they would appear in the
            Designer. See system.gui constants for valid arguments.

    Returns:
        An object that contains pause(), resume(), and cancel() methods,
        allowing for a script to interrupt the animation.
    """
    print(
        component,
        newX,
        newY,
        newWidth,
        newHeight,
        duration,
        callback,
        framesPerSecond,
        acceleration,
        coordSpace,
    )
    return Animator()


def unlockScreen():
    # type: () -> None
    """Unlocks the Client, if it is currently in lock-screen mode."""
    pass


def updateProject():
    # type: () -> None
    """Updates the Vision Client project with saved changes.

    This function is intended to be used in conjunction with the "None"
    option of Vision Project update modes in the Project Properties, and
    the Vision Client System Tag ProjectUpdateAvailable.
    """
    pass
