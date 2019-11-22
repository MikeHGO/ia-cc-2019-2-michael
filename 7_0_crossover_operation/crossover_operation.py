import sys, random
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtWidgets import QApplication, QComboBox, \
    QPushButton, QLineEdit, QLabel, QMessageBox


def compare_str(str_n, check, changes):
    str_list = list(str_n)
    check_list = list(check)
    changes_list = list(changes)
    n = 0

    for i in range(len(str_list)):
        for j in range(len(check_list)):
            if n > (len(check_list) - 1) or i > (len(str_list)-1) or j > (len(check_list)-1) : continue
            elif (str_list[i] == check_list[j]):
                str_list[i] = changes_list[n]
                del (check_list[j])
                del (changes_list[n])
                n += 1

    str_n = "".join(str_list)
    check = "".join(check_list)
    changes = "".join(changes_list)
    return str_n, check, changes

def compare_changes(str_n, check):
    str_list = list(str_n)
    check_list = list(check)
    n = 0

    for i in range(len(str_list)):
        for j in range(len(check_list)):
            if n > (len(check_list) - 1) or i > (len(str_list)-1) or j > (len(check_list)-1) : continue
            elif (str_list[i] == check_list[j]):
                del (check_list[j])
                del (str_list[i])

    str_n = "".join(str_list)
    check = "".join(check_list)
    return str_n, check

def on_cross_pushbutton_clicked():
    if len(father_line_edit.text()) != 10 or len(father_line_edit.text()) != 10:
        QMessageBox.warning(QMessageBox(), "AVISO", "Entrada deve conter 10 caracteres")
        return

    if method_combo_box.currentText() == "Corte Simples":
        offsprings = simple_cut_crossover(1)
        # son1_label_3.setVisible(False)
        # son2_label_3.setVisible(False)
        son1_label_3.setText("")
        son2_label_3.setText("")
    elif method_combo_box.currentText() == "Corte Duplo":
        offsprings = simple_cut_crossover(2)
    elif method_combo_box.currentText() == "PMX":
        if len(father_line_edit.text()) != len(set(father_line_edit.text())) \
                or len(mother_line_edit.text()) != len(set(mother_line_edit.text())):
            QMessageBox.warning(QMessageBox(), "AVISO", "Entrada deve conter valores unicos")
            return
        offsprings = pmx_crossover()

def on_method_combobox_current_text_changed():
    if method_combo_box.currentText() == "PMX":
        father_line_edit.setInputMask("AAAAAAAAAA")
        mother_line_edit.setInputMask("AAAAAAAAAA")
        father_line_edit.setText("ABCDEFGHIJ")
        mother_line_edit.setText("KLMNOPQRST")
    else:
        father_line_edit.setInputMask("BBBBBBBBBB")
        mother_line_edit.setInputMask("BBBBBBBBBB")
        father_line_edit.setText("0000000000")
        mother_line_edit.setText("1111111111")

def pmx_crossover():
    cuts = 2
    # cuts: quantidade de cortes
    # trades: quantidade de trocas
    trades = 1

    papa = father_line_edit.text()
    mama = mother_line_edit.text()

    # parts: vetor de numeros aleatorios
    # que indicam onde os cortes serao feitos
    parts = random.sample(range(1, len(papa)), cuts)
    parts.sort()
    # choose: vetor de numeros aleatorios
    # que indicam os indices que serao trocados
    choose = random.sample(range(0, len(parts)+1), trades)

    # gerando os filhos de acordo com a quantidade de cortes
    son_1 = []
    for i in range (len(parts)+1):
        son_1.append(0)
        if i == 0:
            son_1[i] = papa[:parts[0]]
        elif i == len(parts):
            son_1[i] = papa[parts[i-1]:]
        else:
            son_1[i] = papa[parts[i-1]:parts[i]]

    son_2 = []
    for i in range(len(parts) + 1):
        son_2.append(0)
        if i == 0:
            son_2[i] = mama[:parts[0]]
        elif i == len(parts):
            son_2[i] = mama[parts[i - 1]:]
        else:
            son_2[i] = mama[parts[i - 1]:parts[i]]

    son_b = son_1.copy()

    son_1_changes_1 = ""
    son_1_changes_2 = ""
    for i in range(len(choose)):
        son_1[choose[i]] = son_2[choose[i]]
        son_1_changes_2 += son_2[choose[i]]
        son_2[choose[i]] = son_b[choose[i]]
        son_1_changes_1 += son_b[choose[i]]

    # comparar changes 1 e 2 e remover os characteres repetidos
    # GDFCJIEBAH vs AEFDJGICHB -- GFDBAJEHCI vs FBGAJEICHD
    boys = compare_changes(son_1_changes_1, son_1_changes_2)
    son_1_changes_1 = boys[0]
    son_1_changes_2 = boys[1]

    son_2_changes_1 = son_1_changes_2
    son_2_changes_2 = son_1_changes_1

    for i in range(len(son_1)):
        if i == choose[0]:
            continue
        # print(son_1[i])
        boys = compare_str(son_1[i], son_1_changes_2, son_1_changes_1)
        son_1[i] = boys[0]
        son_1_changes_2 = boys[1]
        son_1_changes_1 = boys[2]

    for i in range(len(son_2)):
        if i == choose[0]:
            continue
        # print(son_1[i])
        boys = compare_str(son_2[i], son_2_changes_2, son_2_changes_1)
        son_2[i] = boys[0]
        son_2_changes_2 = boys[1]
        son_2_changes_1 = boys[2]

    son1_label_1.setText(son_1[0])
    son1_label_2.setText(son_1[1])
    son1_label_3.setText(son_1[2])
    son2_label_1.setText(son_2[0])
    son2_label_2.setText(son_2[1])
    son2_label_3.setText(son_2[2])


def simple_cut_crossover(cuts):
    # cuts: quantidade de cortes
    # trades: quantidade de trocas
    trades = 1

    papa = father_line_edit.text()
    mama = mother_line_edit.text()

    # parts: vetor de numeros aleatorios
    # que indicam onde os cortes serao feitos
    parts = random.sample(range(1, len(papa)), cuts)
    parts.sort()

    # choose: vetor de numeros aleatorios
    # que indicam os indices que serao trocados
    choose = random.sample(range(0, len(parts)+1), trades)

    # iteracao que cria um filho
    son_1 = []
    for i in range (len(parts)+1):
        son_1.append(0)
        if i == 0:
            son_1[i] = papa[:parts[0]]
        elif i == len(parts):
            son_1[i] = papa[parts[i-1]:]
        else:
            son_1[i] = papa[parts[i-1]:parts[i]]

    son_2 = []
    for i in range(len(parts) + 1):
        son_2.append(0)
        if i == 0:
            son_2[i] = mama[:parts[0]]
        elif i == len(parts):
            son_2[i] = mama[parts[i - 1]:]
        else:
            son_2[i] = mama[parts[i - 1]:parts[i]]

    son_b = son_1.copy()

    for i in range(len(choose)):
        son_1[choose[i]] = son_2[choose[i]]
        son_2[choose[i]] = son_b[choose[i]]

    son1_label_1.setText(son_1[0])
    son1_label_2.setText(son_1[1])

    son2_label_1.setText(son_2[0])
    son2_label_2.setText(son_2[1])
    if cuts == 2:
        son1_label_3.setText(son_1[2])
        son2_label_3.setText(son_2[2])

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)

    # Loading widgets elements from ui file
    ui_file = QFile("crossover_operation.ui")
    ui_file.open(QFile.ReadOnly)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    window.show()

    # Getting widgets elements
    father_line_edit = window.findChild(QLineEdit, 'fatherLineEdit')
    mother_line_edit = window.findChild(QLineEdit, 'motherLineEdit')
    son1_label_1 = window.findChild(QLabel, 'son1Label1')
    son1_label_2 = window.findChild(QLabel, 'son1Label2')
    son1_label_3 = window.findChild(QLabel, 'son1Label3')
    son2_label_1 = window.findChild(QLabel, 'son2Label1')
    son2_label_2 = window.findChild(QLabel, 'son2Label2')
    son2_label_3 = window.findChild(QLabel, 'son2Label3')
    method_combo_box = window.findChild(QComboBox, 'methodComboBox')
    cross_push_button = window.findChild(QPushButton, 'crossPushButton')

    # Connecting
    cross_push_button.clicked.connect(on_cross_pushbutton_clicked)
    method_combo_box.currentTextChanged.connect(on_method_combobox_current_text_changed)

    sys.exit(app.exec_())