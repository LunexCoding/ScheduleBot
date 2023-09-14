from gui.uiManager import UIManager
from gui.mainWindow import MainWindow


class App:
    def __init__(self):
        self.__window = MainWindow()
        self._ui_manager = UIManager(self.__window)

        self._ui_manager.onButtonSetGroupClicked += self._onButtonSetGroupClicked
        self._ui_manager.onButtonShowScheduleForRequiredGroupClicked += self._onButtonShowScheduleForRequiredGroupClicked
        self._ui_manager.onButtonShowScheduleForAllGroupsClicked += self._onButtonShowScheduleForAllGroupsClicked

    def _onButtonSetGroupClicked(self):
        ...

    def _onButtonShowScheduleForRequiredGroupClicked(self):
        ...

    def _onButtonShowScheduleForAllGroupsClicked(self):
        ...

    def run(self):
        self._ui_manager.run()
