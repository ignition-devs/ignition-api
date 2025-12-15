"""Tag Functions.

The following functions give you access to interact with Ignition Tags.
"""

from __future__ import print_function

__all__ = [
    "DEFAULT_TIMEOUT_MILLIS",
    "LEGACY_DEFAULT_TIMEOUT_MILLIS",
    "TAG_PATH",
    "browse",
    "configure",
    "copy",
    "deleteTags",
    "exists",
    "exportTags",
    "getConfiguration",
    "importTags",
    "move",
    "query",
    "readAsync",
    "readBlocking",
    "rename",
    "requestGroupExecution",
    "restartProvider",
    "writeAsync",
    "writeBlocking",
]

from typing import Any, Callable, Dict, List, Optional, Union

from com.inductiveautomation.ignition.common.browsing import Results
from com.inductiveautomation.ignition.common.model.values import (
    BasicQualifiedValue,
    QualityCode,
)

DEFAULT_TIMEOUT_MILLIS = 45000
LEGACY_DEFAULT_TIMEOUT_MILLIS = 45000
TAG_PATH = None  # type: Any


def browse(
    path,  # type: Union[str, unicode]
    filter=None,  # type: Optional[Dict[Union[str, unicode], Any]]
):
    # type: (...) -> Results
    """Returns a list of tags found at the specified Tag path.

    The list objects are returned as dictionaries with some basic
    information about each Tag.

    Args:
        path: The path that will be browsed, typically to a folder or
            UDT instance.
        filter: A dictionary of browse filter keys.

    Returns:
        A Results object which contains a list of Tag dictionaries, one
        for each Tag found during the browse.
    """
    print(path, filter)
    return Results()


def configure(
    basePath,  # type: Union[str, unicode]
    tags,  # type: List[Dict[Union[str, unicode], Any]]
    collisionPolicy="o",  # type: Union[str, unicode]
):
    # type: (...) -> List[QualityCode]
    """Creates Tags from a given list of Python dictionaries or from a
    JSON source string.

    Can be used to overwrite a current Tag's configuration.

    When utilizing this function, the Tag definitions must specify the
    names of properties with their scripting/JSON name.

    Args:
        basePath: The starting point where the new Tags will be created.
            When making changes to existing tags with this function,
            you want to set the path to the parent folder of the
            existing Tag(s), not the Tag(s) themselves.
        tags: A list of Tag definitions, where each Tag definition is a
            Python dictionary. Alternately, a JSON source string may be
            passed to this parameter. When editing existing tags, it is
            generally easier to retrieve the Tag configurations with
            system.Tag.getConfiguration, modify the results of the
            getConfiguration call, and then write the new configuration
            to the parent folder of the existing Tag(s).
        collisionPolicy: The action to take when a Tag or folder with
            the same path and name is encountered. Possible values
            include:

            a - Abort and throw an exception
            o - Overwrite and replace existing Tag's configuration
            i - Ignore that item in the list
            m - Merge, modifying values that are specified in the
                definition, without impacting values that aren't defined
                in the definition. Use this when you want to apply a
                slight change to tags, without having to build a
                complete configuration object.

            Defaults to Overwrite. Optional.

    Returns:
        A List of QualityCode objects, one for each Tag in the list,
        that is representative of the result of the operation.
    """
    print(basePath, tags, collisionPolicy)
    return [QualityCode() for _ in tags]


def copy(
    tags,  # type: List[Union[str, unicode]]
    destination,  # type: Union[str, unicode]
    collisionPolicy="o",  # type: Union[str, unicode]
):
    # type: (...) -> List[QualityCode]
    """Copies tags from one folder to another.

    Multiple Tag and folder paths may be passed to a single call of this
    function. The new destination can be a separate Tag provider.

    Args:
        tags: A List of Tag paths to move.
        destination: The destination to copy the Tags to. All specified
            tags will be copied to the same destination. The destination
            Tag provider must be specified.
        collisionPolicy: The action to take when a Tag or folder with
            the same path and name is encountered. Possible values
            include: "a" Abort and throw an exception, "o" Overwrite and
            replace existing Tag's configuration, "i" Ignore that item
            in the list. Defaults to Overwrite. Optional.

    Returns:
        A List of QualityCode objects, one for each Tag in the list,
        that is representative of the result of the operation.
    """
    print(tags, destination, collisionPolicy)
    return [QualityCode() for _ in tags]


def deleteTags(tagPaths):
    # type: (List[Union[str, unicode]]) -> List[QualityCode]
    """Deletes multiple Tags or Tag Folders.

    When deleting a Tag Folder, all Tags under the folder are also
    deleted.

    Args:
        tagPaths: A List of the paths to the Tags or Tag Folders that
            are to be removed.

    Returns:
         A List of QualityCode objects, one for each Tag in the list,
         that is representative of the result of the operation.
    """
    print(tagPaths)
    return [QualityCode() for _ in tagPaths]


def exists(tagPath):
    # type: (Union[str, unicode]) -> bool
    """Checks whether or not a Tag with a given path exists.

    Args:
        tagPath: The path of the Tag to look up.

    Returns:
        True if a Tag exists for the given path, False otherwise.
    """
    print(tagPath)
    return True


def exportTags(
    filePath=None,  # type: Union[str, unicode, None]
    tagPaths=None,  # type: Optional[List[Union[str, unicode]]]
    recursive=True,  # type: bool
    exportType="json",  # type: Union[str, unicode]
):
    # type: (...) -> Union[str, unicode, None]
    """Exports Tags to a file on a local file system.

    The term "local file system" refers to the scope in which the script
    was running; for example, running this script in a Gateway Timer
    script will export the file to the Gateway file system.

    Args:
        filePath: The file path that the Tags will be exported to. If
            the file does not already exist, this function will attempt
            to create it.
        tagPaths: A List of Tag paths to export. All Tag paths in the
            list must be from the same parent folder.
        recursive: Set to True to export all Tags under each Tag path,
            including Tags in child folders. Defaults to True. Optional.
        exportType: The type of file that will be exported. Set to
            "json" or "xml". Defaults to "json". Optional.

    Returns:
        None or if ``filePath`` is omitted, the tag export as a string.
    """
    print(filePath, tagPaths, recursive, exportType)
    return None if filePath is None else ""


def getConfiguration(
    basePath,  # type: Union[str, unicode]
    recursive=False,  # type: bool
):
    # type: (...) -> List[Dict[Union[str, unicode], Any]]
    """Retrieves Tags from the Gateway as Python dictionaries.

    These can be edited and then saved back using system.tag.configure.

    Args:
        basePath: The starting point where the Tags will be retrieved.
            This can be a folder containing, and if recursive is True,
            then the function will attempt to retrieve all of the tags
            in the folder.
        recursive: If True, the entire Tag Tree under the specified path
            will be retrieved. Note that this will only check one level
            under the base path. True recursion would require multiple
            uses of this function at different paths. Optional.

    Returns:
         A List of Tag dictionaries. Nested Tags are placed in a list
         marked as "tags" in the dictionary.
    """
    return (
        [
            {
                "tags": [
                    {
                        "path": "New Tag",
                        "tagType": "AtomicTag",
                        "name": "New Tag",
                        "valueSource": "memory",
                    }
                ],
                "path": basePath,
                "tagType": "Folder",
                "name": "Test",
            }
        ]
        if recursive
        else [{"path": basePath, "tagType": "Folder", "name": "Test"}]
    )


def importTags(
    filePath,  # type: Union[str, unicode]
    basePath,  # type: Union[str, unicode]
    collisionPolicy="o",  # type: Union[str, unicode]
):
    # type: (...) -> List[QualityCode]
    """Imports a JSON Tag file at the provided path.

    Also supports XML and CSV Tag file exports from legacy systems.

    Args:
        filePath: The file path of the Tag export to import.
        basePath: The Tag path that will serve as the root node for the
            imported Tags.
        collisionPolicy: The action to take when a Tag or folder with
            the same path and name is encountered. Possible values
            include: "a" Abort and throw an exception, "o" Overwrite and
            replace existing Tag's configuration, "i" Ignore that item
            in the list. Defaults to Overwrite. Optional.

    Returns:
        A List of QualityCode objects, one for each Tag in the list,
        that is representative of the result of the operation.
    """
    print(filePath, basePath, collisionPolicy)
    return [QualityCode()]


def move(
    tags,  # type: List[Union[str, unicode]]
    destination,  # type: Union[str, unicode]
    collisionPolicy="o",  # type: Union[str, unicode]
):
    # type: (...) -> List[QualityCode]
    """Moves Tags or Folders to a new destination.

    The new destination can be a separate Tag provider. If interested in
    copying the tags to a new destination, instead of moving them,
    please see the system.tag.copy page.

    Args:
        tags: A List of Tag paths to move.
        destination: The destination to move the Tags to. The
            destination Tag provider must be specified: i.e.,
            ``[default]Folder/myTag``.
        collisionPolicy: The action to take when a Tag or folder with
            the same path and name is encountered. Possible values
            include: "a" Abort and throw an exception, "o" Overwrite and
            replace existing Tag's configuration, "i" Ignore that item
            in the list. Defaults to Overwrite. Optional.

    Returns:
        A List of QualityCode objects, one for each Tag in the list,
        that is representative of the result of the operation.
    """
    print(tags, destination, collisionPolicy)
    return [QualityCode() for _ in tags]


def query(
    provider=None,  # type: Union[str, unicode, None]
    query=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    limit=None,  # type: Optional[int]
    continuation=None,  # type: Union[str, unicode, None]
):
    # type: (...) -> Results
    """Queries a Tag Provider to produce a list of tags that meet the
    specified criteria.

    Args:
        provider: The Tag Provider to query. Optional.
        query: A JSON document that specifies the query conditions.
            Optional.
        limit: Maximum results to return. If more results are possible,
            the result will have a continuation point set. Optional.
        continuation: The Tag ID of a previously returned
            continuation point, to continue the associated query from
            that point. Optional.

    Returns:
        A dataset representing the results of the query.
    """
    print(provider, query, limit, continuation)
    return Results()


def readAsync(tagPaths, callback):
    # type: (List[Union[str, unicode]], Callable[..., Any]) -> None
    """Asynchronously reads the value of the Tags at the given paths.

    You must provide a python callback function that can process the
    read results.

    Args:
        tagPaths: A List of Tag paths to read from. If no property is
            specified in the path, the Value property is assumed.
        callback: A Python callback function to process the read
            results. The function definition must provide a single
            argument, which will hold a List of qualified values when
            the callback function is invoked. The qualified values will
            have three sub members: value, quality, and timestamp.
    """
    print(tagPaths, callback)


def readBlocking(
    tagPaths,  # type: List[Union[str, unicode]]
    timeout=45000,  # type: int
):
    # type: (...) -> List[BasicQualifiedValue]
    """Reads the value of the Tags at the given paths.

    Will block until the read operation is complete or times out.

    Args:
        tagPaths: A List of Tag paths to read from. If no property is
            specified in a path, the Value property is assumed.
        timeout: How long to wait in milliseconds before the read
            operation times out. This parameter is optional, and
            defaults to 45000 milliseconds if not specified. Optional.

    Returns:
        A list of QualifiedValue objects corresponding to the Tag paths.
    """
    print(tagPaths, timeout)
    return [BasicQualifiedValue() for _ in tagPaths]


def rename(
    tag,  # type: Union[str, unicode]
    newName,  # type: Union[str, unicode]
    collisionPollicy="a",  # type: Union[str, unicode]
):
    # type: (...) -> QualityCode
    """Renames a single Tag or folder.

    Args:
        tag: A path to the Tag or folder to rename.
        newName: The new name for the tag or folder.
        collisionPollicy: The action to take when a Tag or folder with
            the same path and names is encountered. Possible values
            include "a" (Abort, throws an exception), "o" (Overwrite,
            completely replaces a Tag's configuration), and "i"
            (Ignore). Defaults to Abort if not specified. Optional.

    Returns:
        A QualityCode object that contains the result of the rename
        operation.
    """
    print(tag, newName, collisionPollicy)
    return QualityCode()


def requestGroupExecution(provider, tagGroup):
    # type: (Union[str, unicode], Union[str, unicode]) -> None
    """Sends a request to the specified Tag Group to execute now.

    Args:
        provider: Name of the Tag Provider that the Tag Group is in.
        tagGroup: The name of the Tag Group to execute.
    """
    print(provider, tagGroup)


def restartProvider(provider):
    # type: (Union[str, unicode]) -> bool
    """Stops and restarts the specified provider.

    Args:
        provider: The name of the Tag Provider to restart.

    Returns:
        True if the provider was successfully restarted, False
        otherwise.
    """
    print(provider)
    return True


def writeAsync(
    tagPaths,  # type: List[Union[str, unicode]]
    values,  # type: List[Any]
    callback=None,  # type: Optional[Callable[..., Any]]
):
    # type: (...) -> None
    """Asynchronously writes values to Tags a the given paths.

    You must provide a Python callback function that can process the
    write results.

    Args:
        tagPaths: A List of Tag paths to write to. If no property is
            specified in a Tag path, the Value property is assumed.
        values: The values to write to the specified paths.
        callback: A Python callback function to process the write
            results. The function definition must provide a single
            argument: a List of QualityCode objects corresponding to the
            results of the write operation. Optional.
    """
    print(tagPaths, values, callback)


def writeBlocking(
    tagPaths,  # type: List[Union[str, unicode]]
    values,  # type: List[Any]
    timeout=45000,  # type: int
):
    # type: (...) -> List[QualityCode]
    """Writes values to Tags at the given paths.

    This function will block until the write operation is complete or
    times out.

    Args:
        tagPaths: A List of Tag paths to write to. If no property is
            specified in a Tag path, the Value property is assumed.
        values: The values to write to the specified paths.
        timeout: How long to wait in milliseconds before the write
            operation times out. This parameter is optional, and
            defaults to 45,000 milliseconds if not specified. Optional.

    Returns:
        A List of QualityCode objects, one for each Tag path.
    """
    print(tagPaths, values, timeout)
    return [QualityCode() for _ in tagPaths]
