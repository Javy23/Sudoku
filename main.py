from PySide2.QtWidgets import QApplication
from controllers.ControllerSudoku import ControllerSudoku

if __name__ == '__main__':
    app = QApplication()
    window = ControllerSudoku()  
    window.show()
    window.setMaximumSize(762, 620)
    window.setMinimumSize(762, 620)
    app.exec_()
