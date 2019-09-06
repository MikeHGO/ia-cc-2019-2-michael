import sys, resource
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QLabel, \
    QPushButton, QAction
from PySide2.QtCore import QFile


def on_hello_pushbutton_clicked():
    hello_label.setVisible(True)


def on_action_reset_triggered():
    hello_label.setVisible(False)


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)

    ui_file = QFile("hello_world.ui")
    ui_file.open(QFile.ReadOnly)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()

    hello_label = window.findChild(QLabel, 'helloLabel')
    hello_label.setVisible(False)

    hello_btn = window.findChild(QPushButton, 'helloPushButton')
    hello_btn.clicked.connect(on_hello_pushbutton_clicked)

    action_reset = window.findChild(QAction, 'actionReset')
    action_reset.triggered.connect(on_action_reset_triggered)

    window.show()

    sys.exit(app.exec_())