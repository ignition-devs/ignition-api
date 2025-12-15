from __future__ import print_function

__all__ = ["FPMIWindow"]

from java.lang import String
from javax.swing import JInternalFrame


class FPMIWindow(JInternalFrame):
    CACHE_ALWAYS = 2
    CACHE_AUTO = 0
    CACHE_NEVER = 1
    DOCK_EAST = 2
    DOCK_FLOAT = 0
    DOCK_NORTH = 2
    DOCK_SOUTH = 4
    DOCK_WEST = 3
    PARENT_WINDOW_NAME = "_parent"
    SHOW_ALWAYS = 0
    SHOW_NEVER = 1
    SHOW_MAXIMIZED = 2

    _path = "Path/To/Window"

    def __init__(self, name):
        # type: (String) -> None
        super(FPMIWindow, self).__init__()
        self.name = name

    def getPath(self):
        return self._path

    def getRootContainer(self):
        pass
