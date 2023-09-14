from customtkinter import (
    CTk,
    BOTH,
    BOTTOM,
    LEFT,
    CENTER,
    X,
    Y,
    set_appearance_mode,
    set_default_color_theme,
    CTkFont
)
from CTkMessagebox import CTkMessagebox

from helpers.event import Event
from gui.widgets.frame import Frame
from gui.widgets.tabView import TabView
from gui.widgets.forms import FormWithOneFiled, FormWithTwoFields


class MainWindow(CTk):
    onButtonSetGroup = Event()
    onButtonShowScheduleForRequiredGroup = Event()
    onButtonShowScheduleForAllGroups = Event()

    def __init__(self, title="ScheduleBot", geometry="600x600"):
        super().__init__()
        set_appearance_mode("dark")
        set_default_color_theme("blue")
        self.title(title)
        self.geometry(geometry)
        self.minsize(500, 300)
        self._createUIEelements()

        self.__form = None
        self.__currentOperation = None

    def _createUIEelements(self):
        self.__mainFrame = self.__createFrame(self)
        self.__buttonsFrame = self.__createFrame(self.__mainFrame, fg_color="green")

        self.__onButtonSetGroup = self.__buttonsFrame.createButton('Show date', self.__onButtonSetGroupClicked)
        self.__onButtonShowScheduleForRequiredGroup = self.__buttonsFrame.createButton('List dir', self.__onButtonShowScheduleForRequiredGroup)
        self.__onButtonShowScheduleForAllGroups = self.__buttonsFrame.createButton('Create dir', self.__onButtonShowScheduleForAllGroups)
        self.__onButtonSetGroup.pack(pady=[0, 20], fill=BOTH, expand=True)
        self.__onButtonShowScheduleForRequiredGroup.pack(pady=[0, 20], fill=BOTH, expand=True)
        self.__onButtonShowScheduleForAllGroups.pack(pady=[0, 20], fill=BOTH, expand=True)

        self.__footerFrame = self.__createFrame(self, fg_color="blue")
        self.__copyrightLabel = self.__footerFrame.createLabel("Copyright LunexCoding",
                                                               font=CTkFont("Helvetica", 18, "bold"))
        self.__copyrightLabel.pack(side=LEFT, padx=25)

        self.__tabView = self.__createTabView(self.__mainFrame, fg_color="red")
        self.__tabView.add("Input")
        self.__tabView.add("Output")
        self.__formFrame = self.__tabView.createFrame("Input", fg_color="green")
        self.__dataFrame = self.__tabView.createFrame("Output", fg_color="green")

        self.__buttonsFrame.show(fill=Y, side=LEFT, ipadx=20)
        self.__footerFrame.show(fill=X, side=BOTTOM)
        self.__mainFrame.show(anchor=CENTER, fill=BOTH, expand=True)
        self.__tabView.show(anchor=CENTER, fill=BOTH, padx=[30, 20], pady=[0, 20], expand=True)

    def __createFrame(self, master, **kwargs):
        return Frame(master, **kwargs)

    def __createTabView(self, master, **kwargs):
        return TabView(master, **kwargs)

    def __reloadFormCallbacks(self, operation):
        if self.__form is not None:
            if self.__form.name != operation:
                self.__form.clearCallbacks()

    def __onButtonSetGroupClicked(self):
        operation = "SetGroup"
        self.__formFrame.reload(anchor=CENTER, expand=True)
        self.__reloadFormCallbacks(operation)
        self.__form = FormWithOneFiled(
            master=self.__formFrame,
            name=operation,
            labelText="Enter group number",
            placeholderText="For example 07.09.10"
        )
        def onFormFinished(group):
            if self.__form.isValid:
                self.__onButtonSetGroup(group)

        self.__form.onFinishEvent += onFormFinished
        self.__form.show()
        self.__tabView.set("Input")

    def __onButtonShowScheduleForRequiredGroup(self):
        operation = "ShowScheduleForRequiredGroup"

    def __onButtonShowScheduleForAllGroups(self):
        operation = "ShowScheduleForAllGroups"

    def displayScheduleTable(self, values):
        self.__dataFrame.reload(anchor=CENTER, fill=BOTH, expand=True)
        table = self.__dataFrame.createTable(values, hover=True)
        table.pack(anchor=CENTER, fill=BOTH, expand=True)
        self.__tabView.set("Output")

    @staticmethod
    def showCheckmarkMessageBox(title, message, **kwargs):
        CTkMessagebox(title=title, message=message, icon="check", **kwargs)

    @staticmethod
    def showErrorMessageBox(title, message, **kwargs):
        CTkMessagebox(title=title, message=message, icon="cancel", **kwargs)

    @staticmethod
    def showWarningMessageBox(title, message, **kwargs):
        message = CTkMessagebox(title=title, message=message, icon="warning", **kwargs)
        response = message.get()
        return response

    @staticmethod
    def _onButtonSetGroupClicked():
        MainWindow.onButtonSetGroup.trigger()

    @staticmethod
    def _onButtonShowScheduleForRequiredGroupClicked(path):
        MainWindow.onButtonShowScheduleForRequiredGroup.trigger(path)

    @staticmethod
    def _onButtonShowScheduleForAllGroupsClicked(path):
        MainWindow.onButtonShowScheduleForAllGroups.trigger(path)
