from typing import List, Optional

LANDSCAPE: int
PORTRAIT: int

def getDefaultPrinterName() -> Optional[unicode]: ...
def getPrinterNames() -> List[unicode]: ...
