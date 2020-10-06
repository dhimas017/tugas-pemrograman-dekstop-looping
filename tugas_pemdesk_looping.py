import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

#membuat fungsi utk menentukan layout window
def window_go():
   #inisialisasi pyqt
   app = QApplication(sys.argv)
   window = QWidget()

   #menyiapkan label, menempelkan label ke window
   #settext, dan posisi
   for i in range(10):
         textLabel = QLabel(window)
         textLabel.setText("Hello World!")
         textLabel.move(100,50*i)

   #menentukan ukuran window, + title dan menampilkan
   window.setGeometry(100,100,320,200)
   window.setWindowTitle("PyQt5 Example")
   window.show()
   sys.exit(app.exec_())


if __name__ == '__main__':
   window_go()