from __future__ import print_function

__all__ = [
    "Annotation",
    "AnnotationPoint",
    "AtomicPoint",
    "DataPoint",
    "MetadataPoint",
    "SnapshotCapable",
    "StandardComplexPointType",
    "TemporalPoint",
]

from typing import Any, List, Optional, Union

from java.lang import Class, Comparable, Enum, Object, Record
from java.time import Instant
from java.util import UUID

from com.inductiveautomation.ignition.common import QualifiedPath
from com.inductiveautomation.ignition.common.config import PropertySet, PropertyValue
from com.inductiveautomation.ignition.common.model.values import QualityCode


class SnapshotCapable(object):
    def isSnapshot(self):
        # type: () -> bool
        pass

    def snapshotTime(self):
        # type: () -> Optional[Instant]
        pass

    def withSnapshot(self, timestamp=None):
        # type: (Optional[Instant]) -> SnapshotCapable
        pass


class TemporalPoint(Comparable):
    def compareTo(self, other):
        # type: (TemporalPoint) -> int
        pass

    def source(self):
        # type: () -> QualifiedPath
        pass

    def timestamp(self):
        # type: () -> Instant
        pass

    def type(self):
        # type: () -> Any
        pass

    def value(self):
        # type: () -> Any
        pass


class DataPoint(SnapshotCapable, TemporalPoint):
    def quality(self):
        # type: () -> QualityCode
        pass

    def valueClass(self):
        # type: () -> Any
        pass


class AtomicPoint(DataPoint):
    pass


class Annotation(Record):
    def __init__(
        self,
        notes,  # type: Union[str, unicode]
        type_,  # type: Union[str, unicode]
        author,  # type: Union[str, unicode]
    ):
        # type: (...) -> None
        super(Annotation, self).__init__()

    def author(self):
        # type: () -> Union[str, unicode]
        pass

    def notes(self):
        # type: () -> Union[str, unicode]
        pass

    def type(self):
        # type: () -> Union[str, unicode]
        pass


class AnnotationPoint(Record):
    class Builder(Object):
        def __init__(self):
            # type: () -> None
            super(AnnotationPoint.Builder, self).__init__()

        def annotationType(self, annotationType):
            # type: (Union[str, unicode]) -> AnnotationPoint.Builder
            pass

        def author(self, author):
            # type: (Union[str, unicode]) -> AnnotationPoint.Builder
            pass

        def build(self):
            # type: () -> AnnotationPoint
            pass

        def endTime(self, endTime):
            # type: (Instant) -> AnnotationPoint.Builder
            pass

        def identifier(
            self,
            identifier,  # type: Union[UUID, str, unicode]
        ):
            # type: (...) -> AnnotationPoint.Builder
            pass

        def lastUpdated(self, lastUpdated):
            # type: (Instant) -> AnnotationPoint.Builder
            pass

        def notes(self, notes):
            # type: (Union[str, unicode]) -> AnnotationPoint.Builder
            pass

        def source(self, source):
            # type: (QualifiedPath) -> AnnotationPoint.Builder
            pass

        def startTime(self, startTime):
            # type: (Instant) -> AnnotationPoint.Builder
            pass

    def __init__(
        self,
        identifier,  # type: UUID
        source,  # type: QualifiedPath
        value,  # type: Annotation
        startTime,  # type: Instant
        endTime=None,  # type: Optional[Instant]
        lastUpdated=None,  # type: Optional[Instant]
    ):
        # type: (...) -> None
        super(AnnotationPoint, self).__init__()
        print(identifier, source, value, startTime, endTime, lastUpdated)

    @staticmethod
    def builder():
        # type: () -> AnnotationPoint.Builder
        pass

    def endTime(self):
        # type: () -> Optional[Instant]
        pass

    def identifier(self):
        # type: () -> UUID
        pass

    def lastUpdated(self):
        # type: () -> Optional[Instant]
        pass

    def source(self):
        # type: () -> QualifiedPath
        pass

    def startTime(self):
        # type: () -> Instant
        pass

    def timestamp(self):
        # type: () -> Instant
        pass

    def type(self):
        # type: () -> StandardComplexPointType
        pass

    def value(self):
        # type: () -> Annotation
        pass

    def withSource(self, source):
        # type: (QualifiedPath) -> AnnotationPoint
        pass


class MetadataPoint(Record, TemporalPoint):
    class Builder(Object):
        def __init__(self):
            # type: () -> None
            super(MetadataPoint.Builder, self).__init__()

        def addValue(self, value):
            # type: (PropertyValue) -> MetadataPoint.Builder
            pass

        def build(self):
            # type: () -> MetadataPoint
            pass

        def quality(self, quality):
            # type: (QualityCode) -> MetadataPoint.Builder
            pass

        def source(self, source):
            # type: (QualifiedPath) -> MetadataPoint.Builder
            pass

        def timestamp(self, timestamp):
            # type: (Instant) -> MetadataPoint.Builder
            pass

        def values(self, values):
            # type: (PropertySet) -> MetadataPoint.Builder
            pass

    def __init__(
        self,
        value,  # type: PropertySet
        quality,  # type: QualityCode
        timestamp,  # type: Instant
        source,  # type: QualifiedPath
    ):
        # type: (...) -> None
        super(MetadataPoint, self).__init__()
        print(value, quality, timestamp, source)

    @staticmethod
    def builder(metadataPoint=None):
        # type: (Optional[MetadataPoint]) -> MetadataPoint.Builder
        pass

    @staticmethod
    def empty(source):
        # type: (QualifiedPath) -> MetadataPoint
        pass

    def quality(self):
        # type: () -> QualityCode
        pass

    def withSource(self, source):
        # type: (QualifiedPath) -> MetadataPoint
        pass


class StandardComplexPointType(Enum):
    ANNOTATION = None  # type: StandardComplexPointType
    GENERIC = None  # type: StandardComplexPointType
    METADATA = None  # type: StandardComplexPointType

    def getPointClass(self):
        # type: () -> Class
        pass

    def getQueryOptionsClass(self):
        # type: () -> Class
        pass

    @staticmethod
    def values():
        # type: () -> List[StandardComplexPointType]
        pass
