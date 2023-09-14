from helpers.event import Event


class UIManager:
    onButtonShowScheduleForRequiredGroupClicked = Event()
    onButtonShowScheduleForAllGroupsClicked = Event()

    def __init__(self, window):
        self.__window = window

        self.__window.onButtonShowScheduleForRequiredGroup += self._onButtonShowScheduleForRequiredGroupClicked
        self.__window.onButtonShowScheduleForAllGroups += self._onButtonShowScheduleForAllGroupsClicked

    def run(self):
        self.__window.mainloop()

    @staticmethod
    def _onButtonShowScheduleForRequiredGroupClicked(group):
        UIManager.onButtonShowScheduleForRequiredGroupClicked.trigger(group)

    @staticmethod
    def _onButtonShowScheduleForAllGroupsClicked():
        UIManager.onButtonShowScheduleForAllGroupsClicked.trigger()
