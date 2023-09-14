from customtkinter import W, CENTER

from helpers.event import Event
from .frame import Frame


class Form(Frame):
    onFinishEvent = Event()

    def __init__(self, master, name):
        super().__init__(master)
        self._errorLabel = self.createLabel(text_color="red")
        self._name = name
        self._isValid = False

    def __validate(self):
        ...

    def showErrorLabel(self, message):
        self._errorLabel.configure(text=message)
        self._errorLabel.pack()

    def hideErrorLabel(self):
        self._errorLabel.pack_forget()
        self._errorLabel.show()

    @property
    def isValid(self):
        return self._isValid

    @property
    def name(self):
        return self._name

    @staticmethod
    def clearCallbacks():
        Form.onFinishEvent.clear()


class FormWithOneFiled(Form):
    def __init__(self, master, name, labelText, placeholderText):
        super().__init__(master, name)
        self.__frame = Frame(self)
        self.__buttonCommitForm = self.__frame.createButton("Commit", self._onCommit, width=300)
        self.__label = self.__frame.createLabel(labelText, width=300, anchor=W)
        self.__entry = self.__frame.createEntry(placeholder_text=placeholderText, width=300)
        self.__label.pack()
        self.__entry.pack()
        self.__buttonCommitForm.pack(pady=[20, 0])
        self.__frame.pack(anchor=CENTER, expand=True)

    def _onCommit(self):
        self.__validate()
        if self._isValid:
            Form.onFinishEvent.trigger(self.__entry.get())

    def __validate(self):
        if len(self.__entry.get()) == 0:
            super().showErrorLabel(f"The <{self.__entry.cget('placeholder_text')}> field cannot be empty")
            self._isValid = False
        else:
            self._isValid = True
