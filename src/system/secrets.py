"""Secrets Functions.

The following functions are used to interact with encrypted secrets for
Secret Providers on the Gateway.
"""

from __future__ import print_function

__all__ = [
    "decrypt",
    "encrypt",
    "getProviders",
    "getSecrets",
    "readSecretValue",
]

from typing import Any, Dict, List, Union

from com.inductiveautomation.ignition.common.secrets import (
    PyPlaintext,
    SecretMeta,
    SecretProviderMeta,
)
from com.inductiveautomation.ignition.gateway.secrets import Plaintext


def decrypt(json):
    # type: (Any) -> PyPlaintext
    """Decrypts the given JSON object containing an encrypted secret
    using the system encryption service.

    Args:
        json: The JSON object containing the encrypted secret to
            decrypt.

    Returns:
        The decrypted value of the JSON string.
    """
    return PyPlaintext(Plaintext.fromString(json))


def encrypt(*args):
    # type: (*Any) -> Dict[Union[str, unicode], Any]
    """Encrypts supplied data using the Secrets Management system
    encryption service and returns a JSON object containing the
    encrypted secret.

    Args:
        *args: Variable length argument list.

    Returns:
        A PyDictionary containing the encrypted secret or None if the
        JSON is empty.
    """
    return {
        "ciphertext": None,
        "encrypted_key": None,
        "iv": None,
        "protected": True,
        "tag": None,
    }


def getProviders():
    # type: () -> List[SecretProviderMeta]
    """Returns a list of Secret Providers configured in the Secrets
    Management system on the Gateway. Each list entry includes the name,
    description, and type of the provider.

    Returns:
        A List of SecretProviderMeta instances that represent all of
        the Secret Providers.
    """
    return [
        SecretProviderMeta(
            "SecretProviderName", "SecretProviderDescription", "SecretProviderType"
        )
    ]


def getSecrets(providerName):
    # type: (Union[str, unicode]) -> List[SecretMeta]
    """Returns a list of objects representing all secrets available for
    the named Secret Provider.

    Each list entry includes the name of the secret.

    Args:
        providerName: The name of the Secret Provider to fetch secrets
            from.

    Returns:
        A list of SecretMeta instances that represent all secret names.
    """
    print(providerName)
    return [SecretMeta("SecretName")]


def readSecretValue(providerName, secretName):
    # type: (Union[str, unicode], Union[str, unicode]) -> PyPlaintext
    """Reads the plaintext value of a secret given the name of the
    Secret Provider and the name of the secret.

    Args:
        providerName: The name of the Secret Provider to read the secret
            from.
        secretName: The name of the secret to read.

    Returns:
        A PyPlaintext instance that contains the secret.
    """
    print(providerName, secretName)
    return PyPlaintext(Plaintext())
