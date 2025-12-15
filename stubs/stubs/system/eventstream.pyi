from typing import Any, Dict, Union

def getDiagnostics(project: Union[str, unicode], path: Union[str, unicode]) -> None: ...
def listEventStreams(project: Union[str, unicode]) -> None: ...
def publishEvent(
    project: Union[str, unicode],
    path: Union[str, unicode],
    message: Union[str, unicode],
    acknowledge: bool,
    gatewayId: Union[str, unicode, None] = ...,
) -> Dict[Union[str, unicode], Any]: ...
