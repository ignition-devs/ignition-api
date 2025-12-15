"""Print Functions.

The following functions allow you to send to a printer.
"""

from __future__ import print_function

__all__ = [
    "LANDSCAPE",
    "PORTRAIT",
    "getDefaultPrinterName",
    "getPrinterNames",
]

from typing import List, Optional

LANDSCAPE = 0
PORTRAIT = 1


def getDefaultPrinterName():
    # type: () -> Optional[unicode]
    """Obtains the local default printer.

    Returns:
        A string that represents the default printer. Returns null if
        there is no default printer.
    """
    return unicode("Default Printer")


def getPrinterNames():
    # type: () -> List[unicode]
    """Lists the available local printers.

    Returns:
        A list of strings that contain the names of local printers.
        Returns an empty list if there are no available local printers.
    """
    printer = getDefaultPrinterName()
    return [] if printer is None else [printer]
