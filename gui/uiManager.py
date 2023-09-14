from helpers.event import Event


class UIManager:
    onButtonSetGroupClicked = Event()
    onButtonShowScheduleForRequiredGroupClicked = Event()
    onButtonShowScheduleForAllGroupsClicked = Event()

    def __init__(self, window):
        self.__window = window

        self.__window.onButtonSetGroup += self._onButtonSetGroupClicked
        self.__window.onButtonShowScheduleForRequiredGroup += self._onButtonShowScheduleForRequiredGroupClicked
        self.__window.onButtonShowScheduleForAllGroups += self._onButtonShowScheduleForAllGroupsClicked

    def run(self):
        self.__window.mainloop()

    @staticmethod
    def _onButtonSetGroupClicked():
        UIManager.onButtonSetGroupClicked.trigger()

    @staticmethod
    def _onButtonShowScheduleForRequiredGroupClicked(path):
        UIManager.onButtonShowScheduleForRequiredGroupClicked.trigger(path)

    @staticmethod
    def _onButtonShowScheduleForAllGroupsClicked(path):
        UIManager.onButtonShowScheduleForAllGroupsClicked.trigger(path)
