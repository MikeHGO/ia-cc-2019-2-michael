import sys, resource
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QLabel, \
    QPushButton, QSpinBox, QAction
from PySide2.QtCore import QFile

d_p_1 = 30
d_p_0 = 50
d_r_0 = 30
d_r_1 = 50
d_r_00 = 70
d_a_0 = 50
d_a_1 = 70

p_i_1 = 30
p_i_0 = 70
p_s_0 = 30
p_s_1 = 70

def dinheiro_pouco():
    dinheiro = dinheiro_sb.value()
    if dinheiro <= d_p_1:
        return 1
    if dinheiro > d_p_1 and dinheiro < d_p_0:
        return (d_p_0-dinheiro)/(d_p_0-d_p_1)
    if dinheiro >= d_p_0:
        return 0
def dinheiro_razoavel():
    dinheiro = dinheiro_sb.value()
    if dinheiro <= d_r_0:
        return 0
    if dinheiro > d_r_0 and dinheiro < d_r_1:
        return (d_r_1-dinheiro)/(d_r_1-d_r_0)
    if dinheiro < d_r_00 and dinheiro > d_r_1:
        return (d_r_00 - dinheiro)/(d_r_00-d_r_1)
    if dinheiro >= d_r_00:
        return 0

def dinheiro_adquado():
    dinheiro = dinheiro_sb.value()
    if dinheiro <= d_a_0:
        return 0
    if dinheiro > d_a_0 and dinheiro < d_a_1:
        return (d_a_1-dinheiro)/(d_a_1-d_a_0)
    if dinheiro >= d_a_1:
        return 1

def pessoal_insuficiente():
    pessoa = pessoas_sb.value()
    if pessoa <= p_i_1:
        return 1
    if pessoa > p_i_1 and pessoa < p_i_0:
        return (p_i_0-pessoa)/(p_i_0-p_i_1)
    if pessoa >= p_i_0:
        return 0
def pessoal_satisfatorio():
    pessoa = pessoas_sb.value()
    if pessoa <= p_s_0:
        return 0
    if pessoa >= p_s_1:
        return 1
    if pessoa > p_s_0 and pessoa < p_s_1:
        return (p_s_0-pessoa)/(p_s_1-p_s_0)

def regras(vet):# RISCOS

    if(dinheiro_pouco() > pessoal_insuficiente()):
        alto = dinheiro_pouco()
    else:
        alto = pessoal_insuficiente()
    if(dinheiro_pouco() < pessoal_satisfatorio()):
        alto2 = dinheiro_pouco()
    else:
        alto2 = pessoal_satisfatorio()
    # Alto
    if(alto < alto2):
        vet[2] = alto
    else:
        vet[2] = alto2
    # Medio
    if(dinheiro_razoavel() < pessoal_satisfatorio()):
        vet[1] = dinheiro_razoavel()
    else:
        vet[1] = pessoal_satisfatorio()
    # Baixo
    if(dinheiro_adquado() < pessoal_satisfatorio()):
        vet[0] = dinheiro_adquado()
    else:
        vet[0] = pessoal_satisfatorio()

def on_calcular_pushbutton_clicked():
    intervalos = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    vet = [0, 0, 0]
    regras(vet)
    print(vet)
    numerador = 0; denominador = 0; count = 0; j = 0
    for i in intervalos:
        if(count == 3 or count == 6):
            j += 1

        count += 1
        print(i,vet[j],count)
        numerador += i*vet[j]
        denominador += vet[j]
    calc = numerador/denominador
    risco_label2.setText(str(calc))


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)

    ui_file = QFile("logica_fuzzy.ui")
    ui_file.open(QFile.ReadOnly)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()

    dinheiro_label = window.findChild(QLabel, 'dinheiroLabel')
    dinheiro_label.setVisible(True)

    pessoas_label = window.findChild(QLabel, 'pessoasLabel')
    pessoas_label.setVisible(True)

    risco_label = window.findChild(QLabel, 'riscoLabel')
    risco_label.setVisible(True)

    risco_label2 = window.findChild(QLabel, 'riscoLabel2')
    risco_label2.setVisible(True)

    dinheiro_sb = window.findChild(QSpinBox, 'dinheiroSpinBox')
    dinheiro_sb.setVisible(True)

    pessoas_sb = window.findChild(QSpinBox, 'pessoasSpinBox')
    pessoas_sb.setVisible(True)

    calcular_btn = window.findChild(QPushButton, 'calcularPushButton')
    calcular_btn.clicked.connect(on_calcular_pushbutton_clicked)

    window.show()

    sys.exit(app.exec_())