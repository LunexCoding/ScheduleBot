from customtkinter import CTkLabel

from .widget import Widget


class Label(Widget, CTkLabel):
    def __init__(self, master, text="Default", **kwargs):
        super().__init__(master, **kwargs)
        self.configure(text=text)
