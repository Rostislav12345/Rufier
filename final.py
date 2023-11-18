from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QPushButton, QButtonGroup, QLayout, QBoxLayout, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QLineEdit
from PyQt5.QtGui import QFont
import subprocess
import time as tm
import os
txt_res1 = "Low, See your doctor right away!"
txt_res2 = "Satisfactory, See your doctor!"
txt_res3 = "Average, It may be worth seeing your doctor to get checked out."
txt_res4 = "Above average"
txt_res5 = "High"
if os.path.exists("age.txt"):
    with open("age.txt", "r") as f:
        tm.sleep(1)
        agee = f.read()
        age = int(agee)
        f.close()
        if os.path.exists("age.txt"):
            os.remove("age.txt")
            print('File deleted.')
        else:
            print('No File deleted')
else:
    print("could not read data age")
    
if os.path.exists("data1.txt"):
    with open("data1.txt", "r") as fe:
        tm.sleep(1)
        data1e = fe.read()
        data1 = int(data1e)
        fe.close()
        if os.path.exists("data1.txt"):
            os.remove("data1.txt")
            print('File deleted.')
        else:
            print('No File deleted')
else:
    print("could not read data age")
    
if os.path.exists("data2.txt"):
    with open("data2.txt", "r") as fee:
        tm.sleep(1)
        data2e = fee.read()
        data2 = int(data2e)
        fee.close()
        if os.path.exists("data2.txt"):
            os.remove("data2.txt")
            print('File deleted.')
        else:
            print('No File deleted')
else:
    print("could not read data age")
    
if os.path.exists("data3.txt"): 
    with open("data3.txt", "r") as feee:
        tm.sleep(1)
        data3e = feee.read()
        data3 = int(data3e)
        feee.close()
        if os.path.exists("data3.txt"):
            os.remove("data3.txt")
            print('File deleted.')
        else:
            print('No File deleted')
else:
    print("could not read data age")
    

def results():
    if age < 7:
        return "there is no data for this age"
    else:
        index = (4 * (int(data1) + int(data2) + int(data3)) - 200) / 10
        if age == 7 or age == 8:
            if index >= 21:
                return txt_res1
            elif index < 21 and index >= 17:
                return txt_res2
            elif index < 17 and index >= 12:
                return txt_res3
            elif index < 12 and index >= 6.5:
                return txt_res4
            else:
                return txt_res5
        elif age == 9 or age == 10:
            if index >= 19.5:
                return txt_res1
            elif index < 19.5 and index >= 15.5:
                return txt_res2
            elif index < 15.5 and index >= 10.5:
                return txt_res3
            elif index < 10.5 and index >= 5:
                return txt_res4
            else:
                return txt_res5
        elif age == 11 or age == 12:
            if index >= 18:
                return txt_res1
            elif index < 18 and index >= 14:
                return txt_res2
            elif index < 14 and index >= 9:
                return txt_res3
            elif index < 9 and index >= 3.5:
                return txt_res4
            else:
                return txt_res5
        elif age == 13 or age == 14:
            if index >= 16.5:
                return txt_res1
            elif index < 16.5 and index >= 12.5:
                return txt_res2
            elif index < 12.5 and index >= 7.5:
                return txt_res3
            elif index < 7.5 and index >= 2:
                return txt_res4
            else:
                return txt_res5
        else:
            if index >= 15:
                return txt_res1
            elif index < 15 and index >= 11:
                return txt_res2
            elif index < 11 and index >= 6:
                return txt_res3
            elif index < 6 and index >= 0.5:
                return txt_res4
            else:
                return txt_res5


app = QApplication([])
wid = QWidget() 
preres = QLabel("Rufier test Results:")
#Lab = QLabel(age)
#Labe = QLabel(data1)
#Labee = QLabel(data2)
#Labeee = QLabel(data3)
Result = QLabel(results())
vertical = QVBoxLayout()
wid.resize(1200, 800)
wid.setWindowTitle('Rufier test Results')
vertical.addWidget(preres, alignment= Qt.AlignCenter)
vertical.addWidget(Result, alignment= Qt.AlignCenter)
#vertical.addWidget(Labe, alignment= Qt.AlignCenter)
#vertical.addWidget(Labee, alignment= Qt.AlignCenter)
#vertical.addWidget(Labeee, alignment= Qt.AlignCenter)
wid.setLayout(vertical)
wid.show()
app.exec()