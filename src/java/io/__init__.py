from __future__ import print_function

__all__ = ["Closeable"]

from java.lang import AutoCloseable


class Closeable(AutoCloseable):
    def close(self):
        # type: () -> None
        raise NotImplementedError
