from java.lang import Runnable
from java.util.concurrent import Executor


class ListenableFuture(object):
    def addListener(self, listener, executor):
        # type: (Runnable, Executor) -> None
        pass
