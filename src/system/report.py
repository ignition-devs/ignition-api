"""Report Functions.

The following functions give you access to report details and the
ability to run reports.
"""

from __future__ import print_function

__all__ = [
    "executeAndDistribute",
    "executeReport",
    "getReportNamesAsDataset",
    "getReportNamesAsList",
]

from typing import Any, Dict, List, Optional

from com.inductiveautomation.ignition.common import BasicDataset
from java.lang import IllegalArgumentException, String


def executeAndDistribute(
    path,  # type: String
    project="project",  # type: Optional[String]
    parameters=None,  # type: Optional[Dict[String, int]]
    action=None,  # type: Optional[String]
    actionSettings=None,  # type: Optional[Dict[String, Any]]
):
    # type: (...) -> None
    """Executes and distributes a report.

    Similar to scheduling a report to execute, except a schedule in not
    required to utilize this function. This is a great way to distribute
    the report on demand from a client.

    Args:
        path: The path to the existing report.
        project: The name of the project where the report is located.
            Optional in client scope.
        parameters: An optional dictionary of parameter overrides, in
            the form name:value.
        action: The name of the distribution action to use.
        actionSettings: An optional dictionary of settings particular to
            the action. Missing values will use the default value for
            that action.

    Raises:
        IllegalArgumentException: Thrown when any of the following
            occurs: If the file type is not recognized, path does not
            exist, project does not exist, or a key is not valid.
    """
    if project is not None:
        print(path, project, parameters, action, actionSettings)
    else:
        raise IllegalArgumentException()


def executeReport(
    path,  # type: String
    project="project",  # type: Optional[String]
    parameters=None,  # type: Optional[Dict[String, int]]
    fileType="pdf",  # type: Optional[String]
):
    # type: (...) -> Any
    """Immediately executes an existing report and returns a byte[] of
    the output.

    Args:
        path: The path to the existing report.
        project: The name of the project where the report is located.
            Optional in client scope.
        parameters: An optional dictionary of parameter overrides, in
            the form name:value. Optional.
        fileType: The file type the resulting byte array should
            represent. Defaults to "pdf". Not case-sensitive. Optional.

    Returns:
        A byte array of the resulting report.

    Raises:
        IllegalArgumentException: Thrown when any of the following
            occurs: If the file type is not recognized, path does not
            exist, project does not exist.
    """
    _fileTypes = ["pdf", "html", "csv", "rtf", "jpeg", "png", "xml"]
    if path is None or project is None or fileType not in _fileTypes:
        raise IllegalArgumentException()
    print(path, project, parameters, fileType)


def getReportNamesAsDataset(project="project"):
    # type: (Optional[String]) -> BasicDataset
    """Gets a data of all reports for a project.

    This dataset is particularly suited for display in a Tree View
    component.

    Args:
        project: The name of the project where the reports are located.
            Optional in client scope.

    Returns:
        A dataset of report paths and names for the project. Returns an
        empty dataset if the project has no reports.

    Raises:
        IllegalArgumentException: Thrown when any of the following
            occurs: If the project name is omitted in the Gateway scope,
            project does not exist.
    """
    if project is None:
        raise IllegalArgumentException()
    return BasicDataset()


def getReportNamesAsList(project="project"):
    # type: (Optional[String]) -> List[String]
    """Gets a list of all reports for a project.

    Args:
        project: The name of the project where the reports are located.
            Optional in client scope.

    Returns:
        A list of report paths for the project. Returns an empty list if
        the project has no reports.

    Raises:
        IllegalArgumentException: Thrown when any of the following
            occurs: If the project name is omitted in the Gateway scope,
            project does not exist.
    """
    if project is None:
        raise IllegalArgumentException()
    return []
