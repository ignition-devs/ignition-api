from typing import Dict, List, Optional, Union

from java.util import Locale

def listKeys() -> List[Union[str, unicode]]: ...
def modifyNotes(
    values: Dict[Union[str, unicode], Union[str, unicode, None]],
) -> None: ...
def modifyTranslations(
    values: Dict[Union[str, unicode], Union[str, unicode, None]],
    locale: Union[str, unicode, Locale],
) -> None: ...
def translate(
    terms: List[Union[str, unicode]],
    locale: Union[str, unicode, Locale, None] = ...,
    strict: Optional[bool] = ...,
) -> List[Union[str, unicode, None]]: ...
