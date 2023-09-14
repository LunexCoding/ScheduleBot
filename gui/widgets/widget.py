from customtkinter import CTkBaseClass


class Widget(CTkBaseClass):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self._visibility = False

    def hide(self):
        self.pack_forget()
        self._visibility = False

    def show(self, **kwargs):
        self.pack(**kwargs)
        self._visibility = True

    @property
    def visibility(self):
        return self._visibility
