"""AI Functions.

The following functions give you access to user-authored AI Agents
registered on the Gateway.
"""

from __future__ import print_function

__all__ = ["listAgents", "sendMessage"]

from typing import Any, Dict, List, Optional, Union


def listAgents():
    # type: () -> List[Dict[Union[str, unicode], Any]]
    """Returns a list of all user-authored Agents registered on the
    Gateway.

    Returns:
        A list containing the name, provider, model, and description of
        each agent.
    """
    return [
        {
            "name": "AgentName",
            "provider": "ProviderName",
            "model": "ModelId",
            "description": "AgentDescription",
        }
    ]


def sendMessage(
    agent,  # type: Union[str, unicode]
    prompt,  # type: Union[str, unicode]
    modelOverride=None,  # type: Union[str, unicode, None]
    timeoutSecs=None,  # type: Optional[Any]
):
    # type: (...) -> Union[str, unicode]
    """Sends a one-shot prompt to a user-authored AI agent and returns
    the model's final text reply.

    Args:
        agent: Name of the agent to send the prompt to. This value must
            match the agent resource name in the Gateway configuration
            tree.
        prompt: The prompt to send to the agent.
        modelOverride: Overrides the agent's configured modelId for
            this value. Optional.
        timeoutSecs: This value is accepted for stability, but is not
            currently enforced. Optional.

    Returns:
        The model's final text reply, after the agent has dispatched
        any tool calls.
    """
    print(agent, prompt, modelOverride, timeoutSecs)
    return ""
