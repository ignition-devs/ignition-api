"""Twilio Functions.

The following functions give you access to read info and send SMS
through Twilio. This requires the Twilio Module, which is not included
in a typical install.
"""

from __future__ import print_function

__all__ = [
    "getAccounts",
    "getAccountsDataset",
    "getActiveCall",
    "getPhoneNumbers",
    "getPhoneNumbersDataset",
    "sendFreeformWhatsApp",
    "sendPhoneCall",
    "sendSms",
    "sendWhatsAppTemplate",
]

from typing import List, Union

from com.inductiveautomation.ignition.common import BasicDataset
from com.twilio.rest.api.v2010.account import Call


def getAccounts():
    # type: () -> List[Union[str, unicode]]
    """Return a list of Twilio accounts that have been configured in the
    Gateway.

    Returns:
        A list of configured Twilio accounts.
    """
    return ["twilio_account1", "twilio_account2"]


def getAccountsDataset():
    # type: () -> BasicDataset
    """Return a list of Twilio accounts that have been configured in the
    Gateway as a single-column Dataset.

    Returns:
        A list of configured Twilio accounts as a single-column Dataset.
    """
    return BasicDataset()


def getActiveCall(accountName):
    # type: (Union[str, unicode]) -> List[Call]
    """Returns a list of configurations for currently active Twilio
    voice calls.

    This only applies to synchronous calls that use the reverse-proxy
    system to call back into Ignition for authentication and alarm
    acknowledgements. Since calls can last minutes and potentially be
    stuck ringing for some time, this function gives users a view of the
    current state of call notifications while they're active.

    Args:
        accountName: The Twilio account to retrieve active calls for.

    Returns:
        A list of active phone calls for the given Twilio account.
    """
    print(accountName)
    return [Call()]


def getPhoneNumbers(accountName):
    # type: (Union[str, unicode]) -> List[Union[str, unicode]]
    """Returns a list of outgoing phone numbers for a Twilio account.

    Note that these numbers are supplied by Twilio, and are not defined
    on a user in Ignition.

    Args:
        accountName: The Twilio account to retrieve phone numbers for.

    Returns:
        A list of phone numbers for the given Twilio account.
    """
    phoneNumbers = []  # type: List[Union[str, unicode]]
    if accountName == "Jenny":
        phoneNumbers.append("+12058675309")
    return phoneNumbers


def getPhoneNumbersDataset(accountName):
    # type: (Union[str, unicode]) -> BasicDataset
    """Return a list of outgoing phone numbers for a Twilio account as a
    single-column Dataset.

    Note that these numbers are supplied by Twilio, and are not defined
    on a user in Ignition.

    Args:
        accountName: The Twilio account to retrieve phone numbers for.

    Returns:
        A list of phone numbers for the given Twilio account as a
        single-column Dataset.
    """
    print(accountName)
    return BasicDataset()


def sendFreeformWhatsApp(
    accountName,  # type: Union[str, unicode]
    fromNumber,  # type: Union[str, unicode]
    toNumber,  # type: Union[str, unicode]
    message,  # type: Union[str, unicode]
):
    # type: (...) -> None
    """Sends a free-form WhatsApp message.

    WhatsApp considers any message that is not a pre-approved template a
    free-form message. Free-form messages can only be sent with Ignition
    after a 24-hour Session opens. A user can open a 24-hour Session by
    simply sending a WhatsApp message to the Twilio account. Then, the
    Session remains open for 24 hours from the last inbound message
    received from the user.

    Args:
        accountName: The Twilio account to send from.
        fromNumber: The phone number configured with Twilio to use for
            making the calls.
        toNumber: The phone number of the recipient.
        message: The body of the free-form WhatsApp message.
    """
    print(accountName, fromNumber, toNumber, message)


def sendPhoneCall(
    accountName,  # type: Union[str, unicode]
    fromNumber,  # type: Union[str, unicode]
    toNumber,  # type: Union[str, unicode]
    message,  # type: Union[str, unicode]
    voice="man",  # type: Union[str, unicode]
    language="en-US",  # type: Union[str, unicode]
    recordCall=False,  # type: bool
):
    # type: (...) -> None
    """Sends a phone call to a specific phone number.

    In order to work, a Twilio account must be configured in the Gateway
    with a valid number configured for use with Twilio Voice.

    Args:
        accountName: The Twilio account to use for the calls.
        fromNumber: The phone number configured with Twilio to use for
            making the calls.
        toNumber: The phone number of the recipient.
        message: The message text to use in the call.
        voice: The voice-to-text algorithm to use. "man" and "woman" are
            the basic Twilio voice-to-text algorithms, but Twilio also
            supports using Amazon's and Google's voice-to-text
            algorithms, though pricing may vary depending on your Twilio
            subscription. Defaults to "man". Optional.
        language: The language code for the language to use for
            text-to-speech generation. Defaults to "en-US" if no
            language is configured. Optional.
        recordCall: Whether to record the calls. Defaults to False.
            Optional.
    """
    print(
        accountName,
        fromNumber,
        toNumber,
        message,
        voice,
        language,
        recordCall,
    )


def sendSms(
    accountName,  # type: Union[str, unicode]
    fromNumber,  # type: Union[str, unicode]
    toNumber,  # type: Union[str, unicode]
    message,  # type: Union[str, unicode]
):
    # type: (...) -> None
    """Sends an SMS message.

    Args:
        accountName: The Twilio account to send the SMS from.
        fromNumber: The outbound phone number belonging to the Twilio
            account to use.
        toNumber: The phone number of the recipient.
        message: The body of the SMS.
    """
    print(accountName, fromNumber, toNumber, message)


def sendWhatsAppTemplate(
    accountName,  # type: Union[str, unicode]
    userNumber,  # type: Union[str, unicode]
    whatsAppService,  # type: Union[str, unicode]
    whatsAppTemplate,  # type: Union[str, unicode]
    templateParameters,  # type: Union[str, unicode]
):
    # type: (...) -> None
    """Sends a WhatsApp template message.

    Template messages are configurable messages on Twilio that can be
    sent to users via Twilio WhatsApp Refer to WhatsApp Template
    Overview documentation for more information.
    """
    print(
        accountName, userNumber, whatsAppService, whatsAppTemplate, templateParameters
    )
