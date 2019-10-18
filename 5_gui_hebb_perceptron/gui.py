import sys
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QRadioButton, QPlainTextEdit, QMessageBox
from PySide2.QtCore import QFile

def on_treinar_pushbutton_clicked():

    msg = QMessageBox.warning(QMessageBox(), "AVISO", "Escolha um metodo")

    if hebb_radio.isChecked():
        resposta_label.setText("1")
    teste_lineEdit.setFocus()
    return 1

def on_testar_pushbutton_clicked():
    return 1


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)

    ui_file = QFile("hebb_perceptron.ui")
    ui_file.open(QFile.ReadOnly)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()

    # radio button
    hebb_radio = window.findChild(QRadioButton, 'hebbRadioButton')

    perceptron_radio = window.findChild(QRadioButton, 'perceptronRadioButton')

    # label interface
    treinamento_label = window.findChild(QLabel, 'treinamentoLabel')

    teste_label = window.findChild(QLabel, 'testeLabel')

    pesos_label = window.findChild(QLabel, 'testeLabel_2')

    saida_label = window.findChild(QLabel, 'saidaLabel')

    p1_label = window.findChild(QLabel, 'p1Label')

    p2_label = window.findChild(QLabel, 'p2Label')

    pB_label = window.findChild(QLabel, 'pBLabel')

    # saidas...
    peso1_label = window.findChild(QLabel, 'peso1Label')

    peso2_label = window.findChild(QLabel, 'peso2Label')

    pesoB_label = window.findChild(QLabel, 'pesoBLabel')

    resposta_label = window.findChild(QLabel, 'respostaLabel')

    # entradas
    treinamento_plainText = window.findChild(QPlainTextEdit, 'treinamentoPlainTextEdit')

    teste_lineEdit = window.findChild(QLineEdit, 'testeLineEdit')

    # botoes
    treinar_btn = window.findChild(QPushButton, 'treinamentoPushButton')
    treinar_btn.clicked.connect(on_treinar_pushbutton_clicked)

    testar_btn = window.findChild(QPushButton, 'testePushButton')
    testar_btn.clicked.connect(on_testar_pushbutton_clicked)

    window.show()
    sys.exit(app.exec_())