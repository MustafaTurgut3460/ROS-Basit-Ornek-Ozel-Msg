#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yarisma_gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from datetime import datetime
from PyQt5 import QtCore, QtWidgets
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(270, 70, 251, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.speedEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.speedEdit.setReadOnly(True)
        self.speedEdit.setObjectName("speedEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.speedEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.xEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.xEdit.setReadOnly(True)
        self.xEdit.setObjectName("xEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.xEdit)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.yEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.yEdit.setReadOnly(True)
        self.yEdit.setObjectName("yEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.yEdit)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.timeEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.timeEdit.setReadOnly(True)
        self.timeEdit.setObjectName("timeEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.timeEdit)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 40, 101, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 280, 101, 17))
        self.label_6.setObjectName("label_6")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(260, 310, 261, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.stopButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.stopButton.setObjectName("stopButton")
        self.gridLayout.addWidget(self.stopButton, 3, 1, 1, 1)
        self.forwardButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.forwardButton.setObjectName("forwardButton")
        self.gridLayout.addWidget(self.forwardButton, 2, 1, 1, 1)
        self.rightButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.rightButton.setObjectName("rightButton")
        self.gridLayout.addWidget(self.rightButton, 3, 2, 1, 1)
        self.leftButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.leftButton.setObjectName("leftButton")
        self.gridLayout.addWidget(self.leftButton, 3, 0, 1, 1)
        self.backButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Robot Hız (m/s):"))
        self.speedEdit.setText(_translate("MainWindow", "0.0"))
        self.label_2.setText(_translate("MainWindow", "Konum X:"))
        self.xEdit.setText(_translate("MainWindow", "0.0"))
        self.label_3.setText(_translate("MainWindow", "Konum Y:"))
        self.yEdit.setText(_translate("MainWindow", "0.0"))
        self.label_4.setText(_translate("MainWindow", "Görev Süresi (dk,sn):"))
        self.timeEdit.setText(_translate("MainWindow", "0.0"))
        self.label_5.setText(_translate("MainWindow", "Robot Bilgileri"))
        self.label_6.setText(_translate("MainWindow", "Robot Kontrol "))
        self.stopButton.setText(_translate("MainWindow", "Dur"))
        self.forwardButton.setText(_translate("MainWindow", "İleri"))
        self.rightButton.setText(_translate("MainWindow", "Sağ"))
        self.leftButton.setText(_translate("MainWindow", "Sol"))
        self.backButton.setText(_translate("MainWindow", "Geri"))

        rospy.init_node("yarisma_gui")
        self.startTime = datetime.now()
        self.pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
        self.speedMessage = Twist()
        rospy.Subscriber("odom", Odometry, self.odometryCallback)
        

        # buttons
        self.forwardButton.clicked.connect(self.forward)
        self.backButton.clicked.connect(self.back)
        self.leftButton.clicked.connect(self.left)
        self.rightButton.clicked.connect(self.right)
        self.stopButton.clicked.connect(self.stop)

    def odometryCallback(self, message):
        self.xEdit.setText(str(round(message.pose.pose.position.x, 4)))
        self.yEdit.setText(str(round(message.pose.pose.position.y, 4)))

        # yarisma suresi
        currentTime = datetime.now()
        self.timeEdit.setText(str(self.getTimeDifferance(self.startTime, currentTime)))

    def forward(self):
        self.speedMessage.linear.x = 0.5
        self.speedMessage.angular.z = 0.0
        self.pub.publish(self.speedMessage)
        self.speedEdit.setText(str(self.speedMessage.linear.x))

    def back(self):
        self.speedMessage.linear.x = -0.5
        self.speedMessage.angular.z = 0.0
        self.pub.publish(self.speedMessage)
        self.speedEdit.setText(str(self.speedMessage.linear.x))

    def left(self):
        self.speedMessage.linear.x = 0.0
        self.speedMessage.angular.z = 0.5
        self.pub.publish(self.speedMessage)

    def right(self):
        self.speedMessage.linear.x = 0.0
        self.speedMessage.angular.z = -0.5
        self.pub.publish(self.speedMessage)

    def stop(self):
        self.speedMessage.linear.x = 0.0
        self.speedMessage.angular.z = 0.0
        self.pub.publish(self.speedMessage)
        self.speedEdit.setText(str(self.speedMessage.linear.x))

    def getTimeDifferance(self, time1, time2):
        secondsInDay = 24 * 60 * 60
        differance = time2 - time1
        return divmod(differance.days * secondsInDay + differance.seconds, 60)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
