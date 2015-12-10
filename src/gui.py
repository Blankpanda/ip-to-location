"""
currently unused.
"""

import sys
import locator


from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSlot

app = QApplication(sys.argv)
widg = QWidget()


# static form settings.
widg.setFixedSize(300, 80)
widg.setWindowTitle("IP to Location")

# form objects

info_label = QLabel("IP address/Domain name:", widg)
info_label.setToolTip("IP address/Domain name")
info_label.move(10,10)

find_button = QPushButton("Find",widg)
find_button.setToolTip("Uses inputed address/domain to find its location")
find_button.resize(find_button.sizeHint())
find_button.move(210,50)

input_textbox = QLineEdit(widg)
input_textbox.move(10,25)
input_textbox.resize(280,20)


# form object actions
@pyqtSlot()
def on_click():
    if input_textbox.text() == "":
        QMessageBox.about(widg, "Bad Input Message Box", "Please enter in a IP or domain name.")
    else:
        locator.find(input_textbox.text())

# form action bindings
find_button.clicked.connect(on_click)

# for use in other modules
def show_message_box(prompt):
    QMessageBox.about(widg, "Bad Input Message Box", prompt)


widg.show()

sys.exit(app.exec_())
