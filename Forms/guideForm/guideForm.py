# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Program_project_lesson\23_2\TM23_1\Forms\guideForm\guideForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_guideForm(object):
    def setupUi(self, guideForm):
        guideForm.setObjectName("guideForm")
        guideForm.setWindowModality(QtCore.Qt.ApplicationModal)
        guideForm.resize(400, 300)
        guideForm.setWindowTitle("")
        self.label = QtWidgets.QLabel(guideForm)
        self.label.setGeometry(QtCore.QRect(94, 10, 201, 20))
        self.label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(guideForm)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 381, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(guideForm)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(95, 259, 211, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.saveButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Z:\\Program_project_lesson\\23_2\\TM23_1\\Forms\\guideForm\\../../icons/save48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Z:\\Program_project_lesson\\23_2\\TM23_1\\Forms\\guideForm\\../../icons/delete48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)

        self.retranslateUi(guideForm)
        QtCore.QMetaObject.connectSlotsByName(guideForm)

    def retranslateUi(self, guideForm):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("guideForm", "Клиенты"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("guideForm", "Наименование"))
        self.saveButton.setText(_translate("guideForm", "Сохранить"))
        self.pushButton_4.setText(_translate("guideForm", "Отмена"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    guideForm = QtWidgets.QDialog()
    ui = Ui_guideForm()
    ui.setupUi(guideForm)
    guideForm.show()
    sys.exit(app.exec_())
