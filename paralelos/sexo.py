import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class janela (QMainWindow):
    def __init__(self):
        super().__init__()

        self.largura = 250
        self.altura = 100
        self.titulo = "Janela Foda"
        self.CarregarJanela()


        def CarregarJanela(self):
            self.setGeometry(self.largura, self.altura)
            self.setWindoTitle(self.titulo)
            self.show()


app = QApplication(sys.argv)
j = janela()
sys.exit(app.exec_())