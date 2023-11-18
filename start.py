from PyQt5.QtCore import Qt
import subprocess
from PyQt5.QtWidgets import QApplication, QPushButton, QButtonGroup, QLayout, QBoxLayout, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QLineEdit
app = QApplication([])
wid = QWidget()
def nextfunc():
    wid.hide()
    subprocess.run(["python", "getdata.py"])

hi = QLabel('This application allows you to use the Rufier test to make an initial diagnosis of your health.\n'
    'The Rufier test is a set of physical exercises designed to assess your cardiac performance during physical exertion. The subject lies in the supine position for 5 minutes and has their pulse rate measured for 15 seconds;\n'
    'then, within 45 seconds, the subject performs 30 squats.\n'
    'When the exercise ends, the subject lies down and their pulse is measured again for the first 15 seconds\n'
    'and then for the last 15 seconds of the first minute of the recovery period.\n'
    'Important! If you feel unwell during the test (dizziness,\n'
    'tinnitus, shortness of breath, etc.), stop the test and consult a physician.\n')
hii = QLabel('Welcome to the Health Status detection program!')
start = QPushButton('Start Test')
vertical = QVBoxLayout()
wid.resize(1000, 800)
wid.setWindowTitle('Rufier test')
vertical.addWidget(hii, alignment=Qt.AlignCenter)
vertical.addWidget(hi, alignment=Qt.AlignCenter)
vertical.addWidget(start, alignment=Qt.AlignCenter)
wid.setLayout(vertical)
start.clicked.connect(nextfunc)
wid.show()
app.exec()