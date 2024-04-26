from PyQt5.QtWidgets import QMessageBox


def delRecordOnClick():
    msg = QMessageBox()
    msg.setWindowTitle('Вопрос')
    msg.setText('Вы уверены в удалении записи?')
    msg.setIcon(QMessageBox.Question)
    okButton = msg.addButton('Да', QMessageBox.ButtonRole.YesRole)
    noButton = msg.addButton('Нет', QMessageBox.ButtonRole.NoRole)

    msg.exec_()

    if msg.clickedButton() == okButton:
        print('Да')

    if msg.clickedButton() == noButton:
        print('Нет')