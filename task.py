# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1399, 741)
        MainWindow.setMinimumSize(QtCore.QSize(1399, 741))
        MainWindow.setMaximumSize(QtCore.QSize(1399, 741))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 10, 1401, 101))
        self.label1.setMaximumSize(QtCore.QSize(700000, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(20, 250, 1091, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label1_2 = QtWidgets.QLabel(self.centralwidget)
        self.label1_2.setGeometry(QtCore.QRect(20, 290, 1391, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label1_2.setFont(font)
        self.label1_2.setObjectName("label1_2")
        self.label2_2 = QtWidgets.QLabel(self.centralwidget)
        self.label2_2.setGeometry(QtCore.QRect(20, 390, 1361, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label2_2.setFont(font)
        self.label2_2.setObjectName("label2_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 460, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 490, 591, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label1_3 = QtWidgets.QLabel(self.centralwidget)
        self.label1_3.setGeometry(QtCore.QRect(20, 590, 1391, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label1_3.setFont(font)
        self.label1_3.setObjectName("label1_3")
        self.pushButton_Cramer = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Cramer.setGeometry(QtCore.QRect(20, 700, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Cramer.setFont(font)
        self.pushButton_Cramer.setObjectName("pushButton_Cramer")
        self.pushButton_Gauss = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Gauss.setGeometry(QtCore.QRect(220, 700, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Gauss.setFont(font)
        self.pushButton_Gauss.setObjectName("pushButton_Gauss")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 110, 391, 141))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:\\img\\table.png"))
        self.label_3.setObjectName("label_3")
        self.pushButton_Matrix = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Matrix.setGeometry(QtCore.QRect(420, 700, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Matrix.setFont(font)
        self.pushButton_Matrix.setObjectName("pushButton_Matrix")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "СЛАУ"))
        self.label1.setText(_translate("MainWindow", "Из некоторого листового материала необходимо выкроить 360 заготовок типа А, 300 заготовок\n"
"типа Б и 675 заготовок типа В. При этом можно применять три типа способа раскроя. Количество\n"
"заготовок, получаемых из каждого листа при каждом способе раскроя, указано в таблице:"))
        self.label2.setText(_translate("MainWindow", "Записать в математической формуле условия выполнения задания."))
        self.label1_2.setText(_translate("MainWindow", "Решение. Обозначим через x, y, z количество листов материала, раскраиваемых соответственно\n"
"первым, вторым и третьим способами. Тогда при первом способе раскроя x листов будет\n"
"получено 3x заготовок типа А, при втором - 2y, при третьем - z."))
        self.label2_2.setText(_translate("MainWindow", "Для полного выполнения задания по заготовкам типа А сумма 3x + 2y + z должна\n"
"равняться 360, т.е."))
        self.label.setText(_translate("MainWindow", "3x + 2y + z = 360."))
        self.label_2.setText(_translate("MainWindow", "Аналогично получаем уравнения\n"
"x + 6y + 2z = 300\n"
"4x + y + 5z = 675,"))
        self.label1_3.setText(_translate("MainWindow", "которым должны удовлетворять неизвестные x, y, z для того, чтобы выполнить задание по\n"
"заготовкам Б и В. Полученная система линейных уравнений и выражает в математической\n"
"формуле условия выполнения всего задания по заготовкам А, Б и В."))
        self.pushButton_Cramer.setText(_translate("MainWindow", "Метод Крамера"))
        self.pushButton_Gauss.setText(_translate("MainWindow", "Метод Гаусса"))
        self.pushButton_Matrix.setText(_translate("MainWindow", "Метода Гаусса-Жордана"))