from typing import List, Union

def demandPoll(deviceName: Union[str, unicode], classList: List[int]) -> None: ...
def directOperateAnalog(
    deviceName: Union[str, unicode],
    variation: int,
    index: int,
    value: Union[float, int, long],
) -> None: ...
def directOperateBinary(
    deviceName: Union[str, unicode],
    index: int,
    tcc: int,
    opType: int,
    count: int,
    onTime: int,
    offTime: int,
) -> None: ...
def freezeAnalogs(deviceName: Union[str, unicode], indexes: List[int]) -> None: ...
def freezeAtTimeAnalogs(
    deviceName: Union[str, unicode],
    absoluteTime: int,
    intervalTime: int,
    indexes: List[int],
) -> None: ...
def freezeAtTimeCounters(
    deviceName: Union[str, unicode],
    absoluteTime: int,
    intervalTime: int,
    indexes: List[int],
) -> None: ...
def freezeClearAnalogs(deviceName: Union[str, unicode], indexes: List[int]) -> None: ...
def freezeClearCounters(
    deviceName: Union[str, unicode], indexes: List[int]
) -> None: ...
def freezeCounters(deviceName: Union[str, unicode], indexes: List[int]) -> None: ...
def selectOperateAnalog(
    deviceName: Union[str, unicode],
    variation: int,
    index: int,
    value: Union[float, int, long],
) -> None: ...
def selectOperateBinary(
    deviceName: Union[str, unicode],
    index: int,
    tcc: int,
    opType: int,
    count: int,
    onTime: int,
    offTime: int,
) -> None: ...
def synchronizeTime(deviceName: Union[str, unicode]) -> None: ...
