"""DNP Functions.

The following functions give you access to interact with the DNP3
devices.
"""

from __future__ import print_function

__all__ = [
    "demandPoll",
    "directOperateAnalog",
    "directOperateBinary",
    "freezeAnalogs",
    "freezeAtTimeAnalogs",
    "freezeAtTimeCounters",
    "freezeClearAnalogs",
    "freezeClearCounters",
    "freezeCounters",
    "selectOperateAnalog",
    "selectOperateBinary",
    "synchronizeTime",
]

from typing import List, Union


def demandPoll(deviceName, classList):
    # type: (Union[str, unicode], List[int]) -> None
    """Issues a poll request for one or more classes.

    Args:
        deviceName: The name of the DNP3 device instance.
        classList: A List of classes (1, 2, 3) to issue polls.
    """
    print(deviceName, classList)


def directOperateAnalog(
    deviceName,  # type: Union[str, unicode]
    variation,  # type: int
    index,  # type: int
    value,  # type: Union[float, int, long]
):
    # type: (...) -> None
    """Issues a Direct Operate command to set an analog value in an
    analog output point.

    Args:
        deviceName: The name of the DNP3 device instance.
        variation: The Group 41 variation to use during the operation.
        index: The index of the analog point.
        value: The requested value.
    """
    print(deviceName, variation, index, value)


def directOperateBinary(deviceName, index, tcc, opType, count, onTime, offTime):
    # type: (Union[str, unicode], int, int, int, int, int, int) -> None
    """Performs a Direct Operate command on a binary point.

    Args:
        deviceName: The name of the DNP3 device instance.
        index: The index of the binary point.
        tcc: Trip Close Code: 0=NUL, 1=CLOSE, 2=TRIP.
        opType: Operation Type: 0=NUL, 1=PULSE_ON, 2=PULSE_OFF,
            3=LATCH_ON, 4=LATCH_OFF.
        count: The number of times the outstation shall execute the
            operation.
        onTime: Duration (in milliseconds) the output drive remains
            active.
        offTime: Duration (in milliseconds) the output drive remains
            non-active.
    """
    print(deviceName, index, tcc, opType, count, onTime, offTime)


def freezeAnalogs(deviceName, indexes):
    # type: (Union[str, unicode], List[int]) -> None
    """Issues an Immediate Freeze command targeting one or more analog
    points.

    Args:
        deviceName: The name of the DNP3 device instance.
        indexes: The indices of the analog points to freeze.
    """
    print(deviceName, indexes)


def freezeAtTimeAnalogs(deviceName, absoluteTime, intervalTime, indexes):
    # type: (Union[str, unicode], int, int, List[int]) -> None
    """Issues a Freeze at Time command targeting one or more analog
    points.

    Args:
        deviceName: The name of the DNP3 device instance.
        absoluteTime: Absolute time (in milliseconds since epoch UTC)
            when the initial action should occur.
        intervalTime: Interval time (in milliseconds) between periodic
            actions.
        indexes: The indices of the analog points to freeze.
    """
    print(deviceName, absoluteTime, intervalTime, indexes)


def freezeAtTimeCounters(deviceName, absoluteTime, intervalTime, indexes):
    # type: (Union[str, unicode], int, int, List[int]) -> None
    """Issues a Freeze at Time command targeting one or more counters.

    Args:
        deviceName: The name of the DNP3 device instance.
        absoluteTime: Absolute time (in milliseconds since epoch UTC)
            when the initial action should occur.
        intervalTime: Interval time (in milliseconds) between periodic
            actions.
        indexes: The indices of the counter to freeze.
    """
    print(deviceName, absoluteTime, intervalTime, indexes)


def freezeClearAnalogs(deviceName, indexes):
    # type: (Union[str, unicode], List[int]) -> None
    """Issues a Freeze and Clear command targeting one or more analog
    points.

    Args:
        deviceName: The name of the DNP3 device instance.
        indexes: The indices of the analog points to freeze.
    """
    print(deviceName, indexes)


def freezeClearCounters(deviceName, indexes):
    # type: (Union[str, unicode], List[int]) -> None
    """Issues a Freeze and Clear command targeting one or more counters.

    Args:
        deviceName: The name of the DNP3 device instance.
        indexes: The indices of the counters to freeze.
    """
    print(deviceName, indexes)


def freezeCounters(deviceName, indexes):
    # type: (Union[str, unicode], List[int]) -> None
    """Issues an Immediate Freeze command targeting one or more
    counters.

    Args:
        deviceName: The name of the DNP3 device instance.
        indexes: The indices of the counters to freeze.
    """
    print(deviceName, indexes)


def selectOperateAnalog(
    deviceName,  # type: Union[str, unicode]
    variation,  # type: int
    index,  # type: int
    value,  # type: Union[float, int, long]
):
    # type: (...) -> None
    """Performs a Select then Operate command on an analog point.

    Args:
        deviceName: The name of the DNP3 device instance.
        variation: The Group 41 variation to use during the operation.
        index: The index of the analog point.
        value: The requested value.
    """
    print(deviceName, variation, index, value)


def selectOperateBinary(deviceName, index, tcc, opType, count, onTime, offTime):
    # type: (Union[str, unicode], int, int, int, int, int, int) -> None
    """Performs a Select then Operate command on a binary point.

    Args:
        deviceName: The name of the DNP3 device instance.
        index: The index of the binary point.
        tcc: Trip Close Code: 0=NUL, 1=CLOSE, 2=TRIP.
        opType: Operation Type: 0=NUL, 1=PULSE_ON, 2=PULSE_OFF,
            3=LATCH_ON, 4=LATCH_OFF.
        count: The number of times the outstation shall execute the
            operation.
        onTime: Duration (in milliseconds) the output drive remains
            active.
        offTime: Duration (in milliseconds) the output drive remains
            non-active.
    """
    print(deviceName, index, tcc, opType, count, onTime, offTime)


def synchronizeTime(deviceName):
    # type: (Union[str, unicode]) -> None
    """Issues a Synchronize Time command using the current Ignition
    Gateway time.

    Args:
        deviceName: The name of the DNP3 device instance.
    """
    print(deviceName)
