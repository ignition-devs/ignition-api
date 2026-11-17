from typing import Any, Dict, List, Optional, Union

def listAgents() -> List[Dict[Union[str, unicode], Any]]: ...
def sendMessage(
    agent: Union[str, unicode],
    prompt: Union[str, unicode],
    modelOverride: Union[str, unicode, None] = ...,
    timeoutSecs: Optional[Any] = ...,
) -> Union[str, unicode]: ...
