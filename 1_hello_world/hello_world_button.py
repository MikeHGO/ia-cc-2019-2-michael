from PySide2.QtWidgets import QApplication,QPushButton
from PySide2.QtCore import Slot

@Slot() # identifica que uma função será utilizada como Slot
def say_hello():
    print("Button clicked, Hello")

if __name__ == "__main__":
    #Creat the Qt Application
    app = QApplication([])

    #Creat a button, connect it and show it
    button = QPushButton("Click me")
    button.clicked.connect(say_hello)
    button.show()
    #Run the main QT
    app.exec_()