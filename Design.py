# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(763, 594)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 770, 601))
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
"background: #F9F9F9;\n"
"border: 1px solid #C4C4C3;\n"
"min-width: 20ex;\n"
"padding: 7px;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"background: #F9F9F9;\n"
"}\n"
"QTabBar::tab:selected {\n"
"background: white;\n"
"border-bottom: 0px solid #C2C7CB;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"margin-top: 3px; /* make non-selected tabs look smaller */\n"
"border-left:0px;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.table_coordinates = QtWidgets.QTableWidget(self.tab_3)
        self.table_coordinates.setGeometry(QtCore.QRect(20, 50, 251, 491))
        self.table_coordinates.setObjectName("table_coordinates")
        self.table_coordinates.setColumnCount(0)
        self.table_coordinates.setRowCount(0)
        self.groupBox_14 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_14.setGeometry(QtCore.QRect(560, 50, 181, 151))
        self.groupBox_14.setObjectName("groupBox_14")
        self.label_21 = QtWidgets.QLabel(self.groupBox_14)
        self.label_21.setGeometry(QtCore.QRect(20, 72, 71, 16))
        self.label_21.setObjectName("label_21")
        self.lbl_img_count = QtWidgets.QLabel(self.groupBox_14)
        self.lbl_img_count.setGeometry(QtCore.QRect(100, 70, 61, 21))
        self.lbl_img_count.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;")
        self.lbl_img_count.setObjectName("lbl_img_count")
        self.lbl_box_count = QtWidgets.QLabel(self.groupBox_14)
        self.lbl_box_count.setGeometry(QtCore.QRect(100, 100, 61, 21))
        self.lbl_box_count.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;")
        self.lbl_box_count.setObjectName("lbl_box_count")
        self.label_24 = QtWidgets.QLabel(self.groupBox_14)
        self.label_24.setGeometry(QtCore.QRect(20, 102, 71, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.groupBox_14)
        self.label_25.setGeometry(QtCore.QRect(20, 30, 75, 22))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.groupBox_14)
        self.label_26.setGeometry(QtCore.QRect(100, 31, 31, 21))
        self.label_26.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 5pt \"MS Shell Dlg 2\";")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_14)
        self.label_27.setGeometry(QtCore.QRect(130, 31, 31, 21))
        self.label_27.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: rgb(0,0,0);\n"
"font: 5pt \"MS Shell Dlg 2\";\n"
"border: 1px solid black;")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.tab_3)
        self.label_28.setGeometry(QtCore.QRect(20, 20, 221, 16))
        self.label_28.setObjectName("label_28")
        self.groupBox_15 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_15.setGeometry(QtCore.QRect(560, 220, 181, 201))
        self.groupBox_15.setObjectName("groupBox_15")
        self.label_29 = QtWidgets.QLabel(self.groupBox_15)
        self.label_29.setGeometry(QtCore.QRect(20, 35, 47, 10))
        self.label_29.setObjectName("label_29")
        self.lbl_ssim_score = QtWidgets.QLabel(self.groupBox_15)
        self.lbl_ssim_score.setGeometry(QtCore.QRect(20, 55, 141, 21))
        self.lbl_ssim_score.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;\n"
"padding-right:5px;")
        self.lbl_ssim_score.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_ssim_score.setObjectName("lbl_ssim_score")
        self.label_30 = QtWidgets.QLabel(self.groupBox_15)
        self.label_30.setGeometry(QtCore.QRect(20, 90, 47, 13))
        self.label_30.setObjectName("label_30")
        self.lbl_mse_score = QtWidgets.QLabel(self.groupBox_15)
        self.lbl_mse_score.setGeometry(QtCore.QRect(20, 110, 141, 21))
        self.lbl_mse_score.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;\n"
"padding-right:5px;")
        self.lbl_mse_score.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_mse_score.setObjectName("lbl_mse_score")
        self.lbl_psnr_score = QtWidgets.QLabel(self.groupBox_15)
        self.lbl_psnr_score.setGeometry(QtCore.QRect(20, 165, 141, 21))
        self.lbl_psnr_score.setStyleSheet("border: 1px solid black;\n"
"border-radius:5px;\n"
"padding-right:5px;")
        self.lbl_psnr_score.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_psnr_score.setObjectName("lbl_psnr_score")
        self.label_31 = QtWidgets.QLabel(self.groupBox_15)
        self.label_31.setGeometry(QtCore.QRect(20, 147, 45, 10))
        self.label_31.setObjectName("label_31")
        self.groupBox_16 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_16.setGeometry(QtCore.QRect(560, 430, 181, 111))
        self.groupBox_16.setObjectName("groupBox_16")
        self.btn_apply = QtWidgets.QPushButton(self.groupBox_16)
        self.btn_apply.setGeometry(QtCore.QRect(20, 63, 141, 31))
        self.btn_apply.setStyleSheet("border: 1px solid red;\n"
"color:red;\n"
"")
        self.btn_apply.setObjectName("btn_apply")
        self.btn_coordinates_import = QtWidgets.QPushButton(self.groupBox_16)
        self.btn_coordinates_import.setGeometry(QtCore.QRect(20, 27, 141, 31))
        self.btn_coordinates_import.setStyleSheet("border: 1px solid black;\n"
"color:black;\n"
"")
        self.btn_coordinates_import.setObjectName("btn_coordinates_import")
        self.img_position = QtWidgets.QGraphicsView(self.tab_3)
        self.img_position.setGeometry(QtCore.QRect(290, 230, 251, 201))
        self.img_position.setStyleSheet("")
        self.img_position.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_position.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_position.setObjectName("img_position")
        self.table_result = QtWidgets.QTableWidget(self.tab_3)
        self.table_result.setGeometry(QtCore.QRect(290, 50, 251, 151))
        self.table_result.setObjectName("table_result")
        self.table_result.setColumnCount(0)
        self.table_result.setRowCount(0)
        self.label_22 = QtWidgets.QLabel(self.tab_3)
        self.label_22.setGeometry(QtCore.QRect(290, 210, 71, 16))
        self.label_22.setObjectName("label_22")
        self.img_box = QtWidgets.QGraphicsView(self.tab_3)
        self.img_box.setGeometry(QtCore.QRect(290, 440, 121, 101))
        self.img_box.setStyleSheet("")
        self.img_box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_box.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_box.setObjectName("img_box")
        self.img_best = QtWidgets.QGraphicsView(self.tab_3)
        self.img_best.setGeometry(QtCore.QRect(420, 440, 121, 101))
        self.img_best.setStyleSheet("")
        self.img_best.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_best.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_best.setObjectName("img_best")
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        self.label_23.setGeometry(QtCore.QRect(290, 20, 71, 16))
        self.label_23.setObjectName("label_23")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Selective Search"))
        self.groupBox_14.setTitle(_translate("MainWindow", "B i l g i l e n d i r m e"))
        self.label_21.setText(_translate("MainWindow", "Resim Sayısı :"))
        self.lbl_img_count.setText(_translate("MainWindow", "-"))
        self.lbl_box_count.setText(_translate("MainWindow", "-"))
        self.label_24.setText(_translate("MainWindow", "Box Sayısı :"))
        self.label_25.setText(_translate("MainWindow", "Renklendirme :"))
        self.label_26.setText(_translate("MainWindow", "real"))
        self.label_27.setText(_translate("MainWindow", "sonuç"))
        self.label_28.setText(_translate("MainWindow", "R e f e r a n s  K o r d i n a t l a r :"))
        self.groupBox_15.setTitle(_translate("MainWindow", "K a r ş ı l a ş t ı r m a "))
        self.label_29.setText(_translate("MainWindow", "SSIM :"))
        self.lbl_ssim_score.setText(_translate("MainWindow", "-"))
        self.label_30.setText(_translate("MainWindow", "MSE :"))
        self.lbl_mse_score.setText(_translate("MainWindow", "-"))
        self.lbl_psnr_score.setText(_translate("MainWindow", "-"))
        self.label_31.setText(_translate("MainWindow", "PSNR :"))
        self.groupBox_16.setTitle(_translate("MainWindow", "İ ş l e m l e r"))
        self.btn_apply.setText(_translate("MainWindow", "U Y G U L A"))
        self.btn_coordinates_import.setText(_translate("MainWindow", "Y Ü K L E"))
        self.label_22.setText(_translate("MainWindow", "P o z i s y o n :"))
        self.label_23.setText(_translate("MainWindow", "S o n u ç :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "S e l e c t i ve  S e a r c h"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())