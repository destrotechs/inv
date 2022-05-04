import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QTableWidgetItem,QPushButton

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
        self.editbtn = QPushButton()
        self.editbtn.setText("edit")
        self.ui.items_table.setRowCount(10)
        self.ui.items_table.setColumnCount(8)


        self.ui.items_table.setHorizontalHeaderLabels(["Name", "Job", "Email"])
        self.ui.items_table.setItem(0,0,QTableWidgetItem('Name'))
        self.ui.items_table.setItem(0,1,QTableWidgetItem('City'))
        self.ui.items_table.setItem(0,2,QTableWidgetItem('Street'))

        self.ui.stackedWidget.setCurrentWidget(self.ui.items)

    def showSales(self):
        data = {'col1':['1','2','3','4'],
        'col2':['1','2','1','3'],
        'col3':['1','1','2','1']}

        self.ui.sales_table.setRowCount(10)
        self.ui.sales_table.setColumnCount(8)

        self.ui.sales_table.setItem(0,0,QTableWidgetItem('Name'))
        self.ui.sales_table.setItem(0,1,QTableWidgetItem('City'))
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

