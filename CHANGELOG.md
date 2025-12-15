## v7.9.21 (2022-07-27)

### Feat

- **java**: add String to java.lang (#22)

## v7.9.20 (2022-05-13)

### Fix

- **system**: update type hint for `html` arg (#17)

## v7.9.19 (2022-03-15)

### Refactor

- Sourcery refactored main branch (#1)

## v7.9.18.post7 (2022-01-20)

### Refactor

- move `String` alias to `java.util`
- define ColType as a type alias

## v7.9.18.post6 (2021-11-30)

### Feat

- simplify `beep` code

### BREAKING CHANGE

- `system.util.beep()` will print "Beep!" when called
regardless of platform

### Fix

- **mypy**: add `String` type definition

## v7.9.18.post5 (2021-11-29)

### Feat

- add `String` type

## v7.9.18.post4 (2021-11-26)

### Fix

- install now requires typing

## v7.9.18.post3 (2021-11-23)

### Feat

- add type hints on all `system` functions
- remove deprecated functions
- the triumphant return of `print_function`
- improve `date.format`

### BREAKING CHANGE

- Python versions below 2.7.18 are no longer supported
- `export*` functions have been deprecated in favor
of `system.dataset.export*` functions
- Python versions below 2.7.18 are no longer supported

### Fix

- **ci**: set `python-version` to '3.10'
- **ci**: set `python-version` to 3.10.0

### Refactor

- implement informal interfaces

## v7.9.18.post2 (2021-09-21)

### Feat

- make PyDataSet iterable

## v7.9.18.post1 (2021-09-20)

### Feat

- add `com` package to `pip` release
- **setup**: allow installation on 2.5, 2.6, and 2.7
- **setup**: add setup.py

### Refactor

- use pprint instead of print
- add `com` package
- allow any import level for winsound
- add pylint

### BREAKING CHANGE

- Since Ignition 7.9 relies on Jython 2.5.3, this
  project was adapted to conform with Python 2.5.6

## v7.9.18 (2021-07-08)

### Refactor

- java.util.Date

### Feat

- **pre-commit**: update black 21.5b0 -> 21.5b1
- **pre-commit**: update flake8 3.9.1 -> 3.9.2
- **pre-commit**: update black 21.4b2 -> 21.5b0
- **pre-commit**: update black 21.4b1 -> 21.4b2
- **pre-commit**: update black 21.4b0 -> 21.4b1
- **pre-commit**: update black 20.8b1 -> 21.4b0
- **pre-commit**: bump flake8 to 3.9.1

## v7.9.17 (2021-02-12)

### Feat

- add flake8 to pre-commit hooks

## v7.9.14 (2020-09-01)
