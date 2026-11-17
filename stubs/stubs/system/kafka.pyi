from typing import Any, Dict, List, Optional, Union

def listConnectorInfo() -> List[Dict[Union[str, unicode], Any]]: ...
def listTopicPartitions(
    connector: Union[str, unicode],
    topic: Union[str, unicode],
    groupId: Union[str, unicode],
    options: Optional[Dict[Union[str, unicode], Any]] = ...,
) -> List[Any]: ...
def listTopics(connector: Union[str, unicode]) -> List[Any]: ...
def pollPartition(
    connector: Union[str, unicode],
    topic: Union[str, unicode],
    partition: int,
    offset: Union[str, unicode],
    options: Optional[Dict[Union[str, unicode], Any]] = ...,
    sizeCutoff: Optional[int] = ...,
    timeoutMs: Optional[long] = ...,
) -> List[Any]: ...
def pollTopic(
    connector: Union[str, unicode],
    topic: Union[str, unicode],
    groupId: Union[str, unicode],
    options: Optional[Dict[Union[str, unicode], Any]] = ...,
    sizeCutoff: Optional[int] = ...,
    timeoutMs: Optional[long] = ...,
) -> List[Any]: ...
def seekLatest(
    connector: Union[str, unicode],
    topic: Union[str, unicode],
    partition: int,
    recordCount: int,
    options: Optional[Dict[Union[str, unicode], Any]] = ...,
) -> List[Any]: ...
def sendRecord(
    connector: Union[str, unicode],
    topic: Union[str, unicode],
    key: Union[str, unicode],
    value: Union[str, unicode],
    partition: Optional[int] = ...,
    timestamp: Optional[long] = ...,
    headerKeys: Optional[List[Any]] = ...,
    headerValues: Optional[List[Any]] = ...,
    options: Optional[Dict[Union[str, unicode], Any]] = ...,
) -> Dict[Union[str, unicode], Any]: ...
def sendRecordAsync(
    connector: Union[str, unicode],
    topic: Union[str, unicode],
    key: Union[str, unicode],
    value: Union[str, unicode],
    partition: Optional[int] = ...,
    timestamp: Optional[long] = ...,
    headerKeys: Optional[List[Any]] = ...,
    headerValues: Optional[List[Any]] = ...,
    options: Optional[Dict[Union[str, unicode], Any]] = ...,
) -> None: ...
