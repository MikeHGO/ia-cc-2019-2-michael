import sys, random
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtWidgets import QApplication, QComboBox, \
    QPushButton, QLineEdit, QLabel


def on_cross_pushbutton_clicked():
    if method_combo_box.currentText() == "Corte Simples":
        offsprings = simple_cut_crossover()
        # son1_label_3.setVisible(False)
        # son2_label_3.setVisible(False)
    else:
        offsprings = pmx_crossover()
        son1_label_3.setVisible(True)
        son2_label_3.setVisible(True)

    # son1_label_1.setText(offsprings[0])
    # son1_label_2.setText(offsprings[1])
    # son1_label_3.setText(offsprings[2])
    # son2_label_1.setText(offsprings[3])
    # son2_label_2.setText(offsprings[4])
    # son2_label_3.setText(offsprings[5])


def on_method_combobox_current_text_changed():
    print('combo box changed')

def pmx_crossover():
    return '','','','','',''


def simple_cut_crossover():
    cuts = 2

    papa = father_line_edit.text()
    mama = mother_line_edit.text()
    parts = random.sample(range(1, len(papa)), cuts)
    parts.sort()
    choose = random.randrange(cuts+1)

    son_1 = [papa[:parts[0]], papa[parts[0]:parts[1]], papa[parts[1]:]]
    son_2 = [mama[:parts[0]], mama[parts[0]:parts[1]], mama[parts[1]:]]

    aux = son_2[choose]

    son_2[choose] = son_1[choose]
    son_1[choose] = aux

    print(son_1)
    print(son_1[2])
    print(son_2)


    son1_label_1.setText(son_1[0])
    son1_label_2.setText(son_1[1])
    son1_label_3.setText(son_1[2])

    son2_label_1.setText(son_2[0])
    son2_label_2.setText(son_2[1])
    son2_label_3.setText(son_2[2])
#     adicionar corte duplo na combobox, deixar o "setup" generico for testing



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
