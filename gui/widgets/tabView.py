from customtkinter import CTkTabview

from .widget import Widget
from .frame import Frame
from .forms import FormWithOneFiled, FormWithTwoFields


class TabView(Widget, CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def createFrame(self, master, **kwargs):
        return Frame(
            master=self.tab(master),
            **kwargs
        )

    def createFormWithOneFiled(self, labelText, placeholderText):
        return FormWithOneFiled(
            master=self.tab("Input"),
            labelText=labelText,
            placeholderText=placeholderText
        )

    def createFormWithTwoFields(self, labelTexts, placeholderTexts):
        return FormWithTwoFields(
            master=self.tab("Input"),
            labelText=labelTexts,
            placeholderText=placeholderTexts
        )
