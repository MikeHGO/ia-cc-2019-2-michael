import sys, resource
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QRadioButton, QPlainTextEdit
from PySide2.QtCore import QFile


def on_treinar_pushbutton_clicked():
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
    hebb_radio.setVisible(True)

    perceptron_radio = window.findChild(QRadioButton, 'perceptronRadioButton')
    perceptron_radio.setVisible(True)

    # label interface
    treinamento_label = window.findChild(QLabel, 'treinamentoLabel')
    treinamento_label.setVisible(True)

    teste_label = window.findChild(QLabel, 'testeLabel')
    teste_label.setVisible(True)

    pesos_label = window.findChild(QLabel, 'testeLabel_2')
    pesos_label.setVisible(True)

    saida_label = window.findChild(QLabel, 'saidaLabel')
    saida_label.setVisible(True)

    p1_label = window.findChild(QLabel, 'p1Label')
    p1_label.setVisible(True)

    p2_label = window.findChild(QLabel, 'p2Label')
    p2_label.setVisible(True)

    pB_label = window.findChild(QLabel, 'pBLabel')
    pB_label.setVisible(True)

    # saidas...
    peso1_label = window.findChild(QLabel, 'peso1Label')
    peso1_label.setVisible(True)

    peso2_label = window.findChild(QLabel, 'peso2Label')
    peso2_label.setVisible(True)

    pesoB_label = window.findChild(QLabel, 'pesoBLabel')
    pesoB_label.setVisible(True)

    resposta_label = window.findChild(QLabel, 'respostaLabel')
    resposta_label.setVisible(True)
    # entradas
    treinamento_plainText = window.findChild(QPlainTextEdit, 'treinamentoPlainTextEdit')
    treinamento_plainText.setVisible(True)

    teste_lineEdit = window.findChild(QPlainTextEdit, 'testeLineEdit')
    teste_lineEdit.setVisible(True)
    # botoes
    treinar_btn = window.findChild(QPushButton, 'treinamentoPushButton')
    treinar_btn.clicked.connect(on_treinar_pushbutton_clicked)

    testar_btn = window.findChild(QPushButton, 'testePushButton')
    testar_btn.clicked.connect(on_testar_pushbutton_clicked)

    window.show()
    sys.exit(app.exec_())