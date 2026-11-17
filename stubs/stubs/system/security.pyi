from typing import Optional, Tuple, Union

def getUserRoles(
    username: Union[str, unicode],
    password: Union[str, unicode],
    authProfile: Union[str, unicode] = ...,
    timeout: int = ...,
) -> Optional[Tuple[Union[str, unicode], ...]]: ...
def validateUser(
    username: Union[str, unicode],
    password: Union[str, unicode],
    authProfile: Union[str, unicode] = ...,
    timeout: int = ...,
) -> bool: ...
