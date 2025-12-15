"""Provides a set of "lightweight" (all-Java language) components that,
to the maximum degree possible, work the same on all platforms.
"""

from __future__ import print_function

__all__ = [
    "Icon",
    "JComponent",
    "JFrame",
    "JInternalFrame",
    "JLabel",
    "JOptionPane",
    "JPanel",
    "JPopupMenu",
    "JTextField",
]

from typing import Any, List, Optional

from java.awt import Container, Frame
from java.lang import String
from javax.swing.text import JTextComponent


class Icon(object):
    def getIconHeight(self):
        raise NotImplementedError

    def getIconWidth(self):
        raise NotImplementedError

    def paintIcon(self, c, g, x, y):
        raise NotImplementedError


class JComponent(Container):
    """The base class for all Swing components except top-level
    containers.
    """

    def __init__(self):
        # type: () -> None
        pass


class JFrame(Frame):
    """An extended version of java.awt.Frame that adds support for the
    JFC/Swing component architecture.
    """

    def __init__(self, *args):
        # type: (Any) -> None
        pass


class JInternalFrame(JComponent):
    """A lightweight object that provides many of the features of a
    native frame, including dragging, closing, becoming an icon,
    resizing, title display, and support for a menu bar.
    """

    def __init__(
        self,
        title=None,  # type: Optional[String]
        resizable=None,  # type: Optional[bool]
        closable=None,  # type: Optional[bool]
        maximizable=None,  # type: Optional[bool]
        iconifiable=None,  # type: Optional[bool]
    ):
        # type: (...) -> None
        super(JInternalFrame, self).__init__()
        print(title, resizable, closable, maximizable, iconifiable)


class JLabel(JComponent):
    """A display area for a short text string or an image, or both."""

    def __init__(self, *args):
        # type: (Any) -> None
        super(JLabel, self).__init__()
        print(args)


class JOptionPane(JComponent):
    """JOptionPane makes it easy to pop up a standard dialog box that
    prompts users for a value or informs them of something.

    For information about using JOptionPane, see How to Make Dialogs, a
    section in The Java Tutorial.
    """

    # messageType.
    PLAIN_MESSAGE = -1
    ERROR_MESSAGE = 0
    INFORMATION_MESSAGE = 1
    WARNING_MESSAGE = 2
    QUESTION_MESSAGE = 3

    # optionType.
    DEFAULT_OPTION = -1
    YES_NO_OPTION = 0
    YES_NO_CANCEL_OPTION = 1
    OK_CANCEL_OPTION = 2

    # When one of the showXxxDialog methods returns an integer, the
    # possible values are:
    CLOSED_OPTION = -1
    OK_OPTION = 0
    YES_OPTION = 0
    NO_OPTION = 1
    CANCEL_OPTION = 2

    @staticmethod
    def showConfirmDialog(
        parentComponent,
        message,
        title=None,
        optionType=None,
        messageType=None,
        icon=None,
    ):
        print(parentComponent, message, title, optionType, messageType, icon)
        return JOptionPane.YES_OPTION

    @staticmethod
    def showInputDialog(
        parentComponent,
        message,
        title=None,
        messageType=None,
        icon=None,
        selectionValues=None,
        initialSelectionValue=None,
    ):
        print(
            parentComponent,
            message,
            title,
            messageType,
            icon,
            selectionValues,
            initialSelectionValue,
        )
        return "Input"

    @staticmethod
    def showMessageDialog(
        parentComponent,  # type: Optional[Any]
        message,  # type: Any
        title=None,  # type: Optional[String]
        messageType=None,  # type: Optional[int]
        icon=None,  # type: Optional[Icon]
    ):
        # type: (...) -> None
        print(parentComponent, message, title, messageType, icon)

    @staticmethod
    def showOptionDialog(
        parentComponent,  # type: Optional[Any]
        message,  # type: Any
        title=None,  # type: Optional[String]
        optionType=None,  # type: Optional[int]
        messageType=None,  # type: Optional[int]
        icon=None,  # type: Optional[Icon]
        options=None,  # type: Optional[List[Any]]
        initialValue=None,  # type: Optional[Any]
    ):
        # type: (...) -> int
        print(
            parentComponent,
            message,
            title,
            optionType,
            messageType,
            icon,
            options,
            initialValue,
        )
        return JOptionPane.YES_OPTION


class JPanel(JComponent):
    """JPanel is a generic lightweight container."""

    def __init__(self, *args):
        # type: (Any) -> None
        super(JPanel, self).__init__()
        print(args)


class JPopupMenu(JComponent):
    def __init__(self, label=None):
        # type: (Optional[String]) -> None
        super(JPopupMenu, self).__init__()
        print(label)

    def addAncestorListener(self, listener):
        pass

    def addNotify(self):
        pass

    def createToolTip(self):
        print(self)
        return JToolTip()

    @staticmethod
    def getDefaultLocale():
        pass

    @staticmethod
    def isLightweightComponent(c):
        pass

    @staticmethod
    def setDefaultLocale(l):
        pass


class JTextField(JTextComponent):
    def __init__(self, *args):
        # type: (Any) -> None
        pass


class JToolTip(JComponent):
    def getAccessibleContext(self):
        pass

    def getComponent(self):
        print(self)
        return JComponent()

    def getTipText(self):
        pass
