from typing import Any, Dict, Optional, Union

from com.inductiveautomation.historian.common.model.data import (
    AnnotationPoint,
    AtomicPoint,
    MetadataPoint,
)
from java.util import Date

def annotationPoint(
    source: Union[str, unicode],
    startTime: Date,
    endTime: Optional[Date] = ...,
    annotationType: Optional[Union[str, unicode]] = ...,
    data: Optional[Union[str, unicode]] = ...,
    identifier: Optional[Union[str, unicode]] = ...,
) -> AnnotationPoint: ...
def dataPoint(
    source: Union[str, unicode],
    value: object,
    timestamp: Optional[Date] = ...,
    quality: Optional[int] = ...,
) -> AtomicPoint: ...
def metadataPoint(
    source: Union[str, unicode],
    properties: Dict[Union[str, unicode], Any],
    timestamp: Date,
) -> MetadataPoint: ...
