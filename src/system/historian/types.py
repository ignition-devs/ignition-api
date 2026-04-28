"""Historian types."""

__all__ = ["annotationPoint", "dataPoint", "metadataPoint"]

from typing import Any, Dict, Optional, Union

from java.util import Date

from com.inductiveautomation.historian.common.model.data import (
    AnnotationPoint,
    AtomicPoint,
    MetadataPoint,
)


def annotationPoint(
    source,  # type: Union[str, unicode]
    startTime,  # type: Date
    endTime=None,  # type: Optional[Date]
    annotationType=None,  # type: Optional[Union[str, unicode]]
    data=None,  # type: Optional[Union[str, unicode]]
    identifier=None,  # type: Optional[Union[str, unicode]]
):
    # type: (...) -> AnnotationPoint
    """Creates an annotation point that can be stored to a historian.

    Annotation points represent time-based context, such as operator
    notes, events, or system-generated markers associated with a
    historical path.

    Args:
        source: The historical path where the annotation point will be
            stored.
        startTime: The start time associated with the annotation.
        endTime: The end time associated with the annotation. If
            omitted, the annotation has no end time. Optional.
        annotationType: A string used to categorize the annotation
            (for example, "marker", "note", or "event"). If omitted,
            "marker" is used. Optional.
        data: A string payload associated with the annotation. This can
            contain plain text or structured data, such as JSON. If
            omitted, an empty string is used. Optional.
        identifier: An identifier used to indicate that an existing
            annotation should be updated. Optional.

    Returns:
        An annotation point object that can be passed to
        system.historian.storeAnnotations.
    """
    builder = AnnotationPoint.builder()
    return builder.build()


def dataPoint(
    source,  # type: Union[str, unicode]
    value,  # type: object
    timestamp=None,  # type: Optional[Date]
    quality=None,  # type: Optional[int]
):
    # type: (...) -> AtomicPoint
    """Creates a data point that can be stored to a historian.

    Data points represent individual values associated with a historical
    path, timestamp, and quality.

    Args:
        source: The historical path where the data point will be stored.
        value: The value to be stored in the historian.
        timestamp: The timestamp when the data point was recorded. If
            omitted, the current time is used. Optional.
        quality: The quality code of the data point. If omitted, a
            "good" quality is used. Optional.

    Returns:
        A data point object that can be passed to
        system.historian.storeDataPoints.
    """
    return AtomicPoint()


def metadataPoint(
    source,  # type: Union[str, unicode]
    properties,  # type: Dict[Union[str, unicode], Any]
    timestamp,  # type: Date
):
    # type: (...) -> MetadataPoint
    """Creates a metadata point that can be stored to a historian.

    Metadata points allow you to store additional properties associated
    with a historical path at a specific point in time.

    Args:
        source: The historical path where the metadata point will be
            stored.
        properties: A dictionary of properties to be stored as
            historical metadata.
        timestamp: The timestamp when the metadata point was recorded.

    Returns:
        A metadata point object that can be passed to
        system.historian.storeMetadata.
    """
    builder = MetadataPoint.builder()
    return builder.build()
