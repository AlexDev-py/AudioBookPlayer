"""

Виджет книги.

WARNING! Файл был модифицирован после конвертации из book.ui,
повторная конвертация приведет к утрате важного функционала.

"""

from PyQt5 import QtCore, QtGui, QtWidgets


class UiBook(object):
    def setupUi(self, Book):
        Book.setObjectName("Book")
        Book.resize(881, 240)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Book.sizePolicy().hasHeightForWidth())
        Book.setSizePolicy(sizePolicy)
        Book.setMinimumSize(QtCore.QSize(750, 0))
        Book.setMaximumSize(QtCore.QSize(16777215, 240))
        self.verticalLayout = QtWidgets.QVBoxLayout(Book)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Book)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.cover = QtWidgets.QLabel(self.frame)
        self.cover.setMinimumSize(QtCore.QSize(200, 200))
        self.cover.setAlignment(QtCore.Qt.AlignCenter)
        self.cover.setObjectName("cover")
        self.horizontalLayout_7.addWidget(self.cover)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setContentsMargins(3, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titleLabel = QtWidgets.QLabel(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout_2.addWidget(self.titleLabel)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.inProcessIcon = QtWidgets.QLabel(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.inProcessIcon.sizePolicy().hasHeightForWidth()
        )
        self.inProcessIcon.setSizePolicy(sizePolicy)
        self.inProcessIcon.setText("")
        self.inProcessIcon.setPixmap(QtGui.QPixmap(":/other/clock.svg"))
        self.inProcessIcon.setObjectName("inProcessIcon")
        self.horizontalLayout_8.addWidget(self.inProcessIcon)
        self.finishedIcon = QtWidgets.QLabel(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finishedIcon.sizePolicy().hasHeightForWidth())
        self.finishedIcon.setSizePolicy(sizePolicy)
        self.finishedIcon.setText("")
        self.finishedIcon.setPixmap(QtGui.QPixmap(":/other/check.svg"))
        self.finishedIcon.setObjectName("finishedIcon")
        self.horizontalLayout_8.addWidget(self.finishedIcon)
        self.progressLabel = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.progressLabel.setFont(font)
        self.progressLabel.setObjectName("progressLabel")
        self.horizontalLayout_8.addWidget(self.progressLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6.addWidget(self.frame_9)
        spacerItem = QtWidgets.QSpacerItem(
            155, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_6.addItem(spacerItem)
        self.btnsFtame = QtWidgets.QFrame(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnsFtame.sizePolicy().hasHeightForWidth())
        self.btnsFtame.setSizePolicy(sizePolicy)
        self.btnsFtame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btnsFtame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btnsFtame.setObjectName("btnsFtame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.btnsFtame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.toggleFavoriteBtn = QtWidgets.QPushButton(self.btnsFtame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.toggleFavoriteBtn.sizePolicy().hasHeightForWidth()
        )
        self.toggleFavoriteBtn.setSizePolicy(sizePolicy)
        self.toggleFavoriteBtn.setMinimumSize(QtCore.QSize(45, 45))
        self.toggleFavoriteBtn.setMaximumSize(QtCore.QSize(45, 45))
        self.toggleFavoriteBtn.setText("")
        self.toggleFavoriteBtn.setIcon(QtGui.QIcon(":/other/star.svg"))
        self.toggleFavoriteBtn.setIconSize(QtCore.QSize(30, 30))
        self.toggleFavoriteBtn.setObjectName("toggleFavoriteBtn")
        self.horizontalLayout_5.addWidget(self.toggleFavoriteBtn)
        self.deleteBtn = QtWidgets.QPushButton(self.btnsFtame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteBtn.sizePolicy().hasHeightForWidth())
        self.deleteBtn.setSizePolicy(sizePolicy)
        self.deleteBtn.setMinimumSize(QtCore.QSize(45, 45))
        self.deleteBtn.setMaximumSize(QtCore.QSize(45, 45))
        self.deleteBtn.setText("")
        self.deleteBtn.setIcon(QtGui.QIcon(":/other/trash.svg"))
        self.deleteBtn.setIconSize(QtCore.QSize(30, 30))
        self.deleteBtn.setObjectName("deleteBtn")
        self.horizontalLayout_5.addWidget(self.deleteBtn)
        self.horizontalLayout_6.addWidget(self.btnsFtame)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.description = QtWidgets.QTextEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.description.setFont(font)
        self.description.setStyleSheet(
            "QTextEdit, QTextEdit * {\n"
            "    border: none;\n"
            "    margin-left: -10px;\n"
            "    padding-left: -10px;\n"
            "}"
        )
        self.description.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.description.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.description.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.description.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.description.setObjectName("description")
        self.verticalLayout_3.addWidget(self.description)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(4, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/other/person.svg"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.authorLabel = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.authorLabel.setFont(font)
        self.authorLabel.setObjectName("authorLabel")
        self.horizontalLayout.addWidget(self.authorLabel)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/other/mic.svg"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.readerLabel = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.readerLabel.setFont(font)
        self.readerLabel.setObjectName("readerLabel")
        self.horizontalLayout_2.addWidget(self.readerLabel)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/other/clock.svg"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.durationLabel = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.durationLabel.setFont(font)
        self.durationLabel.setObjectName("durationLabel")
        self.horizontalLayout_4.addWidget(self.durationLabel)
        self.horizontalLayout_3.addWidget(self.frame_6)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.horizontalLayout_7.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Book)
        QtCore.QMetaObject.connectSlotsByName(Book)

    def retranslateUi(self, Book):
        _translate = QtCore.QCoreApplication.translate
        Book.setWindowTitle(_translate("Book", "Form"))
        self.titleLabel.setText(_translate("Book", "Автор - Название"))
        self.progressLabel.setText(_translate("Book", "0% прослушано"))
        self.toggleFavoriteBtn.setToolTip(_translate("Book", "Добавить в избранное"))
        self.deleteBtn.setToolTip(_translate("Book", "Удалить книгу"))
        self.description.setMarkdown(
            _translate(
                "Book",
                "Печальный рассказ о доле молодого человека, чье детство было сытым и\n"
                "счастливым, а будущее рисовалось безоблачным и зажиточным. Но судьба\n"
                "безжалостна, и теперь ему приходится зарабатывать на хлеб нелегким извозчичьим\n"
                "трудом. И невдомёк ему, что...\n"
                "\n"
                "",
            )
        )
        self.description.setHtml(
            _translate(
                "Book",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Печальный рассказ о доле молодого человека, чье детство было сытым и счастливым, а будущее рисовалось безоблачным и зажиточным. Но судьба безжалостна, и теперь ему приходится зарабатывать на хлеб нелегким извозчичьим трудом. И невдомёк ему, что...</p></body></html>',
            )
        )
        self.authorLabel.setText(_translate("Book", "author"))
        self.readerLabel.setText(_translate("Book", "reader"))
        self.durationLabel.setText(_translate("Book", "duration"))
