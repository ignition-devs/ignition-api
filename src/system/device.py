"""Device Functions.

The following functions give you access to view and edit device
connections in the Gateway.
"""

from __future__ import print_function

__all__ = [
    "addDevice",
    "getDeviceHostname",
    "listDevices",
    "refreshBrowse",
    "removeDevice",
    "setDeviceEnabled",
    "setDeviceHostname",
]

from typing import Any, Dict

from com.inductiveautomation.ignition.common import BasicDataset
from java.lang import String


def addDevice(
    deviceType,  # type: String
    deviceName,  # type: String
    deviceProps,  # type: Dict[String, Any]
):
    # type: (...) -> None
    """Adds a new device connection in Ignition.

    Accepts a dictionary of parameters to configure the connection.
    Acceptable parameters differ by device type: i.e., a Modbus/TCP
    connection requires a hostname and port, but a simulator doesn't
    require any parameters.

    Args:
        deviceType: The device driver type. Possible values are listed
            in the Device Types table below.
        deviceName: The name that will be given to the new device
            connection.
        deviceProps: A dictionary of device connection properties and
            values. Each deviceType has different properties, but most
            require at least a hostname. Keys in the dictionary are
            case-insensitive, spaces are omitted, and the names of the
            properties that appear when manually creating a device
            connection.
    """
    print(deviceType, deviceName, deviceProps)


def getDeviceHostname(deviceName):
    # type: (String) -> String
    """Gets the hostname of a device.

    Args:
        deviceName: The name of the device in Ignition.

    Returns:
        The hostname of the device. Null if device doesn't have a
        hostname.
    """
    print(deviceName)
    return ""


def listDevices():
    # type: () -> BasicDataset
    """Returns a dataset of information about each configured device.

    Each row represents a single device.

    Returns:
        A dataset, where each row represents a device. Contains 4
        columns Name, Enabled, State, and Driver.
    """
    return BasicDataset()


def refreshBrowse(deviceName):
    # type: (String) -> None
    """Forces Ignition to browse the controller.

    Only works for Allen-Bradley controllers.

    Args:
        deviceName: The name of the device in Ignition.
    """
    print(deviceName)


def removeDevice(deviceName):
    # type: (String) -> None
    """Removes a given device from Ignition.

    Args:
        deviceName: The name of the device in Ignition.
    """
    print(deviceName)


def setDeviceEnabled(deviceName, enabled):
    # type: (String, bool) -> None
    """Enables/disables a device in Ignition.

    Args:
        deviceName: The name of the device in Ignition.
        enabled: The enabled status of the device.
    """
    print(deviceName, enabled)


def setDeviceHostname(deviceName, hostname):
    # type: (String, String) -> None
    """Changes the hostname of a device.

    Used for all ethernet based drivers.

    Args:
        deviceName: The name of the device in Ignition.
        hostname: The new IP address or hostname.
    """
    print(deviceName, hostname)
