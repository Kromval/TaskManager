# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Program_project_lesson\23_2\TM23_1\Forms\mainForm\mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(816, 600)
        MainWindow.setMinimumSize(QtCore.QSize(816, 600))
        MainWindow.setMaximumSize(QtCore.QSize(816, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 204, 811, 311))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(182, 518, 411, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Z:\\Program_project_lesson\\23_2\\TM23_1\\Forms\\mainForm\\../../icons/add48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.editButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Z:\\Program_project_lesson\\23_2\\TM23_1\\Forms\\mainForm\\../../icons/edit48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editButton.setIcon(icon1)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.editButton)
        self.delButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Z:\\Program_project_lesson\\23_2\\TM23_1\\Forms\\mainForm\\../../icons/delete48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delButton.setIcon(icon2)
        self.delButton.setObjectName("delButton")
        self.horizontalLayout.addWidget(self.delButton)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 312, 201))
        self.calendarWidget.setObjectName("calendarWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(320, 0, 221, 201))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(27, 65, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(27, 95, 47, 13))
        self.label_2.setObjectName("label_2")
        self.dateEditIn = QtWidgets.QDateEdit(self.groupBox)
        self.dateEditIn.setGeometry(QtCore.QRect(85, 61, 110, 22))
        self.dateEditIn.setCalendarPopup(True)
        self.dateEditIn.setObjectName("dateEditIn")
        self.dateEditOut = QtWidgets.QDateEdit(self.groupBox)
        self.dateEditOut.setGeometry(QtCore.QRect(86, 90, 110, 22))
        self.dateEditOut.setCalendarPopup(True)
        self.dateEditOut.setObjectName("dateEditOut")
        self.filterButton = QtWidgets.QPushButton(self.groupBox)
        self.filterButton.setGeometry(QtCore.QRect(27, 125, 170, 23))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Z:\\Program_project_lesson\\23_2\\TM23_1\\Forms\\mainForm\\../../icons/filter48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filterButton.setIcon(icon3)
        self.filterButton.setObjectName("filterButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(550, 0, 251, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 50, 181, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.customerButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.customerButton.setObjectName("customerButton")
        self.verticalLayout.addWidget(self.customerButton)
        self.executorButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.executorButton.setObjectName("executorButton")
        self.verticalLayout.addWidget(self.executorButton)
        self.statusButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.statusButton.setObjectName("statusButton")
        self.verticalLayout.addWidget(self.statusButton)
        self.taskButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.taskButton.setObjectName("taskButton")
        self.verticalLayout.addWidget(self.taskButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Журнал задач"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Клиент"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Задача"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дата поступления"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Исполнитель"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Дата начала"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Срок исполнения"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Дата окончания"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Статус"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.editButton.setText(_translate("MainWindow", "Изменить"))
        self.delButton.setText(_translate("MainWindow", "Удалить"))
        self.groupBox.setTitle(_translate("MainWindow", "Фильтр по датам"))
        self.label.setText(_translate("MainWindow", "Старт"))
        self.label_2.setText(_translate("MainWindow", "Финиш"))
        self.filterButton.setText(_translate("MainWindow", "Фильтровать"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Справочники"))
        self.customerButton.setText(_translate("MainWindow", "Клиенты"))
        self.executorButton.setText(_translate("MainWindow", "Исполнители"))
        self.statusButton.setText(_translate("MainWindow", "Статусы"))
        self.taskButton.setText(_translate("MainWindow", "Задачи"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())