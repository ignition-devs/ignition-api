"""File Functions.

The following functions give you access to read and write to files.
"""

from __future__ import print_function

__all__ = [
    "ISO8859_1",
    "US_ASCII",
    "UTF_16",
    "UTF_16BE",
    "UTF_16LE",
    "UTF_8",
    "fileExists",
    "getTempFile",
    "readFileAsBytes",
    "readFileAsString",
    "writeFile",
]

import io
import os.path
import tempfile
from typing import Any, Union

# Encoding Constants
ISO8859_1 = "ISO-8859-1"
US_ASCII = "US-ASCII"
UTF_8 = "UTF-8"
UTF_16 = "UTF-16"
UTF_16BE = "UTF-16BE"
UTF_16LE = "UTF-16LE"


def fileExists(filepath):
    # type: (Union[str, unicode]) -> bool
    """Checks to see if a file or folder at a given path exists.

    Note:
        This function is scoped for Perspective Sessions, but since all
        scripts in Perspective run on the Gateway, the file must be
        located on the Gateway's file system.

    Args:
        filepath: The path of the file or folder to check.

    Returns:
        True if the file/folder exists, False otherwise.
    """
    return os.path.isfile(filepath)


def getTempFile(extension):
    # type: (Union[str, unicode]) -> Union[str, unicode]
    """Creates a new temp file on the host machine with a certain
    extension, returning the path to the file.

    The file is marked to be removed when the Java VM exits.

    Note:
        This function is scoped for Perspective Sessions, but since all
        scripts in Perspective run on the Gateway, the file must be
        located on the Gateway's file system.

    Args:
        extension: An extension, like ".txt", to append to the end of
            the temporary file.

    Returns:
        The path to the newly created temp file.
    """
    suffix = ".{}".format(extension)
    with tempfile.NamedTemporaryFile(suffix=suffix) as temp:
        return unicode(temp.name)


def readFileAsBytes(filepath):
    # type: (Union[str, unicode]) -> Any
    """Opens the file found at path filename, and reads the entire file.

    Returns the file as an array of bytes. Commonly this array of bytes
    is uploaded to a database table with a column of type BLOB (Binary
    Large OBject). This upload would be done through an INSERT or UPDATE
    SQL statement run through the system.db.runPrepUpdate function. You
    could also write the bytes to another file using the
    system.file.writeFile function, or send the bytes as an email
    attachment using system.net.sendEmail.

    Note:
        This function is scoped for Perspective Sessions, but since all
        scripts in Perspective run on the Gateway, the file must be
        located on the Gateway's file system.

    Args:
        filepath: The path of the file to read.

    Returns:
        The contents of the file as an array of bytes.
    """
    with io.open(filepath, "r+b") as f:
        return f.read()


def readFileAsString(
    filepath,  # type: Union[str, unicode]
    encoding="UTF-8",  # type: Union[str, unicode]
):
    # type: (...) -> Union[str, unicode]
    """Opens the file found at path filename, and reads the entire file.

    Returns the file as a string. Common things to do with this string
    would be to load it into the text property of a component, upload it
    to a database table, or save it to another file using
    system.file.writeFile function.

    Note:
        This function is scoped for Perspective Sessions, but since all
        scripts in Perspective run on the Gateway, the file must be
        located on the Gateway's file system.

    Args:
        filepath: The path of the file to read.
        encoding: The character encoding of the file to be read. Will
            throw an exception if the string does not represent a
            supported encoding. Common encodings are "UTF-8",
            "ISO-8859-1" and "US-ASCII". Default is "UTF-8". Optional.

    Returns:
        The contents of the file as a string.
    """
    with io.open(filepath, "r", encoding=encoding) as f:
        return unicode(f.read())


def writeFile(
    filepath,  # type: Union[str, unicode]
    data,  # type: Any
    append=False,  # type: bool
    encoding="UTF-8",  # type: Union[str, unicode]
):
    # type: (...) -> None
    """Writes the given data to the file at file path filename.

    If the file exists, the append argument determines whether or not it
    is overwritten (the default) or appended to. The data argument can
    be either a string or an array of bytes (commonly retrieved from a
    BLOB in a database or read from another file using
    system.file.readFileAsBytes).

    Note:
        This function is scoped for Perspective Sessions, but since all
        scripts in Perspective run on the Gateway, the file must be
        located on the Gateway's file system.

    Args:
        filepath: The path of the file to write to.
        data: The character or binary content to write to the file.
        append: If True, the file will be appended to if it already
            exists. If False, the file will be overwritten if it
            exists. The default is False. Optional.
        encoding: The character encoding of the file to write. Will
            throw an exception if the string does not represent a
            supported encoding. Common encodings are "UTF-8",
            "ISO-8859-1" and "US-ASCII". Default is "UTF-8". Optional.
    """
    print(filepath, data, append, encoding)
