from java.awt import Container
from java.lang import String


class JTextComponent(Container):
    _text = "Text"  # type: String

    def getText(self):
        # type: () -> String
        return self._text

    def setText(self, t):
        # type: (String) -> None
        self._text = t
