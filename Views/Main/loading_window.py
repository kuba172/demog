# Form implementation generated from reading ui file '.\loading-window.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Loading(object):
    def setupUi(self, Dialog_Loading):
        Dialog_Loading.setObjectName("Dialog_Loading")
        Dialog_Loading.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        Dialog_Loading.resize(666, 143)
        Dialog_Loading.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        Dialog_Loading.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog_Loading)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(parent=Dialog_Loading)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Static_Text = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_Static_Text.setFont(font)
        self.label_Static_Text.setStyleSheet("QLabel {font-size: 24pt;}")
        self.label_Static_Text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Static_Text.setObjectName("label_Static_Text")
        self.verticalLayout.addWidget(self.label_Static_Text)
        self.label_Dynamic_Text = QtWidgets.QLabel(parent=self.frame)
        self.label_Dynamic_Text.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_Dynamic_Text.setFont(font)
        self.label_Dynamic_Text.setStyleSheet("QLabel {font-size: 20pt;}")
        self.label_Dynamic_Text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Dynamic_Text.setObjectName("label_Dynamic_Text")
        self.verticalLayout.addWidget(self.label_Dynamic_Text)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addWidget(self.frame)

        self.retranslateUi(Dialog_Loading)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Loading)

    def retranslateUi(self, Dialog_Loading):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Loading.setWindowTitle(_translate("Dialog_Loading", "Genrowanie wyników..."))
        self.label_Static_Text.setText(_translate("Dialog_Loading", "Trwa generowanie wyników"))
        self.label_Dynamic_Text.setText(_translate("Dialog_Loading", "Proszę czekać, może to potrwać nawet kilka minut..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Loading = QtWidgets.QDialog()
    ui = Ui_Dialog_Loading()
    ui.setupUi(Dialog_Loading)
    Dialog_Loading.show()
    sys.exit(app.exec())
