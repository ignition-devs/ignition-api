"""Historian Functions.

The following functions give you access to interact with the Historian
system.
"""

from __future__ import print_function

__all__ = [
    "browse",
    "deleteAnnotations",
    "queryAggregatedPoints",
    "queryAnnotations",
    "queryMetadata",
    "queryRawPoints",
    "storeAnnotations",
    "storeDataPoints",
    "storeMetadata",
    "updateRegisteredNodePath",
]

from typing import Any, List, Optional, Union

from java.util import Date

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.browsing import Results
from com.inductiveautomation.ignition.common.model.values import BasicQualifiedValue


def browse(rootPath, *args, **kwargs):
    # type: (Union[str, unicode], *Any, **Any) -> Results
    """Returns a list of browse results for the specified Historian."""
    print(rootPath, args, kwargs)
    return Results()


def deleteAnnotations(
    paths,  # type: List[Union[str, unicode]]
    storageIds,  # type: List[Union[str, unicode]]
):
    # type: (...) -> List[BasicQualifiedValue]
    """Deletes desired annotations from the specified Historian.

    Args:
        paths: A list of historical paths associated with the
            annotations.
        storageIds: A list of annotation storage IDs to be used for
            deleting.

    Returns:
        A list of qualified values. The quality code will indicate
        success or failure, and if successful, the storage ID of the
        annotation will have been deleted.
    """
    print(paths, storageIds)
    return [BasicQualifiedValue() for _ in paths]


def queryAggregatedPoints(
    paths,  # type: List[Union[str, unicode]]
    startTime=None,  # type: Optional[Date]
    endTime=None,  # type: Optional[Date]
    aggregates=None,  # type: Optional[List[Union[str, unicode]]]
    fillModes=None,  # type: Optional[List[Union[str, unicode]]]
    columnNames=None,  # type: Optional[List[Union[str, unicode]]]
    returnFormat="Wide",  # type: str
    returnSize=1,  # type: int
    includeBounds=False,  # type: bool
    excludeObservations=False,  # type: bool
):
    # type: (...) -> BasicDataset
    """Queries aggregated data points for the specified historian.

    Args:
        paths: A list of historical paths to query aggregated data
            points for.
        startTime: A start time to query aggregated data points for.
        endTime: An end time to query aggregated data points for.
        aggregates: A list of aggregate functions to apply to the query.
            Optional.
        fillModes: A list of fill modes to apply to the query. Optional.
        columnNames: A list of alias column names for the returned
            dataset. Optional.
        returnFormat: The desired return format for the query. Optional.
        returnSize: The number maximum of results to return. Optional.
        includeBounds: Whether to include the bounds in the query
            results. Optional.
        excludeObservations: Whether to exclude observed aggregated data
            points in the query results. Optional.

    Returns:
        A dataset representing the aggregated points for the specified
        historical paths.
    """
    print(
        paths,
        startTime,
        endTime,
        aggregates,
        fillModes,
        columnNames,
        returnFormat,
        returnSize,
        includeBounds,
        excludeObservations,
    )
    return BasicDataset()


def queryAnnotations(
    paths,  # type: List[Union[str, unicode]]
    startDate=None,  # type: Optional[Date]
    endDate=None,  # type: Optional[Date]
    allowedTypes=None,  # type: Optional[List[Union[str, unicode]]]
):
    # type: (...) -> Results
    """Queries user stored annotations from the Tag history system for a
    set of paths, for a given time range.

    Args:
        paths: A list of historical paths to query annotations for.
        startDate: A start time to query annotations for.
        endDate: An end time to query annotations for. Optional.
        allowedTypes: A list of string types to query annotations for.
            Optional.

    Returns:
        A Results object that contains a list of query results.
    """
    print(paths, startDate, endDate, allowedTypes)
    return Results()


def queryMetadata(
    paths,  # type: List[Union[str, unicode]]
    startDate=None,  # type: Optional[Date]
    endDate=None,  # type: Optional[Date]
):
    # type: (...) -> Results
    """Queries metadata for the specified Historian.

    Args:
        paths: A list of historical paths to query metadata for.
        startDate: A start time to query metadata for. This parameter is
            optional, unless an end time is specified.
        endDate: An end time to query metadata for. If specifying an end
            time, a start time must be provided. Optional.

    Returns:
        A Results object that contains a list of query results.
    """
    print(paths, startDate, endDate)
    return Results()


def queryRawPoints(
    paths,  # type: List[Union[str, unicode]]
    startTime=None,  # type: Optional[Date]
    endTime=None,  # type: Optional[Date]
    columnNames=None,  # type: Optional[List[Union[str, unicode]]]
    returnFormat="Wide",  # type: str
    returnSize=-1,  # type: int
    includeBounds=False,  # type: bool
    excludeObservations=False,  # type: bool
):
    # type: (...) -> BasicDataset
    """Queries raw data points for the specified Historian.

    Args:
        paths: list A list of historical paths to query raw data points
            for.
        startTime: Date A start time to query raw data points for.
        endTime: Date An end time to query raw data points for.
        columnNames: A list of alias column names for the returned
            dataset. Optional.
        returnFormat: The desired return format for the query. Optional.
        returnSize: The maximum number of results to return. Optional.
        includeBounds: Whether to include the bounds in the query
            results. Optional.
        excludeObservations: Whether to exclude observed raw data points
            in the query results. Optional.

    Returns:
        A dataset representing the raw data points for the specified
        historical paths.
    """
    print(
        paths,
        startTime,
        endTime,
        columnNames,
        returnFormat,
        returnSize,
        includeBounds,
        excludeObservations,
    )
    return BasicDataset()


def storeAnnotations(*args, **kwargs):
    # type: (*Any, **Any) -> List[BasicQualifiedValue]
    """Store a list of annotations to the specified Historian.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        A list of qualified values. The quality code will indicate
        success or failure.
    """
    print(args, kwargs)
    return [BasicQualifiedValue()]


def storeDataPoints(*args, **kwargs):
    # type: (*Any, **Any) -> List[BasicQualifiedValue]
    """Store a list of data points to the specified Historian.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        A list of qualified values. The quality code will indicate
        success or failure.
    """
    print(args, kwargs)
    return [BasicQualifiedValue()]


def storeMetadata(*args, **kwargs):
    # type: (*Any, **Any) -> List[BasicQualifiedValue]
    """Store a list of metadata to the specified Historian.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        A list of qualified values. The quality code will indicate
        success or failure.
    """
    print(args, kwargs)
    return [BasicQualifiedValue()]


def updateRegisteredNodePath(
    previousPath,  # type: Union[str, unicode]
    currentPath,  # type: Union[str, unicode]
):
    # type: (...) -> List[BasicQualifiedValue]
    """Updates the existing historical path for a stored historian node
    to the newly specific path.

    Args:
        previousPath: The previous path for the historian node.
        currentPath: The new current path for the historian node. If
            null, then the historian node will be retired.

    Returns:
        A list of qualified values. The quality code will indicate
        success or failure, and if successful, the path will be updated.
    """
    print(previousPath, currentPath)
    return [BasicQualifiedValue()]
