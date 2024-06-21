# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bloom.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Bloom(object):
    def setupUi(self, Bloom):
        Bloom.setObjectName("Bloom")
        Bloom.resize(392, 430)
        self.centralwidget = QtWidgets.QWidget(Bloom)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 10, 160, 100))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bt_sugar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_sugar.setObjectName("bt_sugar")
        self.verticalLayout.addWidget(self.bt_sugar)
        self.bt_honey = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_honey.setObjectName("bt_honey")
        self.verticalLayout.addWidget(self.bt_honey)
        self.bt_stevia = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bt_stevia.setObjectName("bt_stevia")
        self.verticalLayout.addWidget(self.bt_stevia)
        self.cb_iced = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_iced.setGeometry(QtCore.QRect(20, 40, 85, 20))
        self.cb_iced.setObjectName("cb_iced")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 160, 318, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.bt_create = QtWidgets.QPushButton(self.centralwidget)
        self.bt_create.setGeometry(QtCore.QRect(140, 330, 100, 32))
        self.bt_create.setObjectName("bt_create")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(140, 250, 211, 74))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 250, 111, 61))
        self.label.setObjectName("label")
        Bloom.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Bloom)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 392, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Bloom.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Bloom)
        self.statusbar.setObjectName("statusbar")
        Bloom.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(Bloom)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtWidgets.QAction(Bloom)
        self.actionQuit.setObjectName("actionQuit")
        self.actionCut = QtWidgets.QAction(Bloom)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(Bloom)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(Bloom)
        self.actionPaste.setObjectName("actionPaste")
        self.actionAbout_Bloom = QtWidgets.QAction(Bloom)
        self.actionAbout_Bloom.setObjectName("actionAbout_Bloom")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuHelp.addAction(self.actionAbout_Bloom)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Bloom)
        QtCore.QMetaObject.connectSlotsByName(Bloom)

    def retranslateUi(self, Bloom):
        _translate = QtCore.QCoreApplication.translate
        Bloom.setWindowTitle(_translate("Bloom", "Bloomington, MN GIS"))
        self.bt_sugar.setText(_translate("Bloom", "Sugar"))
        self.bt_honey.setText(_translate("Bloom", "Honey"))
        self.bt_stevia.setText(_translate("Bloom", "Stevia"))
        self.cb_iced.setText(_translate("Bloom", "Iced"))
        self.radioButton.setText(_translate("Bloom", "RadioButton"))
        self.radioButton_2.setText(_translate("Bloom", "RadioButton"))
        self.radioButton_3.setText(_translate("Bloom", "RadioButton"))
        self.bt_create.setText(_translate("Bloom", "Create Order"))
        self.label.setText(_translate("Bloom", "Extra Instructions"))
        self.menuFile.setTitle(_translate("Bloom", "File"))
        self.menuEdit.setTitle(_translate("Bloom", "Edit"))
        self.menuHelp.setTitle(_translate("Bloom", "Help"))
        self.actionOpen.setText(_translate("Bloom", "Open..."))
        self.actionQuit.setText(_translate("Bloom", "Quit"))
        self.actionCut.setText(_translate("Bloom", "Cut"))
        self.actionCopy.setText(_translate("Bloom", "Copy"))
        self.actionPaste.setText(_translate("Bloom", "Paste"))
        self.actionAbout_Bloom.setText(_translate("Bloom", "About Bloom"))
