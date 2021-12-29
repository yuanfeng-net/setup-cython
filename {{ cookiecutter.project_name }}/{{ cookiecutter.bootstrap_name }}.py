import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
#import Ui_mainwindow as Ui_mainwindow  # 加载我们的布局
#from mainwindowViewModel import mainwindowViewModel
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    #ui = Ui_mainwindow.Ui_MainWindow()
    #ui.setupUi(MainWindow)

    #加载事件
    #mainwindowViewModel(ui)

    MainWindow.show()
    sys.exit(app.exec_())
