from typing import Any, List, Optional, Union

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.browsing import Results
from com.inductiveautomation.ignition.common.model.values import BasicQualifiedValue
from java.util import Date

def browse(rootPath: Union[str, unicode], *args: Any, **kwargs: Any) -> Results: ...
def deleteAnnotations(
    paths: List[Union[str, unicode]], storageIds: List[Union[str, unicode]]
) -> List[BasicQualifiedValue]: ...
def queryAggregatedPoints(
    paths: List[Union[str, unicode]],
    startTime: Optional[Date] = ...,
    endTime: Optional[Date] = ...,
    aggregates: Optional[List[Union[str, unicode]]] = ...,
    fillModes: Optional[List[Union[str, unicode]]] = ...,
    columnNames: Optional[List[Union[str, unicode]]] = ...,
    returnFormat: str = ...,
    returnSize: int = ...,
    includeBounds: bool = ...,
    excludeObservations: bool = ...,
) -> BasicDataset: ...
def queryAnnotations(
    paths: List[Union[str, unicode]],
    startDate: Optional[Date] = ...,
    endDate: Optional[Date] = ...,
    allowedTypes: Optional[List[Union[str, unicode]]] = ...,
) -> Results: ...
def queryMetadata(
    paths: List[Union[str, unicode]],
    startDate: Optional[Date] = ...,
    endDate: Optional[Date] = ...,
) -> Results: ...
def queryRawPoints(
    paths: List[Union[str, unicode]],
    startTime: Optional[Date] = ...,
    endTime: Optional[Date] = ...,
    columnNames: Optional[List[Union[str, unicode]]] = ...,
    returnFormat: str = ...,
    returnSize: int = ...,
    includeBounds: bool = ...,
    excludeObservations: bool = ...,
) -> BasicDataset: ...
def storeAnnotations(*args: Any, **kwargs: Any) -> List[BasicQualifiedValue]: ...
def storeDataPoints(*args: Any, **kwargs: Any) -> List[BasicQualifiedValue]: ...
def storeMetadata(*args: Any, **kwargs: Any) -> List[BasicQualifiedValue]: ...
def updateRegisteredNodePath(
    previousPath: Union[str, unicode], currentPath: Union[str, unicode]
) -> List[BasicQualifiedValue]: ...
