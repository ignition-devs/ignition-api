from typing import Any, Callable, Dict, List, Optional, Union

from com.inductiveautomation.ignition.common.browsing import Results
from com.inductiveautomation.ignition.common.model.values import (
    BasicQualifiedValue,
    QualityCode,
)

DEFAULT_TIMEOUT_MILLIS: int
LEGACY_DEFAULT_TIMEOUT_MILLIS: int
TAG_PATH: Any

def browse(
    path: Union[str, unicode], filter: Optional[Dict[Union[str, unicode], Any]] = ...
) -> Results: ...
def configure(
    basePath: Union[str, unicode],
    tags: List[Dict[Union[str, unicode], Any]],
    collisionPolicy: Union[str, unicode] = ...,
) -> List[QualityCode]: ...
def copy(
    tags: List[Union[str, unicode]],
    destination: Union[str, unicode],
    collisionPolicy: Union[str, unicode] = ...,
) -> List[QualityCode]: ...
def deleteTags(tagPaths: List[Union[str, unicode]]) -> List[QualityCode]: ...
def exists(tagPath: Union[str, unicode]) -> bool: ...
def exportTags(
    filePath: Union[str, unicode, None] = ...,
    tagPaths: Optional[List[Union[str, unicode]]] = ...,
    recursive: bool = ...,
    exportType: Union[str, unicode] = ...,
) -> Union[str, unicode, None]: ...
def getConfiguration(
    basePath: Union[str, unicode], recursive: bool = ...
) -> List[Dict[Union[str, unicode], Any]]: ...
def importTags(
    filePath: Union[str, unicode],
    basePath: Union[str, unicode],
    collisionPolicy: Union[str, unicode] = ...,
) -> List[QualityCode]: ...
def move(
    tags: List[Union[str, unicode]],
    destination: Union[str, unicode],
    collisionPolicy: Union[str, unicode] = ...,
) -> List[QualityCode]: ...
def query(
    provider: Union[str, unicode, None] = ...,
    query: Optional[Dict[Union[str, unicode], Any]] = ...,
    limit: Optional[int] = ...,
    continuation: Union[str, unicode, None] = ...,
) -> Results: ...
def readAsync(
    tagPaths: List[Union[str, unicode]], callback: Callable[..., Any]
) -> None: ...
def readBlocking(
    tagPaths: List[Union[str, unicode]], timeout: int = ...
) -> List[BasicQualifiedValue]: ...
def rename(
    tag: Union[str, unicode],
    newName: Union[str, unicode],
    collisionPollicy: Union[str, unicode] = ...,
) -> QualityCode: ...
def requestGroupExecution(
    provider: Union[str, unicode], tagGroup: Union[str, unicode]
) -> None: ...
def restartProvider(provider: Union[str, unicode]) -> bool: ...
def writeAsync(
    tagPaths: List[Union[str, unicode]],
    values: List[Any],
    callback: Optional[Callable[..., Any]] = ...,
) -> None: ...
def writeBlocking(
    tagPaths: List[Union[str, unicode]], values: List[Any], timeout: int = ...
) -> List[QualityCode]: ...
