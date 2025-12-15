__all__ = [
    "BoundType",
    "DiscreteDomain",
    "ImmutableCollection",
    "ImmutableList",
    "ImmutableSet",
    "Range",
    "UnmodifiableIterator",
    "UnmodifiableListIterator",
]

from typing import Any, Iterable, List, Optional

from java.lang import Enum, Object
from java.util import AbstractCollection, Comparator
from java.util.stream import Collector


class BoundType(Enum):
    CLOSED = "CLOSED"
    OPEN = "OPEN"

    @staticmethod
    def values():
        # type: () -> List[BoundType]
        pass


class DiscreteDomain(Object):
    @staticmethod
    def bigIntegers():
        # type: () -> DiscreteDomain
        pass

    def distance(self, start, end):
        # type: (Any, Any) -> long
        raise NotImplementedError

    @staticmethod
    def integers():
        # type: () -> DiscreteDomain
        pass

    @staticmethod
    def longs():
        # type: () -> DiscreteDomain
        pass

    def maxValue(self):
        # type: () -> Any
        pass

    def minValue(self):
        # type: () -> Any
        pass

    def next(self, value):
        # type: (Any) -> Any
        raise NotImplementedError

    def previous(self, value):
        # type: (Any) -> Any
        raise NotImplementedError


class ImmutableCollection(AbstractCollection):
    class Builder(Object):
        def add(self, *elements):
            # type: (*Any) -> ImmutableCollection.Builder
            pass

        def addAll(self, elements):
            # type: (Any) -> ImmutableCollection.Builder
            pass

        def build(self):
            # type: () -> ImmutableCollection
            raise NotImplementedError

    def asList(self):
        # type: () -> ImmutableList
        pass

    def contains(self, o):
        # type: (Object) -> bool
        raise NotImplementedError


class ImmutableList(ImmutableCollection):
    class Builder(ImmutableCollection.Builder):
        def build(self):
            # type: () -> ImmutableList
            pass

    @staticmethod
    def builder():
        # type: () -> ImmutableList.Builder
        pass

    @staticmethod
    def builderWithExpectedSize():
        # type: () -> ImmutableList.Builder
        pass

    def contains(self, o):
        # type: (Object) -> bool
        return True

    @staticmethod
    def copyOf(*args):
        # type: (*Any) -> ImmutableList
        pass

    def indexOf(self, obj):
        # type: (Object) -> int
        pass

    def lastIndexOf(self, obj):
        # type: (Object) -> int
        pass

    def listIterator(self, index=None):
        # type: (Optional[int]) -> UnmodifiableListIterator
        pass

    @staticmethod
    def of(*args):
        # type: (*Any) -> ImmutableList
        pass

    @staticmethod
    def sortedCopyOf(comparator, elements):
        # type: (Comparator, Iterable[Any]) -> ImmutableList
        pass

    def subList(self, fromIndex, toIndex):
        # type: (int, int) -> ImmutableList
        pass

    @staticmethod
    def toImmutableList():
        # type: () -> Collector
        pass


class ImmutableSet(ImmutableCollection):
    class Builder(ImmutableCollection.Builder):
        def __init__(self):
            # type: () -> None
            super(ImmutableSet.Builder, self).__init__()

        def build(self):
            # type: () -> ImmutableSet
            pass

    @staticmethod
    def builder():
        # type: () -> ImmutableSet.Builder
        pass

    @staticmethod
    def builderWithExpectedSize():
        # type: () -> ImmutableSet.Builder
        pass

    def contains(self, o):
        # type: (Object) -> bool
        return True

    @staticmethod
    def copyOf(*args):
        # type: (*Any) -> ImmutableSet
        pass

    @staticmethod
    def of(*args):
        # type: (*Any) -> ImmutableSet
        pass

    @staticmethod
    def toImmutableSet():
        # type: () -> Collector
        pass


class Range(Object):
    @staticmethod
    def all():
        # type: () -> Range
        pass

    def apply(self, input):
        # type: (Any) -> bool
        pass

    @staticmethod
    def atLeast(endpoint):
        # type: (Any) -> Range
        pass

    @staticmethod
    def atMost(endpoint):
        # type: (Any) -> Range
        pass

    def canonical(self, domain):
        # type: (DiscreteDomain) -> Range
        pass

    @staticmethod
    def closed(lower, upper):
        # type: (Any, Any) -> Range
        pass

    @staticmethod
    def closedOpen(lower, upper):
        # type: (Any, Any) -> Range
        pass

    def contains(self, value):
        # type: (Any) -> bool
        pass

    def containsAll(self, values):
        # type: (Iterable[Any]) -> bool
        pass

    @staticmethod
    def downTo(endpoint):
        # type: (Any) -> Range
        pass

    @staticmethod
    def encloseAll(values):
        # type: (Iterable[Any]) -> Range
        pass

    def encloses(self, other):
        # type: (Range) -> bool
        pass

    def gap(self, otherRange):
        # type: (Range) -> Range
        pass

    @staticmethod
    def greaterThan(endpoint):
        # type: (Any) -> Range
        pass

    def hasLowerBound(self):
        # type: () -> bool
        pass

    def hasUpperBound(self):
        # type: () -> bool
        pass

    def intersection(self, connectedRange):
        # type: (Range) -> Range
        pass

    def isConnected(self, other):
        # type: (Range) -> bool
        pass

    def isEmpty(self):
        # type: () -> bool
        pass

    @staticmethod
    def lessThan(endpoint):
        # type: (Any) -> Range
        pass

    def lowerBoundType(self):
        # type: () -> BoundType
        pass

    def lowerEndpoint(self):
        # type: () -> Any
        pass

    @staticmethod
    def open(lower, upper):
        # type: (Any, Any) -> Range
        pass

    @staticmethod
    def openClosed(lower, upper):
        # type: (Any, Any) -> Range
        pass

    @staticmethod
    def range(lower, lowerType, upper, upperType):
        # type: (Any, BoundType, Any, BoundType) -> Range
        pass

    @staticmethod
    def singleton(value):
        # type: (Any) -> Range
        pass

    def span(self, other):
        # type: (Range) -> Range
        pass

    def upperBoundType(self):
        # type: () -> BoundType
        pass

    def upperEndpoint(self):
        # type: () -> Any
        pass

    @staticmethod
    def upTo(endpoint, boundType):
        # type: (Any, BoundType) -> Range
        pass


class UnmodifiableIterator(Object):
    def remove(self):
        # type: () -> None
        pass


class UnmodifiableListIterator(UnmodifiableIterator):
    def add(self, e):
        # type: (Any) -> None
        pass

    def set(self, e):
        # type: (Any) -> None
        pass
