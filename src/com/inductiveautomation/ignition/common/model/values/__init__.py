__all__ = ["BasicQualifiedValue", "BasicQuality", "QualifiedValue", "Quality"]


class QualifiedValue(object):
    """Represents a value with a DataQuality & timestamp attached to
    it.
    """

    def getQuality(self):
        raise NotImplementedError

    def getTimestamp(self):
        raise NotImplementedError

    def getValue(self):
        raise NotImplementedError


class BasicQualifiedValue(QualifiedValue):
    def getQuality(self):
        pass

    def getTimestamp(self):
        pass

    def getValue(self):
        pass


class Quality(object):
    def getDescription(self):
        raise NotImplementedError

    def getLevel(self):
        raise NotImplementedError

    def getName(self):
        raise NotImplementedError

    def getQualityCode(self):
        raise NotImplementedError

    def isGood(self):
        raise NotImplementedError


class BasicQuality(Quality):
    def getDescription(self):
        pass

    def getLevel(self):
        pass

    def getName(self):
        pass

    def getQualityCode(self):
        pass

    def isGood(self):
        pass
