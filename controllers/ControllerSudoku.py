from asyncio.windows_events import NULL
from PySide2.QtWidgets import QWidget
from views.ViewSudoku import ViewSudoku
from models.Play import *

class ControllerSudoku(QWidget, ViewSudoku):

    play = NULL
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start()
        self.btnNuevo.clicked.connect(self.start)
        self.btnResolver.clicked.connect(self.resolver)
        
    def start(self):
        self.play = Play()
        self.play.start(self.tablero)
    
    def resolver(self):
        self.play.resolver(self.tablero)