"""Security Functions.

The following functions give you access to interact with the users and
roles in the Gateway. These functions require the Vision module, as
these functions can only be used with User Sources and their interaction
with Vision Clients.
"""

from __future__ import print_function

__all__ = [
    "getUserRoles",
    "validateUser",
]

from typing import Optional, Tuple, Union


def getUserRoles(
    username,  # type: Union[str, unicode]
    password,  # type: Union[str, unicode]
    authProfile="",  # type: Union[str, unicode]
    timeout=60000,  # type: int
):
    # type: (...) -> Optional[Tuple[Union[str, unicode], ...]]
    """Fetches the roles for a user from the Gateway.

    This may not be the currently logged in user. Requires the password
    for that user. If the authentication profile name is omitted, then
    the current project's default authentication profile is used.

    Args:
        username: The username to fetch roles for.
        password: The password for the user.
        authProfile: The name of the authentication profile to run
            against. Leaving this out will use the project's default
            profile. Optional.
        timeout: Timeout for Client-to-Gateway communication. Default is
            60,000ms. Optional.


    Returns:
        A list of the roles that this user has, if the user
        authenticates successfully. Otherwise, returns None.
    """
    print(username, password, authProfile, timeout)
    return "Administrator", "Developer"


def validateUser(
    username,  # type: Union[str, unicode]
    password,  # type: Union[str, unicode]
    authProfile="",  # type: Union[str, unicode]
    timeout=60000,  # type: int
):
    # type: (...) -> bool
    """Tests credentials (username and password) against an
    authentication profile.

    Returns a boolean based upon whether or not the authentication
    profile accepts the credentials. If the authentication profile name
    is omitted, then the current project's default authentication
    profile is used.

    Args:
        username: The username to validate.
        password: The password for the user.
        authProfile: The name of the authentication profile to run
            against. Leaving this out will use the project's default
            profile. Optional.
        timeout: Timeout for Client-to-Gateway communication. Default is
            60,000ms. Optional.

    Returns:
        False if the user failed to authenticate, True if the
        username/password was a valid combination.
    """
    print(username, password, authProfile, timeout)
    return True
