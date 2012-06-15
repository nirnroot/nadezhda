#!/usr/bin/python3.2

import sys
from PyQt4.QtCore import SIGNAL, SLOT
from PyQt4.QtGui import QApplication, QWidget, QLabel, QVBoxLayout, QCheckBox, QPushButton

# TODO: replace with read from sqlbase or file
options = ['SHED_ULE','PREEMPTION','INET','INET6'];

if __name__=='__main__':

	app = QApplication(sys.argv)
	
	MainWindow = QWidget()
	# TODO: make translatable
	MainWindow.setWindowTitle("Надежда - шаблоны конфигураций ядра FreeBSD")
	MainWindow.setGeometry(600, 300, 500, 150)
	#self.setWindowIcon(QtGui.QIcon('pictures/crazy.ico'))

	Layout = QVBoxLayout(MainWindow)
	
	# Print options
	for i in options:
		Layout.addWidget(QCheckBox(i));
	
	# Exit button
	ExitButton = QPushButton("Выход", MainWindow)
	ExitButton.resize(200, 40)
	ExitButton
	Layout.addWidget(ExitButton)
	ExitButton.connect(ExitButton, SIGNAL("clicked()"), app, SLOT("quit()"))
	
	MainWindow.show()

	sys.exit(app.exec_())
	

