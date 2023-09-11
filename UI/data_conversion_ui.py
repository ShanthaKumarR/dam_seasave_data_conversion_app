import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from UI import icons

#self.frame.installEventFilter(self)
class Ui_Data_conversion(QWidget):
    def __init__(self):
        self.app = QApplication(sys.argv)
        QWidget.__init__(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Form")
        self.resize(967, 844)
        self.verticalLayout_3 = QVBoxLayout(self)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout_7.addWidget(self.label)


        self.horizontalLayout_4.addWidget(self.frame)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.data_conversion_settings = QPushButton(self)
        self.data_conversion_settings.setObjectName(u"data_conversion_settings")
        self.data_conversion_settings.setMinimumSize(QSize(28, 28))
        self.data_conversion_settings.setMaximumSize(QSize(28, 28))
        icon = QIcon()
        icon.addFile(u":/images/images/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.data_conversion_settings.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.data_conversion_settings)

        self.data_conversion_min = QPushButton(self)
        self.data_conversion_min.setObjectName(u"data_conversion_min")
        self.data_conversion_min.setMinimumSize(QSize(28, 28))
        self.data_conversion_min.setMaximumSize(QSize(28, 28))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.data_conversion_min.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.data_conversion_min)

        self.data_conversion_max = QPushButton(self)
        self.data_conversion_max.setObjectName(u"data_conversion_max")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.data_conversion_max.sizePolicy().hasHeightForWidth())
        self.data_conversion_max.setSizePolicy(sizePolicy1)
        self.data_conversion_max.setMinimumSize(QSize(28, 28))
        self.data_conversion_max.setMaximumSize(QSize(28, 28))
        icon2 = QIcon()
        icon2.addFile(u":/images/images/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.data_conversion_max.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.data_conversion_max)

        self.data_conversion_close = QPushButton(self)
        self.data_conversion_close.setObjectName(u"data_conversion_close")
        self.data_conversion_close.setMinimumSize(QSize(28, 28))
        self.data_conversion_close.setMaximumSize(QSize(28, 28))
        icon3 = QIcon()
        icon3.addFile(u":/images/images/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.data_conversion_close.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.data_conversion_close)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.groupBox_2 = QGroupBox(self)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_7 = QGroupBox(self.groupBox_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.xlxs_rb = QRadioButton(self.groupBox_7)
        self.xlxs_rb.setObjectName(u"xlxs_rb")

        self.horizontalLayout_6.addWidget(self.xlxs_rb)

        self.txt_rb = QRadioButton(self.groupBox_7)
        self.txt_rb.setObjectName(u"txt_rb")

        self.horizontalLayout_6.addWidget(self.txt_rb)

        self.csv_rb = QRadioButton(self.groupBox_7)
        self.csv_rb.setObjectName(u"csv_rb")

        self.horizontalLayout_6.addWidget(self.csv_rb)


        self.horizontalLayout_2.addWidget(self.groupBox_7)

        self.groupBox_9 = QGroupBox(self.groupBox_2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        self.gridLayout_12 = QGridLayout(self.groupBox_9)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.DC_MultiRB = QRadioButton(self.groupBox_9)
        self.DC_MultiRB.setObjectName(u"DC_MultiRB")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.DC_MultiRB.sizePolicy().hasHeightForWidth())
        self.DC_MultiRB.setSizePolicy(sizePolicy2)
        self.DC_MultiRB.setMinimumSize(QSize(0, 25))
        self.DC_MultiRB.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.DC_MultiRB.setFont(font1)

        self.gridLayout_12.addWidget(self.DC_MultiRB, 0, 1, 1, 1, Qt.AlignLeft)

        self.DC_SingleRB = QRadioButton(self.groupBox_9)
        self.DC_SingleRB.setObjectName(u"DC_SingleRB")
        self.DC_SingleRB.setMinimumSize(QSize(0, 0))
        self.DC_SingleRB.setFont(font1)

        self.gridLayout_12.addWidget(self.DC_SingleRB, 0, 0, 1, 1, Qt.AlignLeft)


        self.horizontalLayout_2.addWidget(self.groupBox_9)

        self.groupBox_6 = QGroupBox(self.groupBox_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.default_rb = QRadioButton(self.groupBox_6)
        self.default_rb.setObjectName(u"default_rb")

        self.verticalLayout_5.addWidget(self.default_rb)

        self.pangaerb = QRadioButton(self.groupBox_6)
        self.pangaerb.setObjectName(u"pangaerb")

        self.verticalLayout_5.addWidget(self.pangaerb)


        self.horizontalLayout_2.addWidget(self.groupBox_6)

        self.groupBox_11 = QGroupBox(self.groupBox_2)
        self.groupBox_11.setObjectName(u"groupBox_11")
        sizePolicy.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy)
        self.verticalLayout_49 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.QFlaga_checkBox = QRadioButton(self.groupBox_11)
        self.QFlaga_checkBox.setObjectName(u"QFlaga_checkBox")

        self.verticalLayout_49.addWidget(self.QFlaga_checkBox)

        self.QFlag_batch_of_file = QRadioButton(self.groupBox_11)
        self.QFlag_batch_of_file.setObjectName(u"QFlag_batch_of_file")

        self.verticalLayout_49.addWidget(self.QFlag_batch_of_file)

        self.QFlag_No = QRadioButton(self.groupBox_11)
        self.QFlag_No.setObjectName(u"QFlag_No")

        self.verticalLayout_49.addWidget(self.QFlag_No)


        self.horizontalLayout_2.addWidget(self.groupBox_11)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_8 = QGroupBox(self)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy3)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(9, -1, -1, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.label_DC_InputLB = QLabel(self.groupBox_8)
        self.label_DC_InputLB.setObjectName(u"label_DC_InputLB")
        self.label_DC_InputLB.setMinimumSize(QSize(75, 25))
        self.label_DC_InputLB.setFont(font1)

        self.gridLayout.addWidget(self.label_DC_InputLB, 0, 0, 1, 1)

        self.DC_InputLE = QLineEdit(self.groupBox_8)
        self.DC_InputLE.setObjectName(u"DC_InputLE")
        self.DC_InputLE.setMinimumSize(QSize(250, 25))
        self.DC_InputLE.setStyleSheet(u"")

        self.gridLayout.addWidget(self.DC_InputLE, 0, 1, 1, 1)

        self.DC_InputPB = QPushButton(self.groupBox_8)
        self.DC_InputPB.setObjectName(u"DC_InputPB")
        self.DC_InputPB.setMinimumSize(QSize(100, 0))
        self.DC_InputPB.setFont(font1)

        self.gridLayout.addWidget(self.DC_InputPB, 0, 2, 1, 1)

        self.update_file = QPushButton(self.groupBox_8)
        self.update_file.setObjectName(u"update_file")

        self.gridLayout.addWidget(self.update_file, 0, 3, 1, 1)

        self.DC_OutPutLB = QLabel(self.groupBox_8)
        self.DC_OutPutLB.setObjectName(u"DC_OutPutLB")
        self.DC_OutPutLB.setMinimumSize(QSize(85, 25))
        self.DC_OutPutLB.setFont(font1)

        self.gridLayout.addWidget(self.DC_OutPutLB, 1, 0, 1, 1)

        self.DC_OutputLE = QLineEdit(self.groupBox_8)
        self.DC_OutputLE.setObjectName(u"DC_OutputLE")
        self.DC_OutputLE.setMinimumSize(QSize(0, 25))
        self.DC_OutputLE.setStyleSheet(u"")

        self.gridLayout.addWidget(self.DC_OutputLE, 1, 1, 1, 1)

        self.DC_OutputPB = QPushButton(self.groupBox_8)
        self.DC_OutputPB.setObjectName(u"DC_OutputPB")
        self.DC_OutputPB.setMinimumSize(QSize(100, 0))
        self.DC_OutputPB.setMaximumSize(QSize(100, 16777215))
        self.DC_OutputPB.setFont(font1)
        self.DC_OutputPB.setStyleSheet(u"")

        self.gridLayout.addWidget(self.DC_OutputPB, 1, 2, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_25 = QFrame(self.groupBox_8)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_25)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_5 = QLabel(self.frame_25)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_46.addWidget(self.label_5, 0, Qt.AlignTop)

        self.frame_30 = QFrame(self.frame_25)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(0, 16777215))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)

        self.verticalLayout_46.addWidget(self.frame_30)

        self.frame_28 = QFrame(self.frame_25)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(0, 16777215))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)

        self.verticalLayout_46.addWidget(self.frame_28)


        self.horizontalLayout_5.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.groupBox_8)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_26)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.frame_26)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.frame_29 = QFrame(self.frame_26)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy3.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy3)
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_29)


        self.horizontalLayout_5.addWidget(self.frame_26)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addWidget(self.groupBox_8)

        self.groupBox = QGroupBox(self)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy4)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.progressBar = QProgressBar(self.groupBox)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy5)
        self.progressBar.setMinimumSize(QSize(0, 0))
        self.progressBar.setMaximumSize(QSize(16777215, 16777215))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"\n"
"  background-color : rgb(0,0,0)\n"
"}\n"
"QProgressBar::hover\n"
"                            {\n"
"                             background-color :#0b313e\n"
"                             }\n"
"")
        self.progressBar.setValue(24)

        self.horizontalLayout_7.addWidget(self.progressBar)

        self.DC_convertData_PB = QPushButton(self.groupBox)
        self.DC_convertData_PB.setObjectName(u"DC_convertData_PB")
        sizePolicy.setHeightForWidth(self.DC_convertData_PB.sizePolicy().hasHeightForWidth())
        self.DC_convertData_PB.setSizePolicy(sizePolicy)
        self.DC_convertData_PB.setMinimumSize(QSize(0, 0))
        self.DC_convertData_PB.setMaximumSize(QSize(100, 16777215))
        self.DC_convertData_PB.setFont(font1)
        self.DC_convertData_PB.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.DC_convertData_PB)

        self.cancelbtn = QPushButton(self.groupBox)
        self.cancelbtn.setObjectName(u"cancelbtn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.cancelbtn.sizePolicy().hasHeightForWidth())
        self.cancelbtn.setSizePolicy(sizePolicy6)

        self.horizontalLayout_7.addWidget(self.cancelbtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)


        self.verticalLayout.addWidget(self.groupBox)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_9.addWidget(self.label_2)

        self.Qsize_widget = QWidget(self)
        self.Qsize_widget.setObjectName(u"Qsize_widget")
        self.Qsize_widget.setMinimumSize(QSize(16, 16))
        self.Qsize_widget.setStyleSheet(u"background-image: url(:/images/images/cil-size-grip.png);")

        self.horizontalLayout_9.addWidget(self.Qsize_widget, 0, Qt.AlignRight)

        QSizeGrip(self.Qsize_widget)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
    
        self.frame.installEventFilter(self)
        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u" Data conversion", None))
        self.data_conversion_settings.setText("")
        self.data_conversion_min.setText("")
        self.data_conversion_max.setText("")
        self.data_conversion_close.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"settings", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Form", u"Output file", None))
        self.xlxs_rb.setText(QCoreApplication.translate("Form", u"xlxs", None))
        self.txt_rb.setText(QCoreApplication.translate("Form", u"txt", None))
        self.csv_rb.setText(QCoreApplication.translate("Form", u"Csv", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Form", u"Number of files", None))
        self.DC_MultiRB.setText(QCoreApplication.translate("Form", u"Folder", None))
        self.DC_SingleRB.setText(QCoreApplication.translate("Form", u"Files", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"Data Base Type", None))
        self.default_rb.setText(QCoreApplication.translate("Form", u"Default", None))
        self.pangaerb.setText(QCoreApplication.translate("Form", u"Pangae", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("Form", u"Quality flag", None))
        self.QFlaga_checkBox.setText(QCoreApplication.translate("Form", u"Q Flag - distinct", None))
        self.QFlag_batch_of_file.setText(QCoreApplication.translate("Form", u"Q Flag - similar group files ", None))
        self.QFlag_No.setText(QCoreApplication.translate("Form", u"No Q Flag", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Form", u"Raw file information", None))
        self.label_DC_InputLB.setText(QCoreApplication.translate("Form", u"Input File or Folder", None))
        self.DC_InputPB.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.update_file.setText(QCoreApplication.translate("Form", u"update", None))
        self.DC_OutPutLB.setText(QCoreApplication.translate("Form", u"Output Folder", None))
        self.DC_OutputPB.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Input Files / Input folder", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Output folder", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Convert data", None))
        self.DC_convertData_PB.setText(QCoreApplication.translate("Form", u"Convert ", None))
        self.cancelbtn.setText(QCoreApplication.translate("Form", u"Cancel conversion", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"DAM-IOW-V1.0", None))
        self.progressBar.setValue(0)
    # retranslateUi









        



    def eventFilter(self, obj, event) -> bool:
        
        if obj == self.frame:
            if event.type() == QEvent.MouseButtonRelease:
                if event.globalPos().y() < 10 and self.moved:
                    self.prevGeo = self.geometry()
                    self.showMaximized()
                    return True

            if event.type() == QEvent.MouseButtonDblClick:
                self.setWindowState(self.windowState() ^ Qt.WindowFullScreen)
                return True
            if event.type() == QEvent.MouseButtonPress:
                    self.oldPosition = event.globalPos()
            if event.type() == QEvent.MouseMove:
                delta = QPoint(event.globalPos() - self.oldPosition)
                self.move(self.x() + delta.x(), self.y() + delta.y())
                self.oldPosition = event.globalPos()
                self.moved = True
            else:
                return True
            
            return True

    