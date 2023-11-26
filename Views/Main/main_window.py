# Form implementation generated from reading ui file '.\main-window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Main(object):
    def setupUi(self, MainWindow_Main):
        MainWindow_Main.setObjectName("MainWindow_Main")
        MainWindow_Main.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        MainWindow_Main.resize(800, 600)
        MainWindow_Main.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow_Main)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.groupBox_Postal_Code = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_Postal_Code.setObjectName("groupBox_Postal_Code")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_Postal_Code)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_Postal_Code = QtWidgets.QLineEdit(parent=self.groupBox_Postal_Code)
        self.lineEdit_Postal_Code.setText("")
        self.lineEdit_Postal_Code.setFrame(True)
        self.lineEdit_Postal_Code.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_Postal_Code.setReadOnly(False)
        self.lineEdit_Postal_Code.setClearButtonEnabled(True)
        self.lineEdit_Postal_Code.setObjectName("lineEdit_Postal_Code")
        self.horizontalLayout_2.addWidget(self.lineEdit_Postal_Code)
        spacerItem1 = QtWidgets.QSpacerItem(10, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_Add_Postal_Code = QtWidgets.QPushButton(parent=self.groupBox_Postal_Code)
        self.pushButton_Add_Postal_Code.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton_Add_Postal_Code.setObjectName("pushButton_Add_Postal_Code")
        self.horizontalLayout_2.addWidget(self.pushButton_Add_Postal_Code)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addWidget(self.groupBox_Postal_Code)
        self.groupBox_Time_Interval = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_Time_Interval.setObjectName("groupBox_Time_Interval")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_Time_Interval)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(parent=self.groupBox_Time_Interval)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.comboBox_Date_From = QtWidgets.QComboBox(parent=self.groupBox_Time_Interval)
        self.comboBox_Date_From.setMinimumSize(QtCore.QSize(75, 0))
        self.comboBox_Date_From.setObjectName("comboBox_Date_From")
        self.horizontalLayout_5.addWidget(self.comboBox_Date_From)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(10, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_Time_Interval)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.comboBox_Date_To = QtWidgets.QComboBox(parent=self.groupBox_Time_Interval)
        self.comboBox_Date_To.setMinimumSize(QtCore.QSize(75, 0))
        self.comboBox_Date_To.setObjectName("comboBox_Date_To")
        self.horizontalLayout_6.addWidget(self.comboBox_Date_To)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4.addWidget(self.groupBox_Time_Interval)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.graphicsView_Interactive_Map = QtWidgets.QGraphicsView(parent=self.centralwidget)
        self.graphicsView_Interactive_Map.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.graphicsView_Interactive_Map.setObjectName("graphicsView_Interactive_Map")
        self.verticalLayout_4.addWidget(self.graphicsView_Interactive_Map)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton_Generate_Report = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Generate_Report.setObjectName("pushButton_Generate_Report")
        self.horizontalLayout.addWidget(self.pushButton_Generate_Report)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        MainWindow_Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow_Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(parent=self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Settings = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Settings.setObjectName("menu_Settings")
        self.menu_Help = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_Locations = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Locations.setObjectName("menu_Locations")
        MainWindow_Main.setMenuBar(self.menubar)
        self.action_About_Program = QtGui.QAction(parent=MainWindow_Main)
        self.action_About_Program.setObjectName("action_About_Program")
        self.action_Exit = QtGui.QAction(parent=MainWindow_Main)
        self.action_Exit.setObjectName("action_Exit")
        self.action_App_Settings = QtGui.QAction(parent=MainWindow_Main)
        self.action_App_Settings.setObjectName("action_App_Settings")
        self.action_Raport_Settings = QtGui.QAction(parent=MainWindow_Main)
        self.action_Raport_Settings.setObjectName("action_Raport_Settings")
        self.action_Settings = QtGui.QAction(parent=MainWindow_Main)
        self.action_Settings.setObjectName("action_Settings")
        self.action_Save = QtGui.QAction(parent=MainWindow_Main)
        self.action_Save.setObjectName("action_Save")
        self.action_Save_As_New = QtGui.QAction(parent=MainWindow_Main)
        self.action_Save_As_New.setObjectName("action_Save_As_New")
        self.action_Selected_Locations = QtGui.QAction(parent=MainWindow_Main)
        self.action_Selected_Locations.setObjectName("action_Selected_Locations")
        self.action_Generate_Report = QtGui.QAction(parent=MainWindow_Main)
        self.action_Generate_Report.setObjectName("action_Generate_Report")
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.action_Save_As_New)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Generate_Report)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menu_Settings.addAction(self.action_Settings)
        self.menu_Help.addAction(self.action_About_Program)
        self.menu_Locations.addAction(self.action_Selected_Locations)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Locations.menuAction())
        self.menubar.addAction(self.menu_Settings.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow_Main)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Main)

    def retranslateUi(self, MainWindow_Main):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Main.setWindowTitle(_translate("MainWindow_Main", "DemoG"))
        self.groupBox_Postal_Code.setTitle(_translate("MainWindow_Main", "Kod pocztowy:"))
        self.lineEdit_Postal_Code.setPlaceholderText(_translate("MainWindow_Main", "00-000"))
        self.pushButton_Add_Postal_Code.setText(_translate("MainWindow_Main", "Dodaj"))
        self.groupBox_Time_Interval.setTitle(_translate("MainWindow_Main", "Przedział czasowy:"))
        self.label.setText(_translate("MainWindow_Main", "Od:"))
        self.comboBox_Date_From.setPlaceholderText(_translate("MainWindow_Main", "od"))
        self.label_2.setText(_translate("MainWindow_Main", "Do:"))
        self.comboBox_Date_To.setPlaceholderText(_translate("MainWindow_Main", "do"))
        self.pushButton_Generate_Report.setText(_translate("MainWindow_Main", " Generuj raport "))
        self.menu_File.setTitle(_translate("MainWindow_Main", "Plik"))
        self.menu_Settings.setTitle(_translate("MainWindow_Main", "Ustawienia"))
        self.menu_Help.setTitle(_translate("MainWindow_Main", "Pomoc"))
        self.menu_Locations.setTitle(_translate("MainWindow_Main", "Lokalizacje"))
        self.action_About_Program.setText(_translate("MainWindow_Main", "O programie..."))
        self.action_About_Program.setShortcut(_translate("MainWindow_Main", "F1"))
        self.action_Exit.setText(_translate("MainWindow_Main", "Wyjście"))
        self.action_App_Settings.setText(_translate("MainWindow_Main", "Aplikacji"))
        self.action_Raport_Settings.setText(_translate("MainWindow_Main", "Raportu"))
        self.action_Settings.setText(_translate("MainWindow_Main", "Ustawienia"))
        self.action_Save.setText(_translate("MainWindow_Main", "Zapisz"))
        self.action_Save.setShortcut(_translate("MainWindow_Main", "Ctrl+S"))
        self.action_Save_As_New.setText(_translate("MainWindow_Main", "Zapisz jako nowy..."))
        self.action_Selected_Locations.setText(_translate("MainWindow_Main", "Wybrane lokalizacje"))
        self.action_Selected_Locations.setShortcut(_translate("MainWindow_Main", "Ctrl+L"))
        self.action_Generate_Report.setText(_translate("MainWindow_Main", "Generuj raport"))
        self.action_Generate_Report.setShortcut(_translate("MainWindow_Main", "Ctrl+G"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_Main = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Main()
    ui.setupUi(MainWindow_Main)
    MainWindow_Main.show()
    sys.exit(app.exec())
