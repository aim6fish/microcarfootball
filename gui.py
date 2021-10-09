import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import serial
import time
COM_PORT = 'COM10'    
BAUD_RATES = 9600   
COM_CTRL = 'COM11'
ser = serial.Serial(COM_PORT, BAUD_RATES)
ser_ctrl = serial.Serial(COM_CTRL, BAUD_RATES)
buf = 0

class mainwin(QWidget):
    def __init__(self):
        super(mainwin,self).__init__()
        self.resize(1500,1500)
        self.setWindowTitle("Car Controller")
        
        self.button1=QPushButton("exit",self)
        self.button1.clicked.connect(self.close)
        self.button1.setCheckable(True)
        self.button1.toggle()
        
        self.button2=QToolButton()
        self.button2.setFixedSize(300, 300)
        self.button2.setIcon(QIcon(QPixmap("icons/left.png")))
        self.button2.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.button2.setIconSize(QSize(300, 300))
        self.button2.clicked.connect(lambda:self.send_signal("left"))

        self.button3=QToolButton()
        self.button3.setFixedSize(300, 300)
        self.button3.setIcon(QIcon(QPixmap("icons/up.png")))
        self.button3.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.button3.setIconSize(QSize(300, 300))
        self.button3.clicked.connect(lambda:self.send_signal("up"))

        self.button4=QToolButton()
        self.button4.setFixedSize(300, 300)
        self.button4.setIcon(QIcon(QPixmap("icons/right.png")))
        self.button4.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.button4.setIconSize(QSize(300, 300))
        self.button4.clicked.connect(lambda:self.send_signal("right"))

        self.button5=QToolButton()
        self.button5.setFixedSize(300, 300)
        self.button5.setIcon(QIcon(QPixmap("icons/down.png")))
        self.button5.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.button5.setIconSize(QSize(300, 300))
        self.button5.clicked.connect(lambda:self.send_signal("down"))

        self.button6=QToolButton()
        self.button6.setFixedSize(300, 300)
        self.button6.setIcon(QIcon(QPixmap("icons/increase.png")))
        self.button6.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.button6.setIconSize(QSize(200, 200))
        self.button6.clicked.connect(lambda:self.send_signal("increase"))

        self.button7=QToolButton()
        self.button7.setFixedSize(300, 300)
        self.button7.setIcon(QIcon(QPixmap("icons/decrease.png")))
        self.button7.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.button7.setIconSize(QSize(200, 200))
        self.button7.clicked.connect(lambda:self.send_signal("decrease"))

        self.button8=QToolButton()
        self.button8.setFixedSize(300, 300)
        #self.button8.setIcon(QIcon(QPixmap("C:/Users/邱彥慈/Desktop/clear.png")))
        self.button8.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.button8.setIconSize(QSize(300, 300))
        
        self.button9=QToolButton()
        self.button9.setFixedSize(300, 300)
        #self.button9.setIcon(QIcon(QPixmap("C:/Users/邱彥慈/Desktop/clear.png")))
        self.button9.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.button9.setIconSize(QSize(300, 300))
        
        self.button10=QToolButton()
        self.button10.setFixedSize(300, 300)
        #self.button10.setIcon(QIcon(QPixmap("C:/Users/邱彥慈/Desktop/clear.png")))
        self.button10.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.button10.setIconSize(QSize(300, 300))
        
        


        self.setlayout_()
        
    
    def send_signal(self, dir):
        if(dir == "left"):
            ser.write(b'l\r')
            time.sleep(0.5)
            #time.sleep(2)
            ser.cancel_write()
            #while ser_ctrl.readline().decode() != "left ok": buf = 0
            #ser_ctrl.reset_input_buffer()
        elif(dir == "right"):
            ser.write(b'r\r')
            time.sleep(0.5)
            #time.sleep(2)
            ser.cancel_write()
            #while ser_ctrl.readline().decode() != "right ok": buf = 0
            #ser_ctrl.reset_input_buffer()
        elif(dir == "up"):
            ser.write(b's\r')
            time.sleep(0.5)
            #time.sleep(2)
            ser.cancel_write()
            #while ser_ctrl.av != "straight ok": buf = 0
            #ser_ctrl.reset_input_buffer()
        elif(dir == "increase"):
            ser.write(b'i\r')
            time.sleep(0.5)
            #time.sleep(2)
            ser.cancel_write()
            #while ser_ctrl.readline().decode() != "increase ok": buf = 0
            #ser_ctrl.reset_input_buffer()
        elif(dir == "decrease"):
            ser.write(b'd\r')
            time.sleep(0.5)
            #time.sleep(2)
            ser.cancel_write()
            #while ser_ctrl.readline().decode() != "decrease ok": buf = 0
            #ser_ctrl.reset_input_buffer()
        elif(dir == "clear"):
            ser.write(b'c\r')
            time.sleep(0.5)
            #time.sleep(2)
            ser.cancel_write()
            #while ser_ctrl.readline().decode() != "clear ok": buf = 0
            #ser_ctrl.reset_input_buffer()
        elif(dir == "Lround"):
            ser.write(b'Lround\r')
            time.sleep(0.5)
            #time.sleep(2)
            ser.cancel_write()
            #while ser_ctrl.readline().decode() != "Lround ok": buf = 0
            #ser_ctrl.reset_input_buffer()
        elif(dir == "Rround"):
            ser.write(b'Rround\r')
            time.sleep(0.5)
            #time.sleep(2)
            ser.cancel_write()
            #while ser_ctrl.readline().decode() != "Rround ok": buf = 0
            #ser_ctrl.reset_input_buffer()
        else:
            ser.write(b'b\r')
            time.sleep(0.5)
            #time.sleep(2)
            ser.cancel_write()
            #while ser_ctrl.readline().decode() != "backward ok": buf = 0
            #ser_ctrl.reset_input_buffer()
        
    
    def setlayout_(self):
        self.arr=QGridLayout(self)
        self.arr.addWidget(self.button3, 0, 1)
        self.arr.addWidget(self.button2, 1, 0)
        self.arr.addWidget(self.button4, 1, 2)
        self.arr.addWidget(self.button5, 2, 1)
        self.arr.addWidget(self.button6, 0, 2)
        self.arr.addWidget(self.button7, 0, 0)
        self.arr.addWidget(self.button8, 1, 1)
        self.arr.addWidget(self.button9, 2, 0)
        self.arr.addWidget(self.button10,2, 2)
        self.arr.setSpacing(15)
        self.setLayout(self.arr)
       
        
if __name__=="__main__":

    app=QApplication(sys.argv)
    MainWindow=mainwin()
    MainWindow.show()
    app.exec_()