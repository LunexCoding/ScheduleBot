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


class FormWithTwoFields(Form):
    def __init__(self, master, name, listTextlabels, listTextPlaceholders):
        super().__init__(master, name)
        self.__frame = Frame(self)
        self.__buttonCommitForm = self.__frame.createButton("Commit", self._onCommit, width=300)
        self.__firstLabel = self.__frame.createLabel(listTextlabels[0], width=300, anchor=W)
        self.__firstEntry = self.__frame.createEntry(placeholder_text=listTextPlaceholders[0], width=300)
        self.__secondLabel = self.__frame.createLabel(listTextlabels[1], width=300, anchor=W)
        self.__secondEntry = self.__frame.createEntry(placeholder_text=listTextPlaceholders[1], width=300)
        self.__firstLabel.pack()
        self.__firstEntry.pack(pady=[0, 10])
        self.__secondLabel.pack()
        self.__secondEntry.pack()
        self.__buttonCommitForm.pack(pady=[20, 0])
        self.__frame.pack(anchor=CENTER, expand=True)

    def _onCommit(self):
        self.__validate()
        if self._isValid:
            fields = {
                self.__firstEntry.cget('placeholder_text'): self.__firstEntry.get(),
                self.__secondEntry.cget('placeholder_text'): self.__secondEntry.get(),
            }
            Form.onFinishEvent.trigger(fields)

    def __validate(self):
        if len(self.__firstEntry.get()) == 0 and len(self.__secondEntry.get()) == 0:
            super().showErrorLabel(f"All fields must be filled")
            self._isValid = False
        elif len(self.__firstEntry.get()) == 0:
            super().showErrorLabel(f"The <{self.__firstEntry.cget('placeholder_text')}> field cannot be empty")
            self._isValid = False
        elif len(self.__secondEntry.get()) == 0:
            super().showErrorLabel(f"The <{self.__secondEntry.cget('placeholder_text')}> field cannot be empty")
            self._isValid = False
        else:
            self._isValid = True
