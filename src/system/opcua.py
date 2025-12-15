"""OPC - UA Functions.

The following functions allow you to interact directly with an OPC-UA
server.
"""

from __future__ import print_function

__all__ = ["callMethod"]

from typing import Any, List, Tuple, Union

String = Union[str, unicode]


def callMethod(
    connectionName,  # type: String
    objectId,  # type: String
    methodId,  # type: String
    inputs,  # type: List[String]
):
    # type: (...) -> Tuple[Any, Any, Any]
    """Calls a method in an OPC UA Server.

    To make the most of this n, you'll need to be familiar with methods
    in the OPC UA Server.

    Args:
        connectionName: The name of the OPC UA connection to the Server
            that the method resides in.
        objectId: The NodeId of the Object Node the Method is a member
            of.
        methodId: The NodeId of the Method Node to call.
        inputs: A list of input values expected by the method.

    Returns:
        A tuple containing the following:
            0: Resulting StatusCode for the call
            1: A list of StatusCode objects corresponding to each
                input argument
            2: A list of output values

    """
    print(connectionName, objectId, methodId, inputs)
    return None, None, None
