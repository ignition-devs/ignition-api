"""Tag Functions.

The following functions give you access to interact with Ignition Tags.
"""

from __future__ import print_function

__all__ = [
    "addTag",
    "browseConfiguration",
    "browseHistoricalTags",
    "browseTags",
    "browseTagsSimple",
    "editAlarmConfig",
    "editTag",
    "editTags",
    "exists",
    "getAlarmStates",
    "isOverlaysEnabled",
    "loadFromFile",
    "queryTagCalculations",
    "queryTagDensity",
    "queryTagHistory",
    "read",
    "readAll",
    "removeTag",
    "removeTags",
    "scan",
    "setOverlaysEnabled",
    "storeTagHistory",
    "write",
    "writeAll",
    "writeAllSynchronous",
    "writeSynchronous",
]

from typing import Any, Dict, List, Optional

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.browsing import BrowseResults
from com.inductiveautomation.ignition.common.model.values import BasicQualifiedValue
from com.inductiveautomation.ignition.common.script.builtin.ialabs import (
    BrowseTag,
    TagAlarmDefinition,
    TagAlarmProperty,
)
from com.inductiveautomation.ignition.common.sqltags.model.types import (
    DataType,
    TagType,
)
from com.inductiveautomation.ignition.common.tags.config import TagConfiguration
from java.lang import Object, String
from java.util import Date


def addTag(
    parentPath,  # type: String
    name,  # type: String
    tagType,  # type: String
    dataType,  # type: String
    accessRights,  # type: String
    enabled,  # type: bool
    value,  # type: Any
    attributes,  # type: Dict[String, Any]
    parameters,  # type: Dict[String, Any]
    overrides,  # type: Dict[String, Any]
    alarmList,  # type: String
    alarmConfig,  # type: Dict[String, Any]
):
    # type: (...) -> None
    """Adds a new tag in Ignition.

    You can add OPC, memory, expression, query, folder, and UDT instance
    tags. You can't add Client Tags, because those can vary from project
    to project.

    Args:
        parentPath: The folder to add the tag to. Leave blank for the
            root folder.
        name: The name of the tag.
        tagType: The type of tag to create. Possible values are OPC,
            MEMORY, EXPRESSION, QUERY, Folder, and UDT_INST.
        dataType: The data type of the tag. Not used for UDT instances
            or folders. Possible basic values are Int1, Int2, Int4,
            Int8, Float4, Float8, Boolean, String, DataSet, and
            DateTime. Possible array values are Int4Array, Int8Array,
            Float8Array, BooleanArray, StringArray, DateTimeArray.
        accessRights: The access rights for a tag. Possible values are
            Read_Only, Read_Write, and Custom.
        enabled: If True, the tag will be enabled.
        value: The value of the tag. Used for memory tags.
        attributes: The tag's configuration attributes.
        parameters: The parameters for a UDT instance tag.
        overrides: All of the overrides for a UDT instance tag.
        alarmList: List of legacy alarms for the tag. The legacy alarm
            system was retired in 7.6.0, so the alarmConfig parameter
            should be utilized on newer versions.
        alarmConfig: The alarm configuration for the tag. See
            editAlarmConfig for details on how to use this parameter.
    """
    print(
        parentPath,
        name,
        tagType,
        dataType,
        accessRights,
        enabled,
        value,
        attributes,
        parameters,
        overrides,
        alarmList,
        alarmConfig,
    )


def browseConfiguration(path, recursive):
    # type: (String, bool) -> List[TagConfiguration]
    """Browses a folder path or UDT and returns Tag configuration
    information for each Tag within the specified path.

    This can be used to view event scripts, alarms, as well as any other
    configurable attribute on a Tag.

    Args:
        path: The path that will be browsed, typically to a folder or
            UDT instance. Leave blank to browse the root folder. A Tag
            Provider may be specified as follows: "[TagProvider]". If
            the Tag Provider is omitted, client scoped calls will be
            made against the project's default provider. Gateway scoped
            calls must include a Tag Provider. When browsing UDTs,
            specifying the UDT path will browse the Tags inside the UDT.
            To browse the UDT instance, specify the parent of the
            instance.
        recursive: If True, will recursively search for Tags in folders.
            Each folder will return a 'tags' property containing the
            nested TagConfigurations in another list.

    Returns:
        A list of TagConfiguration objects. Attributes on the object may
        be read by calling tag.get(propertyObject). A list of attributes
        with configuration information can be obtained by calling
        getProperties(). Only attributes with non-default values will
        appear in the attribute list.
    """
    print(path, recursive)
    return [TagConfiguration()]


def browseHistoricalTags(
    path,  # type: String
    nameFilters=None,  # type: Optional[List[String]]
    maxSize=None,  # type: Optional[int]
    continuationPoint=None,  # type: Optional[Any]
):
    # type: (...) -> BrowseResults
    """Will browse for any historical Tags at the provided historical
    path.

    It will only browse for Tags at the path, and will not go down
    through any children. Will return with a BrowseResults object.

    Args:
        path: The Historical Tag Path to browse. See the Tag Export page
            for a description of how to construct a historical Tag Path.
        nameFilters: A list of name filters to be applied to the result
            set. Optional.
        maxSize: The maximum size of the result set. Optional.
        continuationPoint: Sets the continuation point in order to
            continue a browse that was previously started and then
            limited. Use .getContinuationPoint() on the BrowseResults
            object to get the continuation point. Optional.

    Returns:
        An object that contains the results as well as the Continuation
        Point. Get the results by calling .getResults() on the
        BrowseResults object.
    """
    print(path, nameFilters, maxSize, continuationPoint)
    return BrowseResults()


def browseTags(
    parentPath,  # type: String
    tagPath=None,  # type: Optional[String]
    tagType=None,  # type: Optional[String]
    dataType=None,  # type: Optional[String]
    udtParentType=None,  # type: Optional[String]
    recursive=False,  # type: Optional[bool]
    sort="ASC",  # type: Optional[String]
):
    # type: (...) -> List[BrowseTag]
    """Returns an array of tags from a specific folder.

    The function supports filtering and recursion. Leave filters blank
    to return all tags.

    If called in the gateway scope, a Tag Provider must be specified.

    Args:
        parentPath: The parent folder path. Leave blank for the root
            folder. Note: you can specify the tag provider name in
            square brackets at the beginning of the parentPath string.
            Example: "[myTagProvider]MyTagsFolder". If the tag provider
            name is left off then the project default provider will be
            used.
        tagPath: Filters on a tag path. Use * as a wildcard for any
            number of characters and a ? for a single character.
            Optional.
        tagType: Filters on a tag type. Possible values are OPC, MEMORY,
            DB, QUERY, Folder, DERIVED and UDT_INST. Optional.
        dataType: The data type of the tag. Not used for UDT instances
            or folders. Possible values are Int1, Int2, Int4, Int8,
            Float4, Float8, Boolean, String, and DateTime. Optional.
        udtParentType: The name of the parent UDT. Optional.
        recursive: Recursively search for tags inside of folders. Note:
            It is highly recommended that recursive is set to False, as
            server timeouts are more likely to occur. Optional.
        sort: Sets the sort order, possible values are ASC and DESC.
            Sorting is done on the full path of the tag. Optional.

    Returns:
        An array of BrowseTag. BrowseTag has the following variables:
        name, path, fullPath, type, dataType, and the following
        functions: isFolder(), isUDT(), isOPC(), isMemory(),
        isExpression(), isQuery().
    """
    print(
        parentPath,
        tagPath,
        tagType,
        dataType,
        udtParentType,
        recursive,
        sort,
    )
    return [BrowseTag("name", "path", "fullpath", TagType(), "valueSource", DataType())]


def browseTagsSimple(
    parentPath,  # type: String
    sort,  # type: String
):
    # type: (...) -> List[BrowseTag]
    """Returns a sorted array of tags from a specific folder.

    Args:
        parentPath: The parent folder path. Leave blank for the root
            folder. Note: you can specify the tag provider name in
            square brackets at the beginning of the parentPath string.
            Example: "[myTagProvider]MyTagsFolder". If the tag provider
            name is left off then the project default provider will be
            used.
        sort: Sets the sort order, possible values are ASC and DESC.

    Returns:
        An array of BrowseTag. BrowseTag has the following variables:
        name, path, fullPath, type, dataType, and the following
        functions: isFolder(), isUDT(), isOPC(), isMemory(),
        isExpression(), isQuery().
    """
    print(parentPath, sort)
    return [BrowseTag("name", "path", "fullpath", TagType(), "valueSource", DataType())]


def editAlarmConfig(
    tagPaths,  # type: List[String]
    alarmConfig,  # type: Dict[String, List[List[String]]]
):
    # type: (...) -> None
    """Edit the alarm configuration of multiple existing tags in
    Ignition with a single call.

    Args:
        tagPaths: The full path to the tag you want to edit. Note: you
            can specify the tag provider name in square brackets at the
            beginning of the parentPath string. Example:
            "[myTagProvider]MyTagsFolder". If the tag provider name is
            left off then the project default provider will be used.
        alarmConfig: A dictionary of multi-dimensional lists containing
            the new alarm configuration. The key in the dictionary will
            be the name of the alarm being to edit, and the value is a
            list of lists. The nested lists use the format ["name",
            "Value", "newValue"]. Note that item 1 is always "Value".
    """
    print(tagPaths, alarmConfig)


def editTag(
    tagPath,  # type: String
    attributes=None,  # type: Optional[Dict[String, Any]]
    parameters=None,  # type: Optional[Dict[String, Any]]
    accessRights=None,  # type: Optional[String]
    overrides=None,  # type: Optional[Dict[String, Any]]
    alarmList=None,  # type: Optional[String]
    alarmConfig=None,  # type: Optional[Dict[String, Any]]
):
    # type: (...) -> None
    """Edits an existing Tag in Ignition.

    This will not work on Client Tags, because there is a Client
    Provider for each project.

    Args:
        tagPath: The full path to the Tag you want to edit. For members
            of UDT instances, the tagPath will be the path to the UDT
            instance, with the overrides parameter listing out the
            member Tags to edit. Note: you can specify the Tag provider
            name in square brackets at the beginning of the parentPath
            string. Example: "[myTagProvider]MyTagsFolder". If the Tag
            provider name is left off then the project default provider
            will be used.
        attributes: The Tag's configuration attributes. Optional.
        parameters: The parameters for a UDT instance Tag. Optional.
        accessRights: The access rights for the Tags. Possible s are
            Read_Only, Read_Write, and Custom. Optional.
        overrides: All of the overrides for a UDT instance Tag. The
            dictionary should be in the form of the names of member Tags
            as keys, with the values being a dictionary of
            properties/overrides ie. {'memberTagName':{dictionary of
            overrides}}. Optional.
        alarmList: List of legacy alarms for the Tag. The legacy alarm
            system was retired in 7.6.0. Newer systems should utilize
            the system.tag.editAlarmConfig function instead. Optional.
        alarmConfig: The alarm configuration for the Tag. Note that this
            parameter cannot edit alarms on UDTs. Instead, the
            system.tag.editAlarmConfig function (which can also edit
            alarms on non-UDT Tags) should be used instead. See
            editAlarmConfig for details on how to use this parameter.
            Optional.
    """
    print(
        tagPath,
        attributes,
        parameters,
        accessRights,
        overrides,
        alarmList,
        alarmConfig,
    )


def editTags(
    tagPaths,  # type: List[String]
    attributes,  # type: Dict[String, Any]
    parameters,  # type: Dict[String, Any]
    accessRights,  # type: String
    overrides,  # type: Dict[String, Any]
    alarmList,  # type: String
    alarmConfig,  # type: Dict[String, Any]
    provider="",  # type: Optional[String]
    json=None,  # type: Optional[String]
):
    # type: (...) -> None
    """Edit multiple existing Tags in Ignition with a single call.

    This will not work on Client Tags, because there is a Client
    Provider for each project.

    Args:
        tagPaths: The full path to the Tag you want to edit. For members
            of UDT instances, the tagPath will be the path to the UDT
            instance, with the overrides parameter listing out the
            member Tags to edit. Note: you can specify the Tag provider
            name in square brackets at the beginning of the parentPath
            string. Example: "[myTagProvider]MyTagsFolder". If the Tag
            provider name is left off then the project default provider
            will be used.
        attributes: The Tag's configuration attributes.
        parameters: The parameters for a UDT instance Tag.
        accessRights: The access rights for a Tag. Possible values are
            Read_Only, Read_Write, and Custom.
        overrides: All of the overrides for a UDT instance Tag.
        alarmList: List of legacy alarms for the Tag. The legacy alarm
            system was retired in 7.6.0, so the alarmConfig parameter
            should be utilized on newer versions.
        alarmConfig: The alarm configuration for the Tag.
        provider: The name of the Tag provider, used in conjunction with
            the JSON argument. The default value is the default Tag
            provider. Optional.
        json: The properties to edit on Tags, represented as a JSON
            object. When using this, it acts as a replacement for other
            parameters. Optional.
    """
    print(
        tagPaths,
        attributes,
        parameters,
        accessRights,
        overrides,
        alarmList,
        alarmConfig,
        provider,
        json,
    )


def exists(tagPath):
    # type: (String) -> bool
    """Checks whether or not a tag with a given path exists.

    Args:
        tagPath: The path of the tag to look up.

    Returns:
        True if a tag exists for the given path, False otherwise.
    """
    print(tagPath)
    return True


def getAlarmStates(tagPath):
    # type: (String) -> List[TagAlarmDefinition]
    """Returns an array of alarm definitions for a specific tag.

    Args:
        tagPath: The full path to the tag. Note: you can specify the tag
            provider name in square brackets at the beginning of the
            parentPath string. Example: "[myTagProvider]MyTagsFolder".
            If the tag provider name is left off then the project
            default provider will be used.

    Returns:
        An array of TagAlarmDefinition.
    """
    print(tagPath)
    return [
        TagAlarmDefinition("alarm", [TagAlarmProperty("property", "type", Object())])
    ]


def isOverlaysEnabled():
    # type: () -> bool
    """Returns whether or not the current client's quality overlay
    system is currently enabled.

    Returns:
         True (1) if overlays are currently enabled.
    """
    return False


def loadFromFile(filePath, provider, mode):
    # type: (String, String, int) -> None
    """This function locates an exported tag file and loads the tags
    into the specified tag provider.

    Args:
        filePath: The path of the tag file to import from.
        provider: The name of the provider to import to.
        mode: Dictates what happens if the tag already exists.
            0 = overwrite, 1 = ignore.
    """
    print(filePath, provider, mode)


def queryTagCalculations(
    paths,  # type: List[String]
    calculations,  # type: List[String]
    startDate=None,  # type: Optional[Date]
    endDate=None,  # type: Optional[Date]
    rangeHours=None,  # type: Optional[int]
    rangeMinutes=None,  # type: Optional[int]
    aliases=None,  # type: Optional[List[String]]
    includeBoundingValues=True,  # type: Optional[bool]
    validatesSCExec=True,  # type: Optional[bool]
    noInterpolation=False,  # type: Optional[bool]
    ignoreBadQuality=False,  # type: Optional[bool]
):
    # type: (...) -> BasicDataset
    """Queries various calculations (aggregations) for a set of tags
    over a specified range.

    Returns a dataset with a row per tag, and a column per calculation.

    This is useful when you wish to aggregate tag history collected over
    a period of time into a single value per aggregate. If you want
    multiple values aggregated to a single time slice (i.e., hourly
    aggregates for the same tag over an 8 hour period) consider using
    system.tag.queryTagHistory

    Args:
        paths: An array of tag paths (strings) to query calculations
            for. The resulting dataset will have a row for each tag, and
            a column for each calculation.
        calculations: An array of calculations (aggregation functions)
            to execute for each tag. Valid values are: "Average"
            (time-weighted), "MinMax", "LastValue", "SimpleAverage",
            "Sum", "Minimum", "Maximum", "DurationOn", "DurationOff",
            "CountOn", "CountOff", "Count", "Range", "Variance",
            "StdDev", "PctGood", and "PctBad".
        startDate: The starting point for the calculation window. If
            omitted, and range is not used, 8 hours before the current
            time is used. Optional.
        endDate: The end of the calculation window. If omitted, and
            range is not used, uses the current time. Optional.
        rangeHours: Allows you to specify the query range in hours,
            instead of using start and end date. Can be positive or
            negative, and can be used in conjunction with startDate or
            endDate. Optional.
        rangeMinutes: Same as rangeHours, but in minutes. Optional.
        aliases: Aliases that will be used to override the tag path
            names in the result dataset. Must be 1-to-1 with the tag
            paths. If not specified, the tag paths themselves will be
            used. Optional.
        includeBoundingValues: A boolean flag indicating that the system
            should attempt to load values before and after the query
            bounds for the purpose of interpolation. The effect depends
            on the aggregates used. The default is "True". Optional.
        validatesSCExec: A boolean flag indicating whether or not data
            should be validated against the scan class execution
            records. If False, calculations may include data that is
            assumed to be good, even though the system may not have been
            running. Default is "True". Optional.
        noInterpolation: A boolean flag indicating that the system
            should not attempt to interpolate values in situations where
            it normally would, such as for analog tags. Default is
            "False". Optional.
        ignoreBadQuality: A boolean flag indicating that bad quality
            values should not be used in the query process. If set, any
            value with a "bad" quality will be completely ignored in
            calculations. Default is "False". Optional.

    Returns:
        A dataset representing the calculations over the specified
        range.
    """
    print(
        paths,
        calculations,
        startDate,
        endDate,
        rangeHours,
        rangeMinutes,
        aliases,
        includeBoundingValues,
        validatesSCExec,
        noInterpolation,
        ignoreBadQuality,
    )
    return BasicDataset()


def queryTagDensity(paths, startDate, endDate):
    # type: (List[String], Date, Date) -> BasicDataset
    """Queries the Tag history system for information about the density
    of data.

    In other words, how much data is available for a given time
    span.

    This function is called with a list of Tag paths, and a start and
    end date. The result set is a two column dataset specifying the
    timestamp, and a relative weight. Each row is valid from the given
    time until the next row. Tags are assigned a 1 or a 0 if they are
    present or not. All values are then multiplied together to get a
    decimal based percentage for the density. Thus, for four Tag paths
    passed in, if three Tags were present during the span, the result
    would be 0.75.

    Args:
        paths: An array of Tag paths (strings) to query.
        startDate: The start of the range to query.
        endDate: The end of the range to query.

    Returns:
        A 2-column dataset consisting of a timestamp and a weight. Each
        row is valid until the next row.
    """
    print(paths, startDate, endDate)
    return BasicDataset()


def queryTagHistory(
    paths,  # type: List[String]
    startDate=None,  # type: Optional[Date]
    endDate=None,  # type: Optional[Date]
    returnSize=-1,  # type: Optional[int]
    aggregationMode="Average",  # type: Optional[String]
    returnFormat="Wide",  # type: Optional[String]
    columnNames=None,  # type: Optional[List[String]]
    intervalHours=None,  # type: Optional[int]
    intervalMinutes=None,  # type: Optional[int]
    rangeHours=None,  # type: Optional[int]
    rangeMinutes=None,  # type: Optional[int]
    aggregationModes=None,  # type: Optional[List[String]]
    includeBoundingValues=None,  # type: Optional[bool]
    validateSCExec=None,  # type: Optional[bool]
    noInterpolation=None,  # type: Optional[bool]
    ignoreBadQuality=None,  # type: Optional[bool]
    timeout=None,  # type: Optional[int]
):
    # type: (...) -> BasicDataset
    """Issues a query to the Tag Historian.

    Querying tag history involves specifying the tags and the date
    range, as well as a few optional parameters. The Tag historian will
    find the relevant history and then interpolate and aggregate it
    together into a coherent, tabular result set.

    Args:
        paths: An array of tag paths (strings) to query. Each tag path
            specified will be a column in the result dataset.
        startDate: The earliest value to retrieve. If omitted, 8 hours
            before current time is used. Optional.
        endDate: The latest value to retrieve. If omitted, current time
            is used. Optional.
        returnSize: The number of samples to return. -1 will return
            values as they changed, and 0 will return the "natural"
            number of values based on the logging rates of the scan
            class(es) involved. -1 is the default. Optional.
        aggregationMode: The mode to use when aggregating multiple
            samples into one time slice. Valid values are: "Average"
            (time-weighted), "MinMax", "LastValue", "SimpleAverage",
            "Sum", "Minimum", "Maximum", "DurationOn", "DurationOff",
            "CountOn", "CountOff", "Count", "Range", "Variance",
            "StdDev", "PctGood", and "PctBad". Optional.
        returnFormat: Use "Wide" to have a column per tag queried, or
            "Tall" to have a fixed-column format. Default is "Wide".
            Optional.
        columnNames: Aliases that will be used to override the column
            names in the result dataset. Must be 1-to-1 with the tag
            paths. If not specified, the tag paths themselves will be
            used as column titles. Optional.
        intervalHours: Allows you to specify the window interval in
            terms of hours, as opposed to using a specific return size.
            Optional.
        intervalMinutes: Same as intervalHours, but in minutes. Can be
            used on its own, or in conjunction with intervalHours.
            Optional.
        rangeHours: Allows you to specify the query range in hours,
            instead of using start and end date. Can be positive or
            negative, and can be used in conjunction with startDate or
            endDate. Optional.
        rangeMinutes: Same as rangeHours, but in minutes. Optional.
        aggregationModes: A one-to-one list with paths specifying an
            aggregation mode per column. Optional.
        includeBoundingValues: A boolean flag indicating that the system
            should attempt to include values for the query bound times
            if possible. The default for this property depends on the
            query mode, so unless a specific behavior is desired, it is
            best to not include this parameter. Optional.
        validateSCExec: A boolean flag indicating whether or not data
            should be validated against the scan class execution
            records. If False, data will appear flat (but good quality)
            for periods of time in which the system wasn't running. If
            True, the same data would be bad quality during downtime
            periods. Optional.
        noInterpolation: A boolean flag indicating that the system
            should not attempt to interpolate values in situations where
            it normally would. This will also prevent the return of rows
            that are purely interpolated. Optional.
        ignoreBadQuality: A boolean flag indicating that bad quality
            values should not be used in the query process. If set, any
            value with a "bad" quality will be completely ignored in
            calculations and in the result set. Optional.
        timeout: Timeout in milliseconds for Client Scope. This property
            is ignored in the Gateway Scope. Optional.

    Returns:
        A dataset representing the historian values for the specified
        tag paths. The first column will be the timestamp, and each
        column after that represents a tag.
    """
    print(
        paths,
        startDate,
        endDate,
        returnSize,
        aggregationMode,
        returnFormat,
        columnNames,
        intervalHours,
        intervalMinutes,
        rangeHours,
        rangeMinutes,
        aggregationModes,
        includeBoundingValues,
        validateSCExec,
        noInterpolation,
        ignoreBadQuality,
        timeout,
    )
    return BasicDataset()


def read(tagPath):
    # type: (String) -> BasicQualifiedValue
    """Reads the value of the tag at the given tag path.

    Returns a qualified value object. You can read the value, quality,
    and timestamp from this object. If the tag path does not specify a
    tag property, then the Value property is assumed.

    You can also read the value of tag attributes by appending the
    attribute to the tagPath parameter. See the Tag Attributes page for
    a list of available attributes.

    Args:
        tagPath: Reads from the given tag path. If no property is
            specified in the path, the Value property is assumed.

    Returns:
        A qualified value. This object has three sub-members: value,
        quality, and timestamp.
    """
    print(tagPath)
    return BasicQualifiedValue()


def readAll(tagPaths):
    # type: (List[String]) -> List[BasicQualifiedValue]
    """Reads the values of each tag in the tag path list.

    Returns a sequence of qualified value objects. You can read the
    value, quality, and timestamp from each object in the return
    sequence. Reading in bulk like this is more efficient than calling
    read() many times.

    Args:
        tagPaths: A sequence of tag paths to read from.

    Returns:
        A sequence of qualified values corresponding to each tag path
        given. Each qualified value will have three sub-members: value,
        quality, and timestamp.
    """
    print(tagPaths)
    return [BasicQualifiedValue() for _ in range(len(tagPaths))]


def removeTag(tagPath):
    # type: (String) -> None
    """Removes a tag from Ignition.

    Args:
        tagPath: The path to the tag you want to remove. You can specify
            the tag provider name in square brackets at the beginning of
            the parentPath string. Example:
            "[myTagProvider]MyTagsFolder". If the tag provider name is
            left off, then the project default provider will be used.
            Note that an empty path ('') will remove all tags.
    """
    print(tagPath)


def removeTags(tagPaths):
    # type: (List[String]) -> None
    """Removes multiple tags from Ignition with a single call.

    Args:
        tagPaths: An array of the paths to the tags you want to remove.
            You can specify the tag provider name in square brackets at
            the beginning of the parentPath string. Example:
            "[myTagProvider]MyTagsFolder". If the tag provider name is
            left off, then the project default provider will be used.
            Note that an empty path (['']) will remove all tags.
    """
    print(tagPaths)


def scan(provider, scname):
    # type: (String, String) -> None
    """Forces execution of a scan class.

    On a leased scan class, if both the fast and slow rate are set to 0,
    this will not execute.

    Args:
        provider: The name of the scan class provider. If blank, it will
            use the default. Required if used in the gateway scope.
        scname: The name of the scan class to execute.
    """
    print(provider, scname)


def setOverlaysEnabled(enabled):
    # type: (bool) -> None
    """Enables or disables the component quality overlay system.

    Args:
        enabled: True (1) to turn on tag overlays, False (0) to turn
            them off.
    """
    print(enabled)


def storeTagHistory(
    historyprovider,  # type: String
    tagprovider,  # type: String
    paths,  # type: List[String]
    values,  # type: List[Any]
    qualities=None,  # type: Optional[List[int]]
    timestamps=None,  # type: Optional[List[Date]]
):
    # type: (...) -> None
    """Inserts data into the tag history system, allowing Tag history to
    be recorded via scripting.

    The Tag paths are associated with a historical and realtime
    provider, but they do not necessarily need to exist in the realtime
    provider. This means records from non-existent (virtual) Tags can be
    stored in the Tag History system. Because of this, it is imperative
    that Tag paths passed to the function are typed precisely, otherwise
    the history will be stored at an incorrect path.

    Note that the Tag History system does cache tag data. Thus, if this
    function is called, the tag path and tag id are cached until the
    history provider or gateway are restarted. This means manually
    removing the tag from the sqlth_te table, and then calling this
    function again with the same path will not re-populate the tag
    execution table (especially so when working purely with virtual tag
    paths). Instead, the cache must first be cleared, and then a new
    entry will be added the next time this function is called.

    Args:
        historyprovider: The historical provider to store to.
        tagprovider: The name of the realtime tag provider to associate
            these tags with. The tag provider does not need to exist,
            and the tag paths do not need to exist in it.
        paths: A list of paths to store. The values, qualities, and
            timestamps are one-to-one with the paths. A single path may
            be present multiple times in order to store multiple values.
        values: A list of values to store.
        qualities: A list of integer quality codes corresponding to the
            values. Quality codes can be found on the Tag Quality and
            Overlays page. If omitted, GOOD quality will be used.
            Optional.
        timestamps: A list of Date timestamps corresponding to the
            values. If omitted, the current time will be used. A
            java.util.date object may be passed, so the system.date
            functions can be used to return a timestamp. Optional.
    """
    print(historyprovider, tagprovider, paths, values, qualities, timestamps)


def write(tagPath, value, suppressErrors=False):
    # type: (String, Any, Optional[bool]) -> int
    """Writes a value to a tag.

    Note that this function writes asynchronously. This means that the
    function does not wait for the write to occur before returning - the
    write occurs sometime later on a different thread.

    Args:
        tagPath: The path of the tag to write to.
        value: The value to write.
        suppressErrors: A flag indicating whether or not to suppress
            errors. Optional.

    Returns:
        0 if the write failed immediately, 1 if it succeeded
        immediately, and 2 if it is pending.
    """
    print(tagPath, value, suppressErrors)
    return 1


def writeAll(tagPaths, values):
    # type: (List[String], List[Any]) -> List[int]
    """Performs an asynchronous bulk write.

    Takes two sequences that must have the same number of entries. The
    first is the list of tag paths to write to, and the second is a list
    of values to write. This function is dramatically more efficient
    than calling write multiple times.

    Args:
        tagPaths: The paths of the tags to write to.
        values: The values to write.

    Returns:
        Array of ints with an element for each tag written to: 0 if the
        write failed immediately, 1 if it succeeded immediately, and 2
        if it is pending.
    """
    print(tagPaths, values)
    return [1] * len(tagPaths)


def writeAllSynchronous(
    tagPaths,  # type: List[String]
    values,  # type: List[Any]
    timeout=45000,  # type: Optional[int]
):
    # type: (...) -> None
    """Performs a synchronous write to multiple tags.

    Synchronous means that execution will not continue until this
    function has completed, so you will know that a write has been
    attempted on the provided tags. The first write to fail or time out
    will throw an exception, but any subsequent tags in the provided
    list will still be attempted. This function cannot be called from
    the event dispatch thread, meaning it cannot be called directly from
    a GUI event like a button press without creating a new thread with a
    call to system.util.invokeAsynchronous. You can call this from
    project event scripts like timer scripts.

    Note that the order of the tags listed in the tagPaths parameter
    determines the order that the writes will occur.

    Args:
        tagPaths: The paths of the tags to write to.
        values: The values to write.
        timeout: How long to wait in milliseconds before timing out
            pending writes. The default is 45000 milliseconds. Optional.
    """
    print(tagPaths, values, timeout)


def writeSynchronous(tagPath, value, timeout=45000):
    # type: (String, Any, Optional[int]) -> None
    """Performs a write to a tag, synchronously.

    This means that you know at the end of this function whether or not
    the write succeeded or not. A write that fails or times out will
    throw an error. However, this function cannot be called from the
    event dispatch thread, which means that it cannot be called directly
    from a GUI event like a button press, without wrapping it in a
    system.util.invokeAsynchronous. You can call this from project event
    scripts like timer scripts.

    Args:
        tagPath: The path of the tag to write to.
        value: The value to write.
        timeout: How long to wait in milliseconds before timing out
            pending writes. The default is 45000 milliseconds. Optional.
    """
    print(tagPath, value, timeout)
