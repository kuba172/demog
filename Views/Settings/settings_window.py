# Form implementation generated from reading ui file '.\settings-window.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Settings(object):
    def setupUi(self, MainWindow_Settings):
        MainWindow_Settings.setObjectName("MainWindow_Settings")
        MainWindow_Settings.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        MainWindow_Settings.resize(800, 600)
        MainWindow_Settings.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow_Settings.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow_Settings)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget_Category_List = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget_Category_List.setMaximumSize(QtCore.QSize(125, 16777215))
        self.listWidget_Category_List.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.listWidget_Category_List.setObjectName("listWidget_Category_List")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_Category_List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_Category_List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_Category_List.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget_Category_List)
        self.stackedWidget_Content = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget_Content.setObjectName("stackedWidget_Content")
        self.General = QtWidgets.QWidget()
        self.General.setObjectName("General")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.General)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.General)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 629, 528))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents)
        self.groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox_Language = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox_Language.setObjectName("comboBox_Language")
        self.verticalLayout.addWidget(self.comboBox_Language)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox_Theme = QtWidgets.QComboBox(parent=self.groupBox_2)
        self.comboBox_Theme.setObjectName("comboBox_Theme")
        self.verticalLayout_2.addWidget(self.comboBox_Theme)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.checkBox_Use_Custom_Theme = QtWidgets.QCheckBox(parent=self.groupBox_3)
        self.checkBox_Use_Custom_Theme.setObjectName("checkBox_Use_Custom_Theme")
        self.horizontalLayout_10.addWidget(self.checkBox_Use_Custom_Theme)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.checkBox_Use_Secondary_Colors = QtWidgets.QCheckBox(parent=self.groupBox_3)
        self.checkBox_Use_Secondary_Colors.setEnabled(False)
        self.checkBox_Use_Secondary_Colors.setObjectName("checkBox_Use_Secondary_Colors")
        self.horizontalLayout_10.addWidget(self.checkBox_Use_Secondary_Colors)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.pushButton_Primary_Color = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_Primary_Color.setEnabled(False)
        self.pushButton_Primary_Color.setText("")
        self.pushButton_Primary_Color.setObjectName("pushButton_Primary_Color")
        self.horizontalLayout_3.addWidget(self.pushButton_Primary_Color)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.pushButton_Primary_Light_Color = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_Primary_Light_Color.setEnabled(False)
        self.pushButton_Primary_Light_Color.setText("")
        self.pushButton_Primary_Light_Color.setObjectName("pushButton_Primary_Light_Color")
        self.horizontalLayout_4.addWidget(self.pushButton_Primary_Light_Color)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.pushButton_Secondary_Color = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_Secondary_Color.setEnabled(False)
        self.pushButton_Secondary_Color.setText("")
        self.pushButton_Secondary_Color.setObjectName("pushButton_Secondary_Color")
        self.horizontalLayout_5.addWidget(self.pushButton_Secondary_Color)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.pushButton_Secondary_Light_Color = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_Secondary_Light_Color.setEnabled(False)
        self.pushButton_Secondary_Light_Color.setText("")
        self.pushButton_Secondary_Light_Color.setObjectName("pushButton_Secondary_Light_Color")
        self.horizontalLayout_6.addWidget(self.pushButton_Secondary_Light_Color)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.pushButton_Secondary_Dark_Color = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_Secondary_Dark_Color.setEnabled(False)
        self.pushButton_Secondary_Dark_Color.setText("")
        self.pushButton_Secondary_Dark_Color.setObjectName("pushButton_Secondary_Dark_Color")
        self.horizontalLayout_7.addWidget(self.pushButton_Secondary_Dark_Color)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.pushButton_Primary_Text_Color = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_Primary_Text_Color.setEnabled(False)
        self.pushButton_Primary_Text_Color.setText("")
        self.pushButton_Primary_Text_Color.setObjectName("pushButton_Primary_Text_Color")
        self.horizontalLayout_8.addWidget(self.pushButton_Primary_Text_Color)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.pushButton_Secondary_Text_Color = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_Secondary_Text_Color.setEnabled(False)
        self.pushButton_Secondary_Text_Color.setText("")
        self.pushButton_Secondary_Text_Color.setObjectName("pushButton_Secondary_Text_Color")
        self.horizontalLayout_9.addWidget(self.pushButton_Secondary_Text_Color)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_11.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_7.addWidget(self.scrollArea)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButton_Close_General = QtWidgets.QPushButton(parent=self.General)
        self.pushButton_Close_General.setObjectName("pushButton_Close_General")
        self.horizontalLayout_2.addWidget(self.pushButton_Close_General)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.stackedWidget_Content.addWidget(self.General)
        self.Report = QtWidgets.QWidget()
        self.Report.setObjectName("Report")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.Report)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.Report)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 631, 530))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.groupBox_How_Many_Files = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents_2)
        self.groupBox_How_Many_Files.setObjectName("groupBox_How_Many_Files")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.groupBox_How_Many_Files)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.radioButton_In_One_File = QtWidgets.QRadioButton(parent=self.groupBox_How_Many_Files)
        self.radioButton_In_One_File.setChecked(True)
        self.radioButton_In_One_File.setObjectName("radioButton_In_One_File")
        self.verticalLayout_12.addWidget(self.radioButton_In_One_File)
        self.radioButton_In_Separate_Files = QtWidgets.QRadioButton(parent=self.groupBox_How_Many_Files)
        self.radioButton_In_Separate_Files.setObjectName("radioButton_In_Separate_Files")
        self.verticalLayout_12.addWidget(self.radioButton_In_Separate_Files)
        self.verticalLayout_15.addWidget(self.groupBox_How_Many_Files)
        self.groupBox_Model_Prediction = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents_2)
        self.groupBox_Model_Prediction.setObjectName("groupBox_Model_Prediction")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_Model_Prediction)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.comboBox_Model_Prediction = QtWidgets.QComboBox(parent=self.groupBox_Model_Prediction)
        self.comboBox_Model_Prediction.setObjectName("comboBox_Model_Prediction")
        self.comboBox_Model_Prediction.addItem("")
        self.comboBox_Model_Prediction.addItem("")
        self.comboBox_Model_Prediction.addItem("")
        self.verticalLayout_13.addWidget(self.comboBox_Model_Prediction)
        self.verticalLayout_15.addWidget(self.groupBox_Model_Prediction)
        self.groupBox_Report_Elements = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents_2)
        self.groupBox_Report_Elements.setObjectName("groupBox_Report_Elements")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.groupBox_Report_Elements)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.checkBox_1_Table_Of_Contents = QtWidgets.QCheckBox(parent=self.groupBox_Report_Elements)
        self.checkBox_1_Table_Of_Contents.setChecked(True)
        self.checkBox_1_Table_Of_Contents.setObjectName("checkBox_1_Table_Of_Contents")
        self.verticalLayout_14.addWidget(self.checkBox_1_Table_Of_Contents)
        self.checkBox_2_Summary = QtWidgets.QCheckBox(parent=self.groupBox_Report_Elements)
        self.checkBox_2_Summary.setChecked(True)
        self.checkBox_2_Summary.setObjectName("checkBox_2_Summary")
        self.verticalLayout_14.addWidget(self.checkBox_2_Summary)
        self.checkBox_3_Introduction = QtWidgets.QCheckBox(parent=self.groupBox_Report_Elements)
        self.checkBox_3_Introduction.setChecked(True)
        self.checkBox_3_Introduction.setObjectName("checkBox_3_Introduction")
        self.verticalLayout_14.addWidget(self.checkBox_3_Introduction)
        self.checkBox_4_Methodology = QtWidgets.QCheckBox(parent=self.groupBox_Report_Elements)
        self.checkBox_4_Methodology.setChecked(True)
        self.checkBox_4_Methodology.setObjectName("checkBox_4_Methodology")
        self.verticalLayout_14.addWidget(self.checkBox_4_Methodology)
        self.checkBox_6_Annual_Analysis = QtWidgets.QCheckBox(parent=self.groupBox_Report_Elements)
        self.checkBox_6_Annual_Analysis.setChecked(True)
        self.checkBox_6_Annual_Analysis.setObjectName("checkBox_6_Annual_Analysis")
        self.verticalLayout_14.addWidget(self.checkBox_6_Annual_Analysis)
        self.checkBox_10_Report_Summary = QtWidgets.QCheckBox(parent=self.groupBox_Report_Elements)
        self.checkBox_10_Report_Summary.setChecked(True)
        self.checkBox_10_Report_Summary.setObjectName("checkBox_10_Report_Summary")
        self.verticalLayout_14.addWidget(self.checkBox_10_Report_Summary)
        self.checkBox_11_References = QtWidgets.QCheckBox(parent=self.groupBox_Report_Elements)
        self.checkBox_11_References.setChecked(True)
        self.checkBox_11_References.setObjectName("checkBox_11_References")
        self.verticalLayout_14.addWidget(self.checkBox_11_References)
        self.verticalLayout_15.addWidget(self.groupBox_Report_Elements)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_11.addWidget(self.scrollArea_2)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem4)
        self.pushButton_Close_Report = QtWidgets.QPushButton(parent=self.Report)
        self.pushButton_Close_Report.setObjectName("pushButton_Close_Report")
        self.horizontalLayout_14.addWidget(self.pushButton_Close_Report)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem5)
        self.verticalLayout_11.addLayout(self.horizontalLayout_14)
        self.stackedWidget_Content.addWidget(self.Report)
        self.Map = QtWidgets.QWidget()
        self.Map.setObjectName("Map")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.Map)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.scrollArea_3 = QtWidgets.QScrollArea(parent=self.Map)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 631, 530))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_13.addWidget(self.label_8)
        self.pushButton_Map_Color = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.pushButton_Map_Color.setText("")
        self.pushButton_Map_Color.setObjectName("pushButton_Map_Color")
        self.horizontalLayout_13.addWidget(self.pushButton_Map_Color)
        self.verticalLayout_10.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_17.addWidget(self.label_11)
        self.pushButton_Border_Map_Color = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.pushButton_Border_Map_Color.setText("")
        self.pushButton_Border_Map_Color.setObjectName("pushButton_Border_Map_Color")
        self.horizontalLayout_17.addWidget(self.pushButton_Border_Map_Color)
        self.verticalLayout_10.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_15.addWidget(self.label_9)
        self.pushButton_Selection_Color = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.pushButton_Selection_Color.setText("")
        self.pushButton_Selection_Color.setObjectName("pushButton_Selection_Color")
        self.horizontalLayout_15.addWidget(self.pushButton_Selection_Color)
        self.verticalLayout_10.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_16.addWidget(self.label_10)
        self.pushButton_Hover_Color = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.pushButton_Hover_Color.setText("")
        self.pushButton_Hover_Color.setObjectName("pushButton_Hover_Color")
        self.horizontalLayout_16.addWidget(self.pushButton_Hover_Color)
        self.verticalLayout_10.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_13 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_19.addWidget(self.label_13)
        self.spinBox_Map_Border_Size = QtWidgets.QSpinBox(parent=self.groupBox_4)
        self.spinBox_Map_Border_Size.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spinBox_Map_Border_Size.setMinimum(1)
        self.spinBox_Map_Border_Size.setMaximum(10)
        self.spinBox_Map_Border_Size.setObjectName("spinBox_Map_Border_Size")
        self.horizontalLayout_19.addWidget(self.spinBox_Map_Border_Size)
        self.verticalLayout_10.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_18.addWidget(self.label_12)
        self.spinBox_Selection_Border_Size = QtWidgets.QSpinBox(parent=self.groupBox_4)
        self.spinBox_Selection_Border_Size.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spinBox_Selection_Border_Size.setMinimum(1)
        self.spinBox_Selection_Border_Size.setMaximum(10)
        self.spinBox_Selection_Border_Size.setObjectName("spinBox_Selection_Border_Size")
        self.horizontalLayout_18.addWidget(self.spinBox_Selection_Border_Size)
        self.verticalLayout_10.addLayout(self.horizontalLayout_18)
        self.verticalLayout_16.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents_3)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_14 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_20.addWidget(self.label_14)
        self.spinBox_Default_Map_Scale = QtWidgets.QSpinBox(parent=self.groupBox_5)
        self.spinBox_Default_Map_Scale.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spinBox_Default_Map_Scale.setMinimum(50)
        self.spinBox_Default_Map_Scale.setMaximum(1000)
        self.spinBox_Default_Map_Scale.setProperty("value", 100)
        self.spinBox_Default_Map_Scale.setObjectName("spinBox_Default_Map_Scale")
        self.horizontalLayout_20.addWidget(self.spinBox_Default_Map_Scale)
        self.verticalLayout_17.addLayout(self.horizontalLayout_20)
        self.verticalLayout_16.addWidget(self.groupBox_5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_16.addItem(spacerItem6)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_9.addWidget(self.scrollArea_3)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.pushButton_Close_map = QtWidgets.QPushButton(parent=self.Map)
        self.pushButton_Close_map.setObjectName("pushButton_Close_map")
        self.horizontalLayout_12.addWidget(self.pushButton_Close_map)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem8)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        self.stackedWidget_Content.addWidget(self.Map)
        self.horizontalLayout.addWidget(self.stackedWidget_Content)
        MainWindow_Settings.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_Settings)
        self.stackedWidget_Content.setCurrentIndex(1)
        self.checkBox_Use_Custom_Theme.toggled['bool'].connect(self.pushButton_Primary_Color.setEnabled) # type: ignore
        self.checkBox_Use_Custom_Theme.toggled['bool'].connect(self.pushButton_Secondary_Text_Color.setEnabled) # type: ignore
        self.listWidget_Category_List.currentRowChanged['int'].connect(self.stackedWidget_Content.setCurrentIndex) # type: ignore
        self.checkBox_Use_Custom_Theme.toggled['bool'].connect(self.pushButton_Primary_Text_Color.setEnabled) # type: ignore
        self.checkBox_Use_Custom_Theme.toggled['bool'].connect(self.pushButton_Secondary_Dark_Color.setEnabled) # type: ignore
        self.checkBox_Use_Custom_Theme.toggled['bool'].connect(self.pushButton_Secondary_Color.setEnabled) # type: ignore
        self.pushButton_Close_General.clicked.connect(MainWindow_Settings.close) # type: ignore
        self.checkBox_Use_Custom_Theme.toggled['bool'].connect(self.comboBox_Theme.setDisabled) # type: ignore
        self.checkBox_Use_Custom_Theme.toggled['bool'].connect(self.pushButton_Primary_Light_Color.setEnabled) # type: ignore
        self.checkBox_Use_Custom_Theme.toggled['bool'].connect(self.pushButton_Secondary_Light_Color.setEnabled) # type: ignore
        self.checkBox_Use_Custom_Theme.toggled['bool'].connect(self.checkBox_Use_Secondary_Colors.setEnabled) # type: ignore
        self.pushButton_Close_Report.clicked.connect(MainWindow_Settings.close) # type: ignore
        self.pushButton_Close_map.clicked.connect(MainWindow_Settings.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Settings)

    def retranslateUi(self, MainWindow_Settings):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Settings.setWindowTitle(_translate("MainWindow_Settings", "Ustawienia"))
        __sortingEnabled = self.listWidget_Category_List.isSortingEnabled()
        self.listWidget_Category_List.setSortingEnabled(False)
        item = self.listWidget_Category_List.item(0)
        item.setText(_translate("MainWindow_Settings", "Ogólne"))
        item = self.listWidget_Category_List.item(1)
        item.setText(_translate("MainWindow_Settings", "Raport"))
        item = self.listWidget_Category_List.item(2)
        item.setText(_translate("MainWindow_Settings", "Mapa"))
        self.listWidget_Category_List.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle(_translate("MainWindow_Settings", "Język interfejsu"))
        self.groupBox_2.setTitle(_translate("MainWindow_Settings", "Motyw interfejsu"))
        self.groupBox_3.setTitle(_translate("MainWindow_Settings", "Własny motyw"))
        self.checkBox_Use_Custom_Theme.setText(_translate("MainWindow_Settings", "Własny"))
        self.checkBox_Use_Secondary_Colors.setText(_translate("MainWindow_Settings", "Użyj kolorów dodatkowych"))
        self.label.setText(_translate("MainWindow_Settings", "Kolor podstawowy"))
        self.label_2.setText(_translate("MainWindow_Settings", "Podstawowy jasny kolor"))
        self.label_3.setText(_translate("MainWindow_Settings", "Kolor dodatkowy"))
        self.label_4.setText(_translate("MainWindow_Settings", "Dodatkowy jasny kolor"))
        self.label_5.setText(_translate("MainWindow_Settings", "Dodatkowy ciemny kolor"))
        self.label_6.setText(_translate("MainWindow_Settings", "Podstawowy kolor tekstu"))
        self.label_7.setText(_translate("MainWindow_Settings", "Dodatkowy kolor tekstu"))
        self.pushButton_Close_General.setText(_translate("MainWindow_Settings", "Zamknij"))
        self.groupBox_How_Many_Files.setTitle(_translate("MainWindow_Settings", "Wynik raportu dla wybranych lokalizacji"))
        self.radioButton_In_One_File.setText(_translate("MainWindow_Settings", "w jednym pliku wynikowym"))
        self.radioButton_In_Separate_Files.setText(_translate("MainWindow_Settings", "w osobnych plikach wynikowych"))
        self.groupBox_Model_Prediction.setTitle(_translate("MainWindow_Settings", "Model predykcji"))
        self.comboBox_Model_Prediction.setItemText(0, _translate("MainWindow_Settings", "Random Forest Regression"))
        self.comboBox_Model_Prediction.setItemText(1, _translate("MainWindow_Settings", "Polynomial Regression"))
        self.comboBox_Model_Prediction.setItemText(2, _translate("MainWindow_Settings", "Linear Regression"))
        self.groupBox_Report_Elements.setTitle(_translate("MainWindow_Settings", "Elementy raportu"))
        self.checkBox_1_Table_Of_Contents.setText(_translate("MainWindow_Settings", "Spis treści"))
        self.checkBox_2_Summary.setText(_translate("MainWindow_Settings", "Streszczenie"))
        self.checkBox_3_Introduction.setText(_translate("MainWindow_Settings", "Wprowadzenie"))
        self.checkBox_4_Methodology.setText(_translate("MainWindow_Settings", "Metodologia"))
        self.checkBox_6_Annual_Analysis.setText(_translate("MainWindow_Settings", "Analiza roczna"))
        self.checkBox_10_Report_Summary.setText(_translate("MainWindow_Settings", "Podsumowanie"))
        self.checkBox_11_References.setText(_translate("MainWindow_Settings", "Referencje"))
        self.pushButton_Close_Report.setText(_translate("MainWindow_Settings", "Zamknij"))
        self.groupBox_4.setTitle(_translate("MainWindow_Settings", "Mapa"))
        self.label_8.setText(_translate("MainWindow_Settings", "Kolor tła mapy"))
        self.label_11.setText(_translate("MainWindow_Settings", "Kolor obramowania mapy"))
        self.label_9.setText(_translate("MainWindow_Settings", "Kolor zazaczenia"))
        self.label_10.setText(_translate("MainWindow_Settings", "Kolor najechania "))
        self.label_13.setText(_translate("MainWindow_Settings", "Rozmiar obramowania mapy"))
        self.label_12.setText(_translate("MainWindow_Settings", "Rozmiar obramowania zaznaczenia"))
        self.groupBox_5.setTitle(_translate("MainWindow_Settings", "Wartości początkowe mapy"))
        self.label_14.setText(_translate("MainWindow_Settings", "Skala mapy"))
        self.pushButton_Close_map.setText(_translate("MainWindow_Settings", "Zamknij"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_Settings = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Settings()
    ui.setupUi(MainWindow_Settings)
    MainWindow_Settings.show()
    sys.exit(app.exec())
