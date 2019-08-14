#importando as classes adequadas do PySide2
from PySide2.QtWidgets import QApplication, QLabel


if __name__ == "__main__":
    # here we create the application
    app = QApplication([])

    # Then, we create a label with the text
    label = QLabel("Hellow world")
    label.show()

    # Finally, we execute our app
    app.exec_()