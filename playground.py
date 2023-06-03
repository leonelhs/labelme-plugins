import os
import sys

from qtpy import QtCore
from qtpy.QtWidgets import QApplication
from qtpy.QtWidgets import QWidget, QVBoxLayout, QPushButton

from plugins.makecontour import DialogEndpoint

# Default demo plugins location path
location = os.path.dirname(os.path.abspath(__file__))
INSTALL_DIR = os.path.join(location, "plugins")


@QtCore.Slot()
def signalHandler(value):
    print(value)


app = QApplication(sys.argv)
win = QWidget(None)
win.setLayout(QVBoxLayout())
btn_manager = QPushButton("Show loader")
win.layout().addWidget(btn_manager)

# load = Loading(win)
load = DialogEndpoint(win)

load.signalEndpoint.connect(signalHandler)

btn_manager.clicked.connect(load.show)

win.show()
sys.exit(app.exec_())
