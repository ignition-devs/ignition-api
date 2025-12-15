from java.lang import Runnable as Runnable
from java.util.concurrent import Executor as Executor

class ListenableFuture:
    def addListener(self, listener: Runnable, executor: Executor) -> None: ...
