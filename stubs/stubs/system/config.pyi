from typing import Any, Dict, List, Optional, Union

from com.inductiveautomation.ignition.gateway.script import PyResource

def copy(
    moduleId: Union[str, unicode],
    typeId: Union[str, unicode],
    name: Union[str, unicode, None] = ...,
    collection: Union[str, unicode, None] = ...,
    newName: Union[str, unicode, None] = ...,
    newCollection: Union[str, unicode, None] = ...,
    signature: Union[str, unicode, None] = ...,
    actor: Union[str, unicode, None] = ...,
) -> PyResource: ...
def create(
    moduleId: Union[str, unicode],
    typeId: Union[str, unicode],
    name: Union[str, unicode, None] = ...,
    collection: Union[str, unicode, None] = ...,
    config: Optional[Dict[Union[str, unicode], Any]] = ...,
    backupConfig: Optional[Dict[Union[str, unicode], Any]] = ...,
    files: Optional[Dict[Union[str, unicode], Any]] = ...,
    description: Union[str, unicode, None] = ...,
    enabled: Optional[bool] = ...,
    attributes: Optional[Dict[Union[str, unicode], Any]] = ...,
    actor: Union[str, unicode, None] = ...,
) -> PyResource: ...
def delete(
    moduleId: Union[str, unicode],
    typeId: Union[str, unicode],
    name: Union[str, unicode, None] = ...,
    collection: Union[str, unicode, None] = ...,
    signature: Union[str, unicode, None] = ...,
    force: bool = ...,
    actor: Union[str, unicode, None] = ...,
) -> None: ...
def getActiveMode() -> Union[str, unicode, None]: ...
def getModes() -> List[Union[str, unicode]]: ...
def getResource(
    moduleId: Union[str, unicode],
    typeId: Union[str, unicode],
    name: Union[str, unicode],
    collection: Union[str, unicode],
) -> PyResource: ...
def getResources(
    moduleId: Union[str, unicode], typeId: Union[str, unicode]
) -> List[PyResource]: ...
def getResourceTypes() -> List[Any]: ...
def move(
    moduleId: Union[str, unicode],
    typeId: Union[str, unicode],
    name: Union[str, unicode, None] = ...,
    collection: Union[str, unicode, None] = ...,
    newCollection: Union[str, unicode, None] = ...,
    signature: Union[str, unicode, None] = ...,
    actor: Union[str, unicode, None] = ...,
) -> PyResource: ...
def rename(
    moduleId: Union[str, unicode],
    typeId: Union[str, unicode],
    name: Union[str, unicode, None] = ...,
    collection: Union[str, unicode, None] = ...,
    newName: Union[str, unicode, None] = ...,
    references: Union[str, unicode, None] = ...,
    actor: Union[str, unicode, None] = ...,
) -> PyResource: ...
def replace(
    moduleId: Union[str, unicode],
    typeId: Union[str, unicode],
    name: Union[str, unicode, None] = ...,
    collection: Union[str, unicode, None] = ...,
    signature: Union[str, unicode, None] = ...,
    config: Optional[Dict[Union[str, unicode], Any]] = ...,
    backupConfig: Optional[Dict[Union[str, unicode], Any]] = ...,
    files: Optional[Dict[Union[str, unicode], Any]] = ...,
    description: Union[str, unicode, None] = ...,
    enabled: Optional[bool] = ...,
    attributes: Optional[Dict[Union[str, unicode], Any]] = ...,
    actor: Union[str, unicode, None] = ...,
) -> PyResource: ...
