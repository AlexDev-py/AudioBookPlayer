"""

Окно запуска приложения.

WARNING! Файл был модифицирован после конвертации из startapp.ui,
повторная конвертация приведет к утрате важного функционала.

"""


from PyQt5 import QtCore, QtGui, QtWidgets


class UiStartApp(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(210, 240)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(
            "background-color: rgb(16, 14, 16);\n" "color: rgb(255, 255, 255);"
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 15, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.loading = QtWidgets.QLabel(self.centralwidget)
        self.loading.setMinimumSize(QtCore.QSize(115, 115))
        self.loading.setAlignment(QtCore.Qt.AlignCenter)
        self.loading.setObjectName("loading")
        self.verticalLayout_2.addWidget(self.loading)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.status = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.status.setFont(font)
        self.status.setStyleSheet("border: none;")
        self.status.setMidLineWidth(-3)
        self.status.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.status.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.status.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.status.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.status.setObjectName("status")
        self.verticalLayout.addWidget(self.status)
        self.made_by = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.made_by.setFont(font)
        self.made_by.setAlignment(QtCore.Qt.AlignCenter)
        self.made_by.setObjectName("made_by")
        self.verticalLayout.addWidget(self.made_by)
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ABPlayer"))
        self.status.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Arial'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
                '<p align="center" style="-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;"><br /></p></body></html>',
            )
        )
        self.made_by.setText(_translate("MainWindow", "by AlexDev"))
