# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/destro/projects/python/INVENTORY/uis/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(995, 819)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.sales_btn = QtWidgets.QPushButton(self.groupBox)
        self.sales_btn.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: rgb(255, 255, 255);")
        self.sales_btn.setObjectName("sales_btn")
        self.verticalLayout_3.addWidget(self.sales_btn)
        self.items_btn = QtWidgets.QPushButton(self.groupBox)
        self.items_btn.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: rgb(255, 255, 255);")
        self.items_btn.setObjectName("items_btn")
        self.verticalLayout_3.addWidget(self.items_btn)
        self.categories_btn = QtWidgets.QPushButton(self.groupBox)
        self.categories_btn.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: rgb(255, 255, 255);")
        self.categories_btn.setObjectName("categories_btn")
        self.verticalLayout_3.addWidget(self.categories_btn)
        self.stock_btn = QtWidgets.QPushButton(self.groupBox)
        self.stock_btn.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: rgb(255, 255, 255);")
        self.stock_btn.setObjectName("stock_btn")
        self.verticalLayout_3.addWidget(self.stock_btn)
        self.reports_btn = QtWidgets.QPushButton(self.groupBox)
        self.reports_btn.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"color: rgb(255, 255, 255);")
        self.reports_btn.setObjectName("reports_btn")
        self.verticalLayout_3.addWidget(self.reports_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox)
        self.stackedWidget.setObjectName("stackedWidget")
        self.categories = QtWidgets.QWidget()
        self.categories.setObjectName("categories")
        self.label_2 = QtWidgets.QLabel(self.categories)
        self.label_2.setGeometry(QtCore.QRect(380, 250, 131, 41))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.categories)
        self.stock = QtWidgets.QWidget()
        self.stock.setObjectName("stock")
        self.label_3 = QtWidgets.QLabel(self.stock)
        self.label_3.setGeometry(QtCore.QRect(350, 230, 101, 21))
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.stock)
        self.reports = QtWidgets.QWidget()
        self.reports.setObjectName("reports")
        self.label_4 = QtWidgets.QLabel(self.reports)
        self.label_4.setGeometry(QtCore.QRect(370, 390, 67, 17))
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.reports)
        self.items = QtWidgets.QWidget()
        self.items.setObjectName("items")
        self.label_5 = QtWidgets.QLabel(self.items)
        self.label_5.setGeometry(QtCore.QRect(340, 390, 67, 17))
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.items)
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.label = QtWidgets.QLabel(self.home)
        self.label.setGeometry(QtCore.QRect(350, 240, 101, 51))
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.home)
        self.sales = QtWidgets.QWidget()
        self.sales.setObjectName("sales")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.sales)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.sales)
        self.pushButton.setStyleSheet("background-color: rgb(32, 74, 135);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Ubuntu Mono\";\n"
"padding:10px;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.line = QtWidgets.QFrame(self.sales)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.treeWidget = QtWidgets.QTreeWidget(self.sales)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.verticalLayout_7.addWidget(self.treeWidget)
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_6.setStretch(1, 1)
        self.verticalLayout_6.setStretch(2, 5)
        self.gridLayout_4.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.sales)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "INVENTORY SYSTEM"))
        self.groupBox.setTitle(_translate("MainWindow", "MENU"))
        self.sales_btn.setText(_translate("MainWindow", "SALES"))
        self.items_btn.setText(_translate("MainWindow", "ITEMS"))
        self.categories_btn.setText(_translate("MainWindow", "CATEGORIES"))
        self.stock_btn.setText(_translate("MainWindow", "STOCK"))
        self.reports_btn.setText(_translate("MainWindow", "REPORTS"))
        self.label_2.setText(_translate("MainWindow", "categories"))
        self.label_3.setText(_translate("MainWindow", "Stock"))
        self.label_4.setText(_translate("MainWindow", "Reports"))
        self.label_5.setText(_translate("MainWindow", "Items"))
        self.label.setText(_translate("MainWindow", "HOME PAGE"))
        self.pushButton.setText(_translate("MainWindow", "NEW SALE"))
