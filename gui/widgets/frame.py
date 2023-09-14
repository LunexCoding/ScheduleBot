from customtkinter import CTkFrame, CTkButton, CTkEntry
from .CTkTable import CTkTable

from .label import Label
from .widget import Widget


class Frame(Widget, CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def reload(self, **kwargs):
        if self._visibility:
            self.clear()
        if not self._visibility:
            self.show(**kwargs)

    def createButton(self, text, func, **kwargs):
        return CTkButton(
            master=self,
            text=text,
            command=func,
            **kwargs
        )

    def createLabel(self, text="Default", **kwargs):
        return Label(
            master=self,
            text=text,
            **kwargs
        )

    def createEntry(self, **kwargs):
        return CTkEntry(
            master=self,
            **kwargs
        )

    def createTable(self, values, **kwargs):
        return CTkTable(
            master=self,
            values=values,
            **kwargs
        )

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()
