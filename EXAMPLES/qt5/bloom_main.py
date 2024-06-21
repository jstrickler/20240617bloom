import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_bloom import Ui_Bloom

class BloomMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_Bloom()
        self.ui.setupUi(self)

        # Connect up buttons.
        # self.ui.BUTTON_NAME.clicked.connect(self._pushed)
        self.ui.bt_create.clicked.connect(self._create)  # HANDLE THE EVENT!

    def _create(self):
        self.ui.statusbar.showMessage("Creating order", 500)
        # self.ui.statusbar.removeMessage()
        # or
        # self.ui.statusbar.showMessage("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = BloomMain()
    main.show()
    status_code = app.exec()
    sys.exit(status_code)

