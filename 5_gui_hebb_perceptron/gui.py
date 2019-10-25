import sys
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QRadioButton, QPlainTextEdit, QMessageBox
from PySide2.QtCore import QFile
from hebb import Hebb
from perceptron import Perceptron
from neuron import Neuron

# 1 1 1 1
# 1 -1 1 -1
# -1 1 1 -1
# -1 -1 1 -1

neurinho = Neuron()

def hebb_split(texto):
    split_1 = texto.split("\n")
    split_2 = []
    for i in range(len(split_1)):
        floats = [float(x) for x in split_1[i].split()]
        target = floats[-1]
        floats.pop()
        tupleAux = (floats, target)
        split_2.append(tupleAux)
    return split_2

def perceptron_split(texto):
    split_1 = texto.split("\n")
    split_2 = []
    alpha_theta = []
    for i in range(len(split_1)):
        floats = [float(x) for x in split_1[i].split()]
        if(i < len(split_1) - 2):
            target = floats[-1]
            floats.pop()
            tupleAux = (floats, target)
            split_2.append(tupleAux)
        else:
            alpha_theta.append(floats[0])
    return [split_2, alpha_theta[0], alpha_theta[1]]

def hebb_setPesos():
    entradas = Hebb(hebb_split(treinamento_plainText.toPlainText()))
    lista_pesos = entradas.passo_n()
    neurinho.entradas = hebb_split(treinamento_plainText.toPlainText())
    neurinho.lista_pesos = lista_pesos
    p1_label.setText("{: f}".format(lista_pesos[0]))
    p2_label.setText("{: f}".format(lista_pesos[1]))
    pB_label.setText("{: f}".format(lista_pesos[2]))
    return

def perceptron_setPesos():
    entradas = perceptron_split(treinamento_plainText.toPlainText())
    neuron_perceptron = Perceptron(entradas[0], entradas[1], entradas[2])
    lista_pesos = neuron_perceptron.passo_n()
    neurinho.entradas = entradas
    neurinho.lista_pesos = lista_pesos
    p1_label.setText("{: f}".format(lista_pesos[0]))
    p2_label.setText("{: f}".format(lista_pesos[1]))
    pB_label.setText("{: f}".format(lista_pesos[2]))

def on_treinar_pushbutton_clicked():
    if treinamento_plainText.toPlainText() == "":
        QMessageBox.warning(QMessageBox(), "AVISO", "Forneca uma entrada")
        return
    if hebb_radio.isChecked():
        hebb_setPesos()
    elif perceptron_radio.isChecked():
        perceptron_setPesos()
    else:
        QMessageBox.warning(QMessageBox(), "AVISO", "Escolha um metodo")
        return
    teste_lineEdit.setFocus()
    return 1

def on_testar_pushbutton_clicked():

    if p1_label.text() == "":
        QMessageBox.warning(QMessageBox(), "AVISO", "Execute o treinamento")
        teste_lineEdit.clear()
        treinamento_plainText.setFocus()
        return
    if hebb_radio.isChecked():
        resposta_label.setText(str(neurinho.h_saida([float(x) for x in teste_lineEdit.text().split()])))
        return
    elif perceptron_radio.isChecked():
        resposta_label.setText(str(neurinho.p_saida([float(x) for x in teste_lineEdit.text().split()], neurinho.entradas[2])))
        return
    return


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

    peso1_label = window.findChild(QLabel, 'peso1Label')

    peso2_label = window.findChild(QLabel, 'peso2Label')

    pesoB_label = window.findChild(QLabel, 'pesoBLabel')

    # saidas...

    p1_label = window.findChild(QLabel, 'p1Label')

    p2_label = window.findChild(QLabel, 'p2Label')

    pB_label = window.findChild(QLabel, 'pBLabel')

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