# ignition-api-stubs

<!--- Badges --->
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ignition-api-stubs)](https://pypi.org/project/ignition-api-stubs/)
[![PyPI - Version](https://img.shields.io/pypi/v/ignition-api-stubs)](https://pypi.org/project/ignition-api-stubs/)
[![PyPI - Downloads](https://pepy.tech/badge/ignition-api-stubs)](https://pepy.tech/project/ignition-api-stubs)
[![ignition-api-stubs](https://snyk.io/advisor/python/ignition-api-stubs/badge.svg)](https://snyk.io/advisor/python/ignition-api-stubs)
[![ci](https://github.com/ignition-devs/ignition-api/actions/workflows/ci.yml/badge.svg?branch=8.3)](https://github.com/ignition-devs/ignition-api/actions/workflows/ci.yml)
[![Join us on GitHub discussions](https://img.shields.io/badge/github-discussions-informational)](https://github.com/orgs/ignition-devs/discussions)

This package contains a collection of [stubs] for [`ignition-api-8.3`]. These
files were generated using `mypy`'s [`stubgen`].

## Installation and usage

To use ignition-api-stubs, you may install it with `pip`. It requires Python
3.7+ through 3.12.

> [!WARNING]
> Python 3.13 will not be supported.

```sh
python3 -m pip install ignition-api-stubs
```

To run `mypy` against your code, execute the following command passing the
source directory (typically `src`) or a single file:

> [!NOTE]
> Ensure you have installed [`mypy`] before running the commands
> below.

```sh
python3 -m pip install "mypy[python2]==0.971"
```

Then

```sh
mypy --py2 src
```

Or

```sh
mypy --py2 code.py
```

## Contributing

See [CONTRIBUTING.md].

## Discussions

Feel free to post your questions and/or ideas at [Discussions].

## Contributors

Thanks to everyone who has contributed to this project.

Up-to-date list of [contributors].

## License

See the [LICENSE].

## Code of conduct

See [CODE_OF_CONDUCT.md].

<!-- Links -->
[CODE_OF_CONDUCT.md]: https://github.com/ignition-devs/.github/blob/main/CODE_OF_CONDUCT.md
[CONTRIBUTING.md]: https://github.com/ignition-devs/ignition-api-8.3/blob/main/CONTRIBUTING.md
[contributors]: https://github.com/ignition-devs/ignition-api-8.3-stubs/graphs/contributors
[Discussions]: https://github.com/orgs/ignition-devs/discussions
[`ignition-api-8.3`]: https://github.com/ignition-devs/ignition-api-8.3
[LICENSE]: https://github.com/ignition-devs/ignition-api-8.3/blob/main/LICENSE
[`mypy`]: https://coatl-mypy.readthedocs.io/en/v0.971/
[`stubgen`]: https://coatl-mypy.readthedocs.io/en/v0.971/stubgen.html
[stubs]: https://www.python.org/dev/peps/pep-484/
