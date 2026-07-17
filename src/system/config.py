"""Config Functions.

The following functions allow you to configure various aspects of your
Gateway configuration.
"""

from __future__ import print_function

__all__ = [
    "copy",
    "create",
    "delete",
    "getActiveMode",
    "getModes",
    "getResource",
    "getResourceTypes",
    "getResources",
    "move",
    "rename",
    "replace",
]

from typing import Any, Dict, List, Optional, Union

from com.inductiveautomation.ignition.gateway.script import PyResource


def copy(
    moduleId,  # type: Union[str, unicode]
    typeId,  # type: Union[str, unicode]
    name=None,  # type: Union[str, unicode, None]
    collection=None,  # type: Union[str, unicode, None]
    newName=None,  # type: Union[str, unicode, None]
    newCollection=None,  # type: Union[str, unicode, None]
    signature=None,  # type: Union[str, unicode, None]
    actor=None,  # type: Union[str, unicode, None]
):
    # type: (...) -> PyResource
    """Copies a resource to a new name and/or collection.

    When using this function, either the newName or newCollection
    parameter must be defined.

    Args:
        moduleId: The module ID portion of the resource type identifier.
        typeId: The type ID portion of the resource type identifier.
        name: The name of the resource. Required for named resources,
            but must be omitted for singleton resources. Optional.
        collection: The collection containing the resource. If omitted,
            uses the active definition. Optional.
        newName: The new name for the copied resource. Required if not
            changing collection for named resource types. Optional.
        newCollection: The new collection for the copied resource.
            Required if not changing name for singleton resource types.
            Optional.
        signature: The hex-encoded signature of the resource. Optional.
        actor: A string identifying the actor performing the operation.
            If not specified, an identifier will be automatically
            generated. Optional.

    Returns:
        A PyResource containing the specified parameter attributes of an
        existing Gateway resource, which can also be read as plain
        Python properties.
    """
    print(moduleId, typeId, name, collection, newName, newCollection, signature, actor)
    return PyResource()


def create(
    moduleId,  # type: Union[str, unicode]
    typeId,  # type: Union[str, unicode]
    name=None,  # type: Union[str, unicode, None]
    collection=None,  # type: Union[str, unicode, None]
    config=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    backupConfig=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    files=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    description=None,  # type: Union[str, unicode, None]
    enabled=None,  # type: Optional[bool]
    attributes=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    actor=None,  # type: Union[str, unicode, None]
):
    # type: (...) -> PyResource
    """Creates a new resource of the specified type.

    Args:
        moduleId: The module ID portion of the resource type identifier.
        typeId: The type ID portion of the resource type identifier.
        name: The name of the resource. Required for named resources,
            but must be omitted for singleton resources. Optional.
        collection: The collection containing the resource. If omitted,
            uses the active definition. Optional.
        config: A dictionary representing the resource configuration,
            matching the resource type's JSON schema. If not provided,
            the files argument must be provided. Optional.
        backupConfig: A dictionary representing the backup configuration
            for resources that support backup data. Optional.
        files: A dictionary of additional files to include with the
            resource. Keys are filenames, values can be byte arrays,
            strings, lists, or dictionaries. If not provided, the config
            argument must be provided. Optional.
        description: A description for the resource. Optional.
        enabled: Whether the resource should be enabled. If omitted, the
            resource will be enabled when created. Optional.
        attributes: A dictionary of resource attributes to set.
            Optional.
        actor: A string identifying the actor performing the operation.
            If not specified, an identifier will be automatically
            generated. Optional.

    Returns:
        A PyResource containing the specified parameter attributes of
        your newly created Gateway resource, which can also be read as
        plain Python properties.
    """
    print(
        moduleId,
        typeId,
        name,
        collection,
        config,
        backupConfig,
        files,
        description,
        enabled,
        attributes,
        actor,
    )
    return PyResource()


def delete(
    moduleId,  # type: Union[str, unicode]
    typeId,  # type: Union[str, unicode]
    name=None,  # type: Union[str, unicode, None]
    collection=None,  # type: Union[str, unicode, None]
    signature=None,  # type: Union[str, unicode, None]
    force=False,  # type: bool
    actor=None,  # type: Union[str, unicode, None]
):
    # type: (...) -> None
    """Deletes a resource from the Gateway.

    Args:
        moduleId: The module ID portion of the resource type identifier.
        typeId: The type ID portion of the resource type identifier.
        name: The name of the resource. Required for named resources,
            but must be omitted for singleton resources. Optional.
        collection: The collection containing the resource. If omitted,
            uses the active definition. Optional.
        signature: The hex-encoded signature of the resource. Optional.
        force: f true, deletes the resource even if other resources
            reference it. If omitted, default is false. Optional.
        actor: A string identifying the actor performing the operation.
            If not specified, an identifier will be automatically
            generated. Optional.
    """
    print(moduleId, typeId, name, collection, signature, force, actor)


def getActiveMode():
    # type: () -> Union[str, unicode, None]
    """Returns the current deployment mode, or None if no mode is
    explicitly active.

    Returns:
        The current deployment mode, as a string.
    """
    return None


def getModes():
    # type: () -> List[Union[str, unicode]]
    """Returns a list of all available deployment modes.

    Returns:
        A list of strings, containing all the available deployment modes
        on the Gateway.
    """
    return []


def getResource(
    moduleId,  # type: Union[str, unicode]
    typeId,  # type: Union[str, unicode]
    name,  # type: Union[str, unicode]
    collection,  # type: Union[str, unicode]
):
    # type: (...) -> PyResource
    """Returns a resource from the Gateway.

    Args:
        moduleId: The module ID portion of the resource type identifier.
        typeId: The type ID portion of the resource type identifier.
        name: The name of the resource. Required for named resources,
            but must be omitted for singleton resources.
        collection: The collection containing the resource. If omitted,
            uses the active definition.

    Returns:
        The specified Gateway resource, as a PyResource that can be read
        as plain Python properties.
    """
    print(moduleId, typeId, name, collection)
    return PyResource()


def getResources(
    moduleId,  # type: Union[str, unicode]
    typeId,  # type: Union[str, unicode]
):
    # type: (...) -> List[PyResource]
    """Returns a resource from the Gateway.

    Args:
        moduleId: The module ID portion of the resource type identifier.
        typeId: The type ID portion of the resource type identifier.

    Returns:
        A List of all the resources of the specified type, as a
        PyResource.
    """
    print(moduleId, typeId)
    return [PyResource()]


def getResourceTypes():
    # type: () -> List[Any]
    """Returns a list of all registered resource types.

    Returns:
        A list of tuples containing all the currently registered
        resource types on the Gateway.
    """
    return []


def move(
    moduleId,  # type: Union[str, unicode]
    typeId,  # type: Union[str, unicode]
    name=None,  # type: Union[str, unicode, None]
    collection=None,  # type: Union[str, unicode, None]
    newCollection=None,  # type: Union[str, unicode, None]
    signature=None,  # type: Union[str, unicode, None]
    actor=None,  # type: Union[str, unicode, None]
):
    # type: (...) -> PyResource
    """Moves a resource to a different collection.

    The move operation changes which collection a resource belongs to,
    but does not allow renaming. Use the rename() operation to change a
    resource's name.

    Args:
        moduleId: The module ID portion of the resource type identifier.
        typeId: The type ID portion of the resource type identifier.
        name: The name of the resource. Required for named resources,
            but must be omitted for singleton resources. Optional.
        collection: The collection containing the resource. If omitted,
            uses the active definition. Optional.
        newCollection: The new collection for the copied resource.
            Required if not changing name for singleton resource types.
            Optional.
        signature: The hex-encoded signature of the resource. Optional.
        actor: A string identifying the actor performing the operation.
            If not specified, an identifier will be automatically
            generated. Optional.

    Returns:
        The Gateway resource that was moved, which can also be read as
        plain Python properties.
    """
    print(moduleId, typeId, name, collection, newCollection, signature, actor)
    return PyResource()


def rename(
    moduleId,  # type: Union[str, unicode]
    typeId,  # type: Union[str, unicode]
    name=None,  # type: Union[str, unicode, None]
    collection=None,  # type: Union[str, unicode, None]
    newName=None,  # type: Union[str, unicode, None]
    references=None,  # type: Union[str, unicode, None]
    actor=None,  # type: Union[str, unicode, None]
):
    # type: (...) -> PyResource
    """Renames the specified resource within its current collection.

    Use the move() function to transfer resources between collections.

    Args:
        moduleId: The module ID portion of the resource type identifier.
        typeId: The type ID portion of the resource type identifier.
        name: The name of the resource. Required for named resources,
            but must be omitted for singleton resources. Optional.
        collection: The collection containing the resource. If omitted,
            uses the active definition. Optional.
        newName: The new name for the resource.
        references: How Ignition should handle references from other
            resources to the current value of the resource that is being
            renamed. Optional.
        actor: A string identifying the actor performing the operation.
            If not specified, an identifier will be automatically
            generated. Optional.

    Returns:
        The resource that was renamed, as a PyResource that can also be
        read as plain Python properties.
    """
    print(moduleId, typeId, name, collection, newName, references, actor)
    return PyResource()


def replace(
    moduleId,  # type: Union[str, unicode]
    typeId,  # type: Union[str, unicode]
    name=None,  # type: Union[str, unicode, None]
    collection=None,  # type: Union[str, unicode, None]
    signature=None,  # type: Union[str, unicode, None]
    config=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    backupConfig=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    files=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    description=None,  # type: Union[str, unicode, None]
    enabled=None,  # type: Optional[bool]
    attributes=None,  # type: Optional[Dict[Union[str, unicode], Any]]
    actor=None,  # type: Union[str, unicode, None]
):
    # type: (...) -> PyResource
    """Copies a resource to a new name and/or collection.

    When using this function, either the newName or newCollection
    parameter must be defined.

    Args:
        moduleId: The module ID portion of the resource type identifier.
        typeId: The type ID portion of the resource type identifier.
        name: The name of the resource. Required for named resources,
            but must be omitted for singleton resources. Optional.
        collection: The collection containing the resource. If omitted,
            uses the active definition. Optional.
        signature: The hex-encoded signature of the resource. Optional.
        config: A dictionary representing the resource configuration,
            matching the resource type's JSON schema. If not provided,
            the files argument must be provided. Optional.
        backupConfig: A dictionary representing the backup configuration
            for resources that support backup data. Optional.
        files: A dictionary of additional files to include with the
            resource. Keys are filenames, values can be byte arrays,
            strings, lists, or dictionaries. If not provided, the config
            argument must be provided. Optional.
        description: A description for the resource. Optional.
        enabled: Whether the replacement resource should be enabled. If
            omitted, the resource will be in the same state after its
            configuration is replaced. Optional.
        attributes: A dictionary of resource attributes to set.
            Optional.
        actor: A string identifying the actor performing the operation.
            If not specified, an identifier will be automatically
            generated. Optional.

    Returns:
        The newly configured resource, as a PyResource that can also be
        read as plain Python properties.
    """
    print(
        moduleId,
        typeId,
        name,
        collection,
        signature,
        config,
        backupConfig,
        files,
        description,
        enabled,
        attributes,
        actor,
    )
    return PyResource()
