from __future__ import print_function

__all__ = ["AbstractOPCUtilities", "DatasetUtilities", "SProcCall", "SystemUtilities"]

from typing import List, Optional

from com.inductiveautomation.ignition.common import BasicDataset, Dataset
from com.inductiveautomation.ignition.common.opc import BrowseElementType
from com.inductiveautomation.ignition.common.script.message import Request
from java.lang import Object, String
from java.util import Locale
from org.python.core import PyObject


class AbstractOPCUtilities(Object):
    def browseServer(self, opcServer, nodeId):
        # type: (String, String) -> List[AbstractOPCUtilities.PyOPCTag]
        return [
            AbstractOPCUtilities.PyOPCTag(opcServer, nodeId, "", BrowseElementType())
        ]

    def getServers(self):
        pass

    def getServerState(self, opcServer):
        pass

    def isServerEnabled(self, serverName):
        pass

    def readValue(self, opcServer, itemPath):
        pass

    def readValues(self, opcServer, itemPaths):
        pass

    def setServerEnabled(self, serverName, enabled):
        pass

    def writeValue(self, *args, **kwargs):
        pass

    def writeValues(self, *args, **kwargs):
        pass

    class PyOPCTag(PyObject):
        _displayName = None
        _elementType = None
        _nodeId = None
        _serverName = None

        def __init__(self, serverName, nodeId, displayName, elementType):
            # type: (String, String, String, BrowseElementType) -> None
            self._serverName = serverName
            self._nodeId = nodeId
            self._displayName = displayName
            self._elementType = elementType
            super(AbstractOPCUtilities.PyOPCTag, self).__init__()

        def __findattr_ex__(self, name):
            pass

        def getDisplayName(self):
            return self._displayName

        def getElementType(self):
            return self._elementType

        def getNodeId(self):
            return self._nodeId

        def getServerName(self):
            return self._serverName


class DatasetUtilities(Object):
    @staticmethod
    def addColumn(*args):
        pass

    @staticmethod
    def addRow(*args):
        pass

    @staticmethod
    def addRows(*args):
        pass

    @staticmethod
    def appendDataset(ds1, ds2):
        pass

    @staticmethod
    def clearDataset(ds):
        pass

    @staticmethod
    def dataSetToExcel(headerRow, datasets):
        pass

    @staticmethod
    def dataSetToExcelBytes(headerRow, objects, nullsEmpty, sheetNames):
        pass

    @staticmethod
    def dataSetToExcelStreaming(headerRow, objects, out, nullsEmpty):
        pass

    @staticmethod
    def dataSetToHTML(headerRow, ds, title):
        pass

    @staticmethod
    def dataSetToHTMLStreaming(headerRow, ds, title, fw):
        pass

    @staticmethod
    def deleteRow(ds, row):
        pass

    @staticmethod
    def deleteRows(ds, rows):
        pass

    @staticmethod
    def filterColumns(dataset, columns):
        pass

    @staticmethod
    def formatDates(dataset, format, locale=Locale.US):
        pass

    @staticmethod
    def fromCSV(csv):
        pass

    @staticmethod
    def fromCSVJava(csv):
        pass

    @staticmethod
    def getColumnHeaders(ds):
        pass

    @staticmethod
    def insertColumn(*args):
        pass

    @staticmethod
    def insertRow(*args):
        pass

    @staticmethod
    def setValue(*args):
        pass

    @staticmethod
    def sort(ds, keyColumn, ascending=None, naturalOrdering=None):
        pass

    @staticmethod
    def toCSV(*args, **kwargs):
        pass

    @staticmethod
    def toCSVJava(ds, showHeaders, forExport, localized=False):
        pass

    @staticmethod
    def toCSVJavaStreaming(ds, showHeaders, forExport, sw, localized):
        pass

    @staticmethod
    def toDataSet(*args):
        pass

    @staticmethod
    def toExcel(*args, **kwargs):
        pass

    @staticmethod
    def toJSONObject(data):
        pass

    @staticmethod
    def toPyDataSet(dataset):
        pass

    @staticmethod
    def updateRow(ds, row, changes):
        pass

    class PyDataSet(Dataset):
        _ds = None

        def __init__(self, ds=None):
            # type: (Optional[BasicDataset]) -> None
            self._ds = ds

        def __getitem__(self, item):
            pass

        def __iter__(self):
            pass

        def __len__(self):
            pass

        def getColumnCount(self):
            pass

        def getColumnIndex(self, name):
            pass

        def getColumnName(self, col):
            pass

        def getColumnNames(self):
            pass

        def getColumnType(self, col):
            pass

        def getColumnTypes(self):
            pass

        def getPrimitiveValueAt(self, row, col):
            pass

        def getQualityAt(self, row, col):
            pass

        def getRowCount(self):
            pass

        def getValueAt(self, row, col):
            pass


class SProcCall(Object):
    def _getParams(self):
        pass

    def _getReturnParam(self):
        pass

    def getDatasource(self):
        pass

    def getOutParamValue(self, param):
        print(self, param)
        return 0

    def getProcedureName(self):
        pass

    def getResultSet(self):
        print(self)
        return BasicDataset()

    def getReturnValue(self):
        print(self)
        return 0

    def getTxId(self):
        pass

    def getUpdateCount(self):
        print(self)
        return 1

    def isSkipAudit(self):
        pass

    def registerInParam(self, param, typeCode, value):
        print(self, param, typeCode, value)

    def registerOutParam(self, param, typeCode):
        print(self, param, typeCode)

    def registerReturnParam(self, typeCode):
        print(self, typeCode)

    def setDatasource(self, datasource):
        pass

    def setProcedureName(self, procedureName):
        pass

    def setSkipAudit(self, skipAudit):
        pass

    def setTxId(self, txId):
        pass

    class SProcArg(Object):
        def getParamType(self):
            pass

        def getValue(self):
            pass

        def isInParam(self):
            pass

        def isOutParam(self):
            pass

        def setParamType(self, paramType):
            pass

        def setValue(self, value):
            pass

        def toString(self):
            pass

    class SProcArgKey(Object):
        def getParamIndex(self):
            pass

        def getParamName(self):
            pass

        def hashCode(self):
            pass

        def isNamedParam(self):
            pass

        def toString(self):
            pass


class SystemUtilities(Object):
    @staticmethod
    def logger(loggerName):
        pass

    @staticmethod
    def parseTranslateArguments(*args, **kwargs):
        pass

    class RequestImpl(Object, Request):
        timeout = None  # type: int

        def __init__(self, timeout):
            # type: (int) -> None
            self.timeout = timeout

        def checkTimeout(self):
            pass

        def dispatchFunc(self):
            pass

        def finishExceptionally(self, e):
            pass

        def finishSuccessfully(self, value):
            pass

        def getLongId(self):
            pass

        def cancel(self):
            pass

        def get(self):
            pass

        def getError(self):
            pass

        def onError(self, func):
            pass

        def onSuccess(self, func):
            pass
