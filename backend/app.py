from gui.uiManager import UIManager
from gui.mainWindow import MainWindow
from backend.schedule import g_scheduleParser


class App:
    SCHEDULE_TABLE_HEADERS_FOR_REQUIRED_GROUP = [["Lesson", "Time", "Discipline", "Teacher", "Cabinet"]]
    SCHEDULE_TABLE_HEADERS_FOR_ALL_GROUPS = [["Group", "Lesson", "Time", "Discipline", "Teacher", "Cabinet"]]
    def __init__(self):
        self.__window = MainWindow()
        self._ui_manager = UIManager(self.__window)

        self._ui_manager.onButtonShowScheduleForRequiredGroupClicked += self._onButtonShowScheduleForRequiredGroupClicked
        self._ui_manager.onButtonShowScheduleForAllGroupsClicked += self._onButtonShowScheduleForAllGroupsClicked

    def _onButtonShowScheduleForRequiredGroupClicked(self, group):
        items = self.SCHEDULE_TABLE_HEADERS_FOR_REQUIRED_GROUP.copy()
        if not group in g_scheduleParser.groups:
            return self.__window.showErrorMessageBox(
                title=f"Group {group}",
                message=f"Group <{group}> not found!"
            )
        g_scheduleParser.setGroup(group)
        for lesson in g_scheduleParser.getLessons():
            items.append([data for data in lesson.values()])
        self.__window.displayScheduleTable(items)

    def _onButtonShowScheduleForAllGroupsClicked(self):
        items = self.SCHEDULE_TABLE_HEADERS_FOR_REQUIRED_GROUP.copy()
        for groupData in g_scheduleParser.getScheduleForAllGroups():
            if groupData["lessons"] != "Выходной":
                for lesson in groupData["lessons"]:
                    data = [groupData["group"]]
                    data.extend([data for data in lesson.values()])
                    items.append(data)
            else:
                data = [groupData["group"]]
                data.extend(["Выходной" for num in range(len(self.SCHEDULE_TABLE_HEADERS_FOR_ALL_GROUPS[0]) - 1)])
                items.append(data)
        self.__window.displayScheduleTable(items)

    def run(self):
        self._ui_manager.run()
