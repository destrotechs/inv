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
        #set default widget
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        #listen for menu button clicks
        self.ui.items_btn.clicked.connect(self.showItems)
        self.ui.sales_btn.clicked.connect(self.showSales)
        self.ui.categories_btn.clicked.connect(self.showCategories)
        self.ui.stock_btn.clicked.connect(self.showStock)
        self.ui.reports_btn.clicked.connect(self.showReports)

        

    def showUi(self):
        self.main_window.show()
    

    #click handlers
    def showItems(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.items)

    def showSales(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.sales)
    
    def showCategories(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.categories)
    
    def showStock(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stock)
    
    def showReports(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.reports)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = AppLaunch()
    main_win.showUi()

    sys.exit(app.exec_())

