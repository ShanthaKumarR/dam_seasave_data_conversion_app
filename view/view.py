from UI.data_conversion_ui import Ui_Data_conversion
import sys
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout
from PyQt5 import QtCore
from qt_material import apply_stylesheet, QtStyleTools, list_themes

color_dict = {'dark_amber':'#ffd740', 'dark_blue':'#448aff', 'dark_cyan':'#4dd0e1', 'dark_lightgreen':'#8bc34a', 'dark_pink': '#ff4081', 'dark_purple':'#ab47bc', 'dark_red':'#ff1744',\
        'dark_teal':'#1de9b6', 'dark_yellow':'#ffff00', 'light_blue':'#2979ff', 'light_amber':'#ffc400', 'light_blue_500':'#03a9f4','light_cyan':'#00e5ff', 'light_cyan_500':'#00bcd4','light_lightgreen':'#64dd17', \
        'light_lightgreen_500':'#8bc34a', 'light_orange':'#ff3d00','light_pink':'#ff4081', 'light_pink_500':'#e91e63','light_purple':'#e040fb', 'light_purple_500':'#9c27b0', 'light_red':'#ff1744',\
        'light_red_500':'#f44336', 'light_teal':'#1de9b6', 'light_teal_500':'#009688', 'light_yellow':'#ffea00'}

class View:
    def __init__(self):
        self.data_converstion_ui = Ui_Data_conversion()
        self.set_app_style_sheet(header_color = '#448aff', color = 'dark_blue.xml')
        #self.theme_option()

    def set_app_style_sheet(self, header_color, color):
        self.data_converstion_ui.label.setStyleSheet('background-color:'+header_color)
        #self.data_converstion_ui..setStyleSheet('background-color: #448aff')
        extra = {'density_scale': '0',}
        
        apply_stylesheet(self.data_converstion_ui, color, invert_secondary=True, extra=extra)

    
    def data_conversion_controls(self, controller):
        self.data_converstion_ui.DC_InputPB.clicked.connect(controller.predict_single_or_multiple_file)
        self.data_converstion_ui.DC_OutputPB.clicked.connect(lambda:controller.getOutPutDirpath(self.data_converstion_ui.DC_OutputLE, obj=self.data_converstion_ui))
        #self.data_converstion_ui.QFlaga_checkBox.setChecked(True)
        self.data_converstion_ui.DC_SingleRB.clicked.connect(controller.assign_file_or_folder)
        self.data_converstion_ui.DC_MultiRB.clicked.connect(controller.assign_file_or_folder)

        self.data_converstion_ui.default_rb.clicked.connect(controller.assign_database_type)

        self.data_converstion_ui.pangaerb.clicked.connect(controller.assign_database_type)

        self.data_converstion_ui.DC_convertData_PB.clicked.connect(controller.start_data_conversion)

        self.data_converstion_ui.csv_rb.clicked.connect(controller.assign_output_file_format)
        self.data_converstion_ui.txt_rb.clicked.connect(controller.assign_output_file_format)
        self.data_converstion_ui.xlxs_rb.clicked.connect(controller.assign_output_file_format)

        self.data_converstion_ui.data_conversion_close.clicked.connect(controller.data_conversion_on_close_run)
        
        self.data_converstion_ui.update_file.clicked.connect(controller.update_file_names)
        self.data_converstion_ui.data_conversion_max.clicked.connect(self.MaximizeWindow)
        self.data_converstion_ui.data_conversion_min.clicked.connect(self.MinimusedWindow)
        self.data_converstion_ui.data_conversion_settings.clicked.connect(self.theme_option)

    def MaximizeWindow(self):
        if self.data_converstion_ui.isMaximized():
            self.data_converstion_ui.showNormal()
           
        else:
            self.data_converstion_ui.showMaximized()

    def normalWindow(self):
        self.data_converstion_ui.showNormal()

    def MinimusedWindow(self):
        self.data_converstion_ui.showMinimized()

    def theme_option(self):
        self.theme = QDialog()
        #self.theme.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Vbox_layout = QVBoxLayout(self.theme)
        Themes = list_themes()
        self.Theme_buttons = [QPushButton(self.theme) for _ in range(len(Themes))]
        [btn.setText(name.split('.')[0]) for btn, name in zip(self.Theme_buttons, Themes)]
        [btn.setObjectName(name.split('.')[0]) for btn, name in zip(self.Theme_buttons, Themes)]
        self.theme_button_color(self.Theme_buttons)
        [Vbox_layout.addWidget(btn)   for btn in self.Theme_buttons]
        [button.clicked.connect(lambda:self.theme_button_clicke_action()) for button in self.Theme_buttons]
        self.theme.exec_()
    
    def theme_button_clicke_action(self):
        theme = self.data_converstion_ui.sender().objectName()+'.xml'
        self.set_app_style_sheet(color_dict[theme.split('.')[0]], theme)
       
    def theme_button_color(self, theme_buttons):
        try:
            [btn.setStyleSheet("background-color: "+ color_dict[btn.objectName()]) for btn in theme_buttons]
        except:
            pass
           
            

           