import sys
from PyQt5 import QtWidgets, uic
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QLineEdit, QPlainTextEdit
import pafy
import io 

code = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>625</width>
    <height>353</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>90</x>
     <y>197</y>
     <width>441</width>
     <height>91</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 36pt &quot;MS Shell Dlg 2&quot;;</string>
   </property>
   <property name="text">
    <string>Download</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="pippo">
   <property name="geometry">
    <rect>
     <x>90</x>
     <y>151</y>
     <width>441</width>
     <height>31</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 14pt &quot;MS Shell Dlg 2&quot;;</string>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>60</x>
     <y>60</y>
     <width>541</width>
     <height>61</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 italic 28pt &quot;Sitka&quot;;</string>
   </property>
   <property name="text">
    <string>Insert url to Download mp3</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>'''



class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()        
        f = io.StringIO(code)
        uic.loadUi(f, self)

        self.pushButton.clicked.connect(self.pippato)


    def pippato(self):
        url = self.pippo.text()
        video = pafy.new(url)

        bestaudio = video.getbestaudio()
        print(video.title)

        bestaudio.download()
        

app = QApplication(sys.argv)

main = Main()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main)
widget.setFixedWidth(625)
widget.setFixedHeight(353)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Program been Started, insert de link of the YouTube video to download it Audio.\n\n")
