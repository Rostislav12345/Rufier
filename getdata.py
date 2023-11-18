from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QPushButton, QButtonGroup, QLayout, QBoxLayout, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QLineEdit
from PyQt5.QtGui import QFont
import subprocess
import json
import time as tm
app = QApplication([])
wid = QWidget()
text_timer = QLabel('0')
text_timer.setFont(QFont("Times", 36, QFont.Bold))
timer = QTimer()
data1 = 0
data2 = 0
data3 = 0
def dump_json_data(data, filename):
    """Dumps the given data to JSON format and writes it to the specified file.

    Args:
        data: The data to be dumped to JSON.
        filename: The path to the file to write the JSON data to.
    """

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
        
def collect_line_edit_data():
    text = text1field.text()
    text2 = text3field.text()
    text3 = text3field2.text()
    age2 = age.text()
    data = {
    "age": age,
    "data1": text,
    "data2": text2,
    "data3": text3,
    }
    with open("data1.txt", "w") as f:
       f.write(text)
    with open("data2.txt", "w") as f:
       f.write(text2)
    with open("data3.txt", "w") as f:
       f.write(text3)
    with open("age.txt", "w") as f:
       f.write(age2)
    wid.hide()
    subprocess.run(["python", "final.py"])
    
def timer1Event():
    global time
    time = time.addSecs(-1)
    text_timer.setText(time.toString("hh:mm:ss"))
    #text_timer.setFont(QFont("Times", 36, QFont.Bold)) 
    text_timer.setStyleSheet ("color: rgb(0,0,0)") 
    if time.toString("hh:mm:ss") == "00:00:00": 
        timer.stop()
def timer2Event():
    global time
    time = time.addSecs(-1)
    text_timer.setText(time.toString("hh:mm:ss"))
    #text_timer.setFont(QFont("Times", 36, QFont.Bold)) 
    text_timer.setStyleSheet ("color: rgb(0,0,0)") 
    if time.toString("hh:mm:ss") == "00:00:00": 
        tm.sleep(1)
        timer.timeout.connect(timer_test4)
def timer3Event():
    global time
    time = time.addSecs(-1)
    text_timer.setText(time.toString("hh:mm:ss"))
    #text_timer.setFont(QFont("Times", 36, QFont.Bold)) 
    text_timer.setStyleSheet ("color: rgb(0,0,0)") 
    if time.toString("hh:mm:ss") == "00:00:00": 
        tm.sleep(1)
        timer.timeout.connect(timer_test5)
def timer_test1():
    global time
    time = QTime(0,0,15)
    timer.timeout.connect(timer1Event)
    timer.start(1000)
def timer_test2():
    global time
    time = QTime(0,0,45)
    timer.timeout.connect(timer1Event)
    timer.start(1000)
def timer_test3():
    global time
    time = QTime(0,0,15)
    timer.timeout.connect(timer2Event)
    timer.start(1000)
def timer_test4():
    global time
    time = QTime(0,1,0)
    timer.timeout.connect(timer3Event)
    timer.start(1000)
def timer_test5():
    global time
    time = QTime(0,0,15)
    timer.timeout.connect(timer1Event)
    timer.start(1000)
    
        
name = QLineEdit('Full name')
age = QLineEdit('Age')
text1 = QLabel('Lie on your back and take a pulse for 15 seconds.\n'
               'Click the Start test to start the timer.\n'
               'Write down the result below.\n'
               )
text1field = QLineEdit()
text1start = QPushButton('Start Test')
text2 = QLabel('Perform 30 squats in 45 seconds. to start click Start Squat\n'
               )
text2start = QPushButton('Start Squat')
text2field = QLineEdit()
text3 = QLabel('Lie on your back and take your pulse for the first 15 seconds of the minute, then for the last 15 seconds of the minute. Press the "Start final test" button to start the timer.\n'
               'The first 15 seconds and the last 15 seconds after 1 min should be measured. Write down the results in the appropriate fields.'
               )
text3start = QPushButton('Start Final Test')
text3field = QLineEdit()
text3field2 = QLineEdit()
vertical = QVBoxLayout()
submit = QPushButton('Submit')
wid.resize(1200, 800)
wid.setWindowTitle('Rufier test')
vertical.addWidget(text_timer, alignment= Qt.AlignRight)
vertical.addWidget(name, alignment= Qt.AlignLeft)
vertical.addWidget(age, alignment= Qt.AlignLeft)
vertical.addWidget(text1, alignment= Qt.AlignLeft)
vertical.addWidget(text1start, alignment= Qt.AlignLeft)
vertical.addWidget(text1field, alignment= Qt.AlignLeft)
vertical.addWidget(text2, alignment= Qt.AlignLeft)
vertical.addWidget(text2start, alignment= Qt.AlignLeft)
vertical.addWidget(text3, alignment= Qt.AlignLeft)
vertical.addWidget(text3start, alignment= Qt.AlignLeft)
vertical.addWidget(text3field, alignment= Qt.AlignLeft)
vertical.addWidget(text3field2, alignment= Qt.AlignLeft)
vertical.addWidget(submit, alignment= Qt.AlignLeft)
text1start.clicked.connect(timer_test1)
text2start.clicked.connect(timer_test2)
text3start.clicked.connect(timer_test3)
submit.clicked.connect(collect_line_edit_data)
wid.setLayout(vertical)
wid.show()
app.exec()