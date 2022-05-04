import sys
from PyQt5.QtWidgets import QApplication,QMainWindow

from uis.UI_MainWindow import Ui_MainWindow


class AppLaunch():
    def __init__(self):
        #create window
        self.main_window = QMainWindow()

        #instantiate your main ui
        self.ui = Ui_MainWindow()

        #setup ui to the main window
        self.ui.setupUi(self.main_window)

    def showUi(self):
        self.main_window.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = AppLaunch()
    main_win.showUi()

    sys.exit(app.exec_())

