import sys
import xml_make as ss


from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = ss.Ui_Form()
    # ui = learn.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
