"""Secrets Functions.

The following functions are used to interact with encrypted secrets for
Secret Providers on the Gateway.
"""

from __future__ import print_function

__all__ = [
    "createEmbeddedSecretConfig",
    "createReferencedSecretConfig",
    "decrypt",
    "encrypt",
    "getProviders",
    "getSecrets",
    "readConfiguredSecretValue",
    "readSecretValue",
]

from typing import Any, Dict, List, Union

from com.inductiveautomation.ignition.common.secrets import (
    PyPlaintext,
    SecretMeta,
    SecretProviderMeta,
)
from com.inductiveautomation.ignition.gateway.secrets import Plaintext, SecretException
from org.python.core import PyObject


def createEmbeddedSecretConfig(json):
    # type: (Any) -> PyObject
    """Creates a new Embedded SecretConfig instance given the JSON
    representation of the encrypted data.

    Args:
        json: The JSON object containing the encrypted secret.

    Returns:
        A Dictionary containing the JSON representation of an Embedded
        SecretConfig instance containing the encrypted secret.

    Raises:
        ValueError: Throws a ValueError if there is no JSON.
    """
    if not json:
        raise ValueError("No JSON provided for creating an Embedded SecretConfig.")
    return PyObject()


def createReferencedSecretConfig(providerName, secretName):
    # type: (Union[str, unicode], Union[str, unicode]) -> PyObject
    """Creates a new Referenced SecretConfig instance given the name of
    the secret provider and the name of the secret stored in the
    provider.

    Args:
        providerName: The name of the Secret Provider to reference.
        secretName: The name of the secret to reference.

    Returns:
        PyObject: A Dictionary containing the JSON representation of a
            Referenced SecretConfig instance with the provider and
            secret names.

    Raises:
        ValueError: Throws a ValueError if the providerName or
            secretName parameters do not have any values.
    """
    if not providerName or not secretName:
        raise ValueError("Both providerName and secretName must be provided.")
    return PyObject()


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


def readConfiguredSecretValue(secretConfig):
    # type: (Any) -> PyPlaintext
    """Reads the value of a secret configured by its SecretConfig.

    Args:
        secretConfig: The JSON object containing the SecretConfig.

    Returns:
        A PyPlaintext instance containing the specified secret.

    Raises:
        ValueError: Throws a ValueError if there is no JSON.
        SecretException: Throws a SecretException if there is a problem
            reading the secret.
    """
    if not secretConfig:
        raise ValueError("There is no JSON.")
    if not isinstance(secretConfig, dict):
        raise SecretException("There is a problem reading the secret.")
    return PyPlaintext(Plaintext())


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
