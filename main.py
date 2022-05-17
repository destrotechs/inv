from os import system
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QPushButton,
    QMessageBox,
    QTableView,
    QTableWidget,
    QHeaderView,
)
from db.base import *
from uis.UI_MainWindow import Ui_MainWindow
from uis.UI_NewCategory import Ui_Form


class AppLaunch:
    def __init__(self):
        # create window
        self.main_window = QMainWindow()

        # instantiate your main ui
        self.ui = Ui_MainWindow()

        # setup ui to the main window
        self.ui.setupUi(self.main_window)
        # set default widget
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        # listen for menu button clicks
        self.ui.items_btn.clicked.connect(self.showItems)
        self.ui.sales_btn.clicked.connect(self.showSales)
        self.ui.categories_btn.clicked.connect(self.showCategories)
        self.ui.stock_btn.clicked.connect(self.showStock)
        self.ui.reports_btn.clicked.connect(self.showReports)

        # add buttons
        self.ui.add_caegory_btn.clicked.connect(self.showaddcategory)

    def showUi(self):
        self.main_window.show()

    # click handlers
    def showItems(self):
        for i in reversed(range(self.ui.items_layout.count())):
            self.ui.items_layout.itemAt(i).widget().setParent(None)

        db = Base()
        db.db_connect()

        records = db.get_records("items")

        self.table = QTableWidget()

        self.table.setRowCount(len(records))
        self.table.setColumnCount(4)

        self.table.setHorizontalHeaderLabels(
            ["ITEM CODE", "CATEGORY", "NAME", "DESCRIPTION"]
        )
        rows = 0

        for record in records:
            self.table.setItem(rows, 0, QTableWidgetItem(str(record[0])))
            self.table.setItem(rows, 1, QTableWidgetItem(str(record[1])))
            self.table.setItem(rows, 2, QTableWidgetItem(str(record[2])))
            self.table.setItem(rows, 3, QTableWidgetItem(str(record[3])))

            rows + 1
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)

        self.ui.items_layout.addWidget(self.table)

        self.ui.stackedWidget.setCurrentWidget(self.ui.items)

    def showSales(self):
        self.ui.sales_table.setRowCount(10)
        self.ui.sales_table.setColumnCount(8)

        self.ui.sales_table.setItem(0, 0, QTableWidgetItem("Name"))
        self.ui.sales_table.setItem(0, 1, QTableWidgetItem("City"))
        self.ui.stackedWidget.setCurrentWidget(self.ui.sales)

    def showCategories(self):
        for i in reversed(range(self.ui.categories_layout.count())):
            self.ui.categories_layout.itemAt(i).widget().setParent(None)
        db = Base()
        db.db_connect()

        records = db.get_records("item_categories")

        print("RECORDS==========", records)

        self.table = QTableWidget()
        self.table.setRowCount(len(records) + 2)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["CODE", "NAME", "DESCRIPTION"])

        rows = 0
        for record in records:
            self.table.setItem(rows, 0, QTableWidgetItem(str(record[0])))
            self.table.setItem(rows, 1, QTableWidgetItem(str(record[1])))
            self.table.setItem(rows, 2, QTableWidgetItem(str(record[2])))

            rows = rows + 1

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        self.ui.categories_layout.addWidget(self.table)

        self.ui.stackedWidget.setCurrentWidget(self.ui.categories)

    def showStock(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stock)

    def showReports(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.reports)

    def showaddcategory(self):
        self.form = Ui_Form()
        self.form.show()


def createConnection():
    conn = Base()

    if conn.db_connect() != True:
        QMessageBox.critical(
            None,
            "Error!",
            "Database Error: %s" % conn.db_connect(),
        )
        return False
    print("Connected....")
    return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    connected = createConnection()
    if not connected:
        sys.exit(1)
    main_win = AppLaunch()
    main_win.showUi()

    sys.exit(app.exec_())
