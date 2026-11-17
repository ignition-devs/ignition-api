"""Internationalization Functions.

The following functions give you access to translation keys, notes, and
translations.
"""

from __future__ import print_function

__all__ = ["listKeys", "modifyNotes", "modifyTranslations", "translate"]

from typing import Dict, List, Optional, Union

from java.util import Locale


def listKeys():
    # type: () -> List[Union[str, unicode]]
    """Returns all translation keys.

    Returns:
        A list of all translation keys.
    """
    return []


def modifyNotes(
    values,  # type: Dict[Union[str, unicode], Union[str, unicode, None]]
):
    # type: (...) -> None
    """Adds, updates, or removes notes on one or more translation keys.

    Args:
        values: A dictionary mapping each translation key to its note. A
            value of None removes the key's note.
    """
    print(values)


def modifyTranslations(
    values,  # type: Dict[Union[str, unicode], Union[str, unicode, None]]
    locale,  # type: Union[str, unicode, Locale]
):
    # type: (...) -> None
    """Adds, updates, or removes translations for a single locale.

    Args:
        values: A dictionary mapping each translation key to its
            translation for the given locale. A value of None removes
            the key's translation.
        locale: The locale the values dictionary applies to, such as
            "it" or "en-IE". Accepts a Java Locale object, a BCP-47
            language tag, or a Java locale identifier.
    """
    print(values, locale)


def translate(
    terms,  # type: List[Union[str, unicode]]
    locale=None,  # type: Union[str, unicode, Locale, None]
    strict=False,  # type: Optional[bool]
):
    # type: (...) -> List[Union[str, unicode, None]]
    """Translates a list of terms in bulk.

    Args:
        terms: The terms to translate.
        locale: The locale to translate the terms to, such as "it" or
            "en-IE". Accepts a Java Locale object, a BCP-47 language
            tag, or a Java locale identifier. If omitted, the function
            attempts to use the default locale of the current context,
            such as the Perspective Session or the Gateway. Optional.
        strict: If True, a term without a defined translation returns
            None. If False, the original term is returned. Optional.

    Returns:
        The translated terms.
    """
    print(locale)
    return [None for _ in terms] if strict else list(terms)
