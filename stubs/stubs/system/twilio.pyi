from typing import List, Union

from com.inductiveautomation.ignition.common import BasicDataset
from com.twilio.rest.api.v2010.account import Call

def getAccounts() -> List[Union[str, unicode]]: ...
def getAccountsDataset() -> BasicDataset: ...
def getActiveCall(accountName: Union[str, unicode]) -> List[Call]: ...
def getPhoneNumbers(accountName: Union[str, unicode]) -> List[Union[str, unicode]]: ...
def getPhoneNumbersDataset(accountName: Union[str, unicode]) -> BasicDataset: ...
def sendFreeformWhatsApp(
    accountName: Union[str, unicode],
    fromNumber: Union[str, unicode],
    toNumber: Union[str, unicode],
    message: Union[str, unicode],
) -> None: ...
def sendPhoneCall(
    accountName: Union[str, unicode],
    fromNumber: Union[str, unicode],
    toNumber: Union[str, unicode],
    message: Union[str, unicode],
    voice: Union[str, unicode] = ...,
    language: Union[str, unicode] = ...,
    recordCall: bool = ...,
) -> None: ...
def sendSms(
    accountName: Union[str, unicode],
    fromNumber: Union[str, unicode],
    toNumber: Union[str, unicode],
    message: Union[str, unicode],
) -> None: ...
def sendWhatsAppTemplate(
    accountName: Union[str, unicode],
    userNumber: Union[str, unicode],
    whatsAppService: Union[str, unicode],
    whatsAppTemplate: Union[str, unicode],
    templateParameters: Union[str, unicode],
) -> None: ...
