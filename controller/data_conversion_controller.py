
from queue import Queue
from threading import Thread, Lock
from typing import Callable
from PyQt5.QtWidgets import QFileDialog, QFileSystemModel, QTreeView, QTextEdit, QVBoxLayout, QMessageBox, QDialog, QDialogButtonBox, QLabel

import os
from PyQt5.QtCore import pyqtSignal, QThread

from PyQt5.QtCore import QSize 
import json


from UI.QFlag import QFlagWindow

import math


class InputFileSystemViewer:
    def __init__(self, frame_28, frame_30, vlayout_46, input_line_edit, output_data_file_format) -> None:
        #QObject.__init__(self)
        self.frame_28 = frame_28
        self.frame_30 = frame_30
        self.vlayout = vlayout_46
        self.input_line_edit = input_line_edit
        self.output_data_file_format = output_data_file_format
        
        self.bacth_of_file = str()
        self.batch_input_file_name =  list()

        self.cnv_file_system_viewer_files()

    def get_input_file_name(self, obj):

        temp_input_file_path = self.input_line_edit.text()
        self.selected_input_file_name, _ = QFileDialog.getOpenFileNames(obj, 'System file', 'F:/', "system file (*.cnv)")  

        self.updated_file_names = self.input_line_edit.text().split(',')  
        
        if not self.selected_input_file_name:
            self.input_line_edit.setText(temp_input_file_path)
        else:
            if len(self.updated_file_names) == 1:
                self.batch_input_file_name.clear()
                self.bacth_of_file = str()

                for file in self.selected_input_file_name:
                    self.add_full_file_path(file)
                    self.input_line_edit.setText(self.bacth_of_file)
                    self.set_input_file_to_line_edit()
                
            elif len(self.updated_file_names) > 1:
                self.remove_file_path()                
                for file in self.selected_input_file_name:
                    if file.split('/')[-1] not in self.updated_file_names:
                        self.add_full_file_path(file)   
                    else:
                        pass   
                    self.input_line_edit.setText(self.bacth_of_file)
                    self.set_input_file_to_line_edit()
           
    

    def set_input_file_to_line_edit(self):
        self.file_list_tree.clear()
        [self.file_list_tree.append(i) for i in self.batch_input_file_name]

    
    def remove_file_path(self):
        self.bacth_of_file = self.input_line_edit.text()
        for old_file in self.batch_input_file_name:
            if old_file.split('/')[-1] not in self.bacth_of_file.split(','):
                self.batch_input_file_name.remove(old_file)
    
    def add_full_file_path(self, file):
        self.batch_input_file_name.append(file)
        self.bacth_of_file = self.bacth_of_file + file.split('/')[-1] +','

    
    def update_file_names(self):
        self.updated_file_names = self.input_line_edit.text().split(',')
        self.bacth_of_file = self.input_line_edit.text()
        self.remove_file_path()

        for file in self.batch_input_file_name:
            if file.split('/')[-1] not in self.updated_file_names:
                self.batch_input_file_name.remove(file)
            else:
               pass

        self.set_input_file_to_line_edit()


    def cnv_file_system_viewer_files(self):
        self.cfsv_Vlayout = QVBoxLayout(self.frame_30)
        self.file_list_tree = QTextEdit()
        self.file_list_tree.setStyleSheet("color: rgb(0, 0, 0)")
        self.cfsv_Vlayout.addWidget(self.file_list_tree)
        self.vlayout.addWidget(self.frame_30)
        self.frame_28.setMaximumSize(QSize(0, 0))

    def cnv_folder_window_resize(self):
        self.frame_30.setMaximumSize(QSize(0, 0))  
        self.frame_28.setMaximumSize(QSize(16777215, 16777215))

    def cnv_file_window_resize(self):
        self.frame_28.setMaximumSize(QSize(0, 0))
        self.frame_30.setMaximumSize(QSize(16777215, 16777215))

    def set_output_file_names(self):
        output_data_file_name = str()
        for file in self.batch_input_file_name:
            output_data_file_name = output_data_file_name + file.split('/')[-1]+self.output_data_file_format+' , '
        
    



def csv_output_file_format():
    return 'CSV'
    
def xls_output_file_format():
    return 'XlXS'

def txt_output_file_format():
    return 'TXT'

def its_file():
    return 'file'

def its_folder():
    return 'folder'

class DataConversionController(InputFileSystemViewer):
    def __init__(self, data_conversion_object, data_base_options, output_file_formatting):
        
        self.view = data_conversion_object['view']
        #self.view.data_conversion_ui(self)
        self.data_base_options = data_base_options
        self.output_file_formatting =output_file_formatting
        self.input_file_name = None
        self.output_dir_path = None
        self.progress_bar_status_queue = Queue()
        self.progress_bar_status_queue.put(0)
        self.selected_output_file_format = None
        
        self.data_conversion_previous_data = data_conversion_object['previous_data_class']
        self.start_run = None

        self.file_type_rb ={'csv':self.view.csv_rb, 'txt': self.view.txt_rb, 'xlxs': self.view.xlxs_rb}
        self.file_or_folder = {'file':self.view.DC_SingleRB, 'folder':self.view.DC_MultiRB}
        self.data_base_rb = {'pangaea':self.view.pangaerb, 'default':self.view.default_rb}
        self.quality_falg_rb = {'distinct': self.view.QFlaga_checkBox, 'group_files':self.view.QFlag_batch_of_file, 'no_flag': self.view.QFlag_No}
        self.output_file_system()       
        self.cnv_file_system_viewer_folder()
        
        
        InputFileSystemViewer.__init__(self, self.view.frame_28, self.view.frame_30, self.view.verticalLayout_46, self.view.DC_InputLE,\
              self.selected_output_file_format)
        self.my_obj = self.data_conversion_previous_data()
        #self.data_conversion_on_open_run()
    
    def start_condition_check(self):
        emmpty_path_info_alert = QMessageBox()
        emmpty_path_info_alert.setIcon(QMessageBox.Information)
        emmpty_path_info_alert.setInformativeText("Please provide the input files or input folder and output folder directory information")
        emmpty_path_info_alert.setStandardButtons(QMessageBox.Ok)
        emmpty_path_info_alert.resize(450, 100)
        emmpty_path_info_alert.setWindowTitle("File Information Alert")
        emmpty_path_info_alert.exec_()

    def get_input_dir_path(self, InputdirLE, obj):
        temp_input_dir_path = InputdirLE.text()
        self.input_file_name= QFileDialog.getExistingDirectory(obj, 'Input Directory Path')
        self.cnv_model.setRootPath(self.input_file_name)
        self.cnv_tree.setModel(self.cnv_model)
        self.cnv_tree.setRootIndex(self.cnv_model.index(self.input_file_name))

        if not self.input_file_name:
            InputdirLE.setText(temp_input_dir_path)
        else:
            InputdirLE.setText(self.input_file_name)
    
    def predict_single_or_multiple_file(self)->None:
        '''This method detects whether different files or a folder full of files is going to be converted'''

        if self.view.DC_MultiRB.isChecked():
            self.get_input_dir_path(InputdirLE = self.view.DC_InputLE, obj = self.view)
            
        elif self.view.DC_SingleRB.isChecked():
            self.get_input_file_name(obj = self.view)

        elif not (self.view.DC_MultiRB.isChecked() or self.view.DC_SingleRB.isChecked()):
            self.check_file_selection_option()
            
    def check_file_selection_option(self):
        alert = QMessageBox()
        alert.setWindowTitle('Alert')
        alert.setInformativeText('Please select single or multiple file')
        alert.setIcon(QMessageBox.Warning)
        _ = alert.exec()

    
    def getOutPutDirpath(self, output_dir_LE, obj):
        temp_output_dir_path = output_dir_LE.text()
        self.output_dir_path = QFileDialog.getExistingDirectory(obj, 'Output Directory Path')

        self.set_output_file_system_viewer()
        if not self.output_dir_path:
            output_dir_LE.setText(temp_output_dir_path)
        else:
            output_dir_LE.setText(self.output_dir_path)

    def get_output_file_format(self):
        '''creates the object of the CsvWriter class'''
        try:
            self.output_file_type = [format[self.selected_output_file_format] for format in self.output_file_formatting['output_format'] for k in format.keys() if k == self.selected_output_file_format][0](self.output_dir_path)
        except IndexError:
            #self.start_condition_check()
            self.output_file_type = None
            
        
        
    def get_column_attribute(self):
        '''if the selected attribute is pangaea then self.data_base_option returns dictionary, else retuns string'''
        self.column_attribute= [database[self.selected_data_base] for database in self.data_base_options['column_attribute'] for k in database.keys() if k == self.selected_data_base][0]()

    def start_data_conversion(self):
        try:
            if (len(self.view.DC_OutputLE.text()) != 0 ) and  (len(self.view.DC_InputLE.text()) != 0):
                
                self.view.progressBar.setValue(0)
                self.output_file_type.converted_data_folder = self.output_dir_path
                att_from_thread = Queue()
                attriute_receiver_lock = Lock()
                attribute_receiver_thread = [Thread(target=self.attribute_receiver_handler, args=(self.column_attribute.get_attribute, file, attriute_receiver_lock, att_from_thread), daemon=True) for file in self.get_file_list()]
                [i.start() for i in attribute_receiver_thread]

                if self.view.QFlaga_checkBox.isChecked():
                    #temp_attribut = att_from_thread.get()
                    self.add_distinct_qflag(att_from_thread)

                elif self.view.QFlag_batch_of_file.isChecked():
                    temp_attribut = att_from_thread.get()
                    self.batch_of_file_conversion_with_same_qflag(temp_attribut)
                    
                else:
                    self.file_conversion_with_no_qflag()
            else:
                self.start_condition_check()
        except TypeError:
            self.start_condition_check()
    
    def attribute_receiver_handler(self, column_attributes, file, lk, qu):
        with lk:
            new_attribute = self.output_file_formatting['Meta_data'].get_index_from_file(column_attributes, file, self.selected_data_base)
            qu.put(new_attribute)
            
    
    def attribute_writer_handler(self, qu, file, lk):
        
        with lk:
            self.output_file_type.attribute_write(qu, file)
            

    def data_writer_handler(self, lk, string_check, file, Qflag, addQflage, val, PB_queue):
        with lk:
            self.output_file_type.data_writer(string_check, file, Qflag, addQflage)
            PB_queue.put(PB_queue.get()+val)
            
       
    def update_progressbar(self, p_value):
        self.p_value = self.p_value +p_value
        if self.p_value > 100:
            self.p_value = 100
            self.view.progressBar.setValue(self.p_value)
        else:
            self.view.progressBar.setValue(self.p_value)
            

    def update_progress_handler(self, p_value):
       
        if p_value < 100:
            self.view.progressBar.setValue(p_value)
        else:
            self.view.progressBar.setValue(100)

    def cnv_file_system_viewer_folder(self):
        self.cfsvf_Vlayout = QVBoxLayout(self.view.frame_28)
        self.cnv_model = QFileSystemModel()
        self.cnv_tree =  QTreeView(self.view.frame_28)
        self.cfsvf_Vlayout.addWidget(self.cnv_tree)
        #self.cnv_tree.setAlternatingRowColors(True)
        self.view.verticalLayout_46.addWidget(self.view.frame_28)
        self.view.frame_28.setMaximumSize(QSize(0, 0))

    def output_file_system(self):
        self.v_layout = QVBoxLayout(self.view.frame_29)
        self.output_file_model = QFileSystemModel()
        self.output_file_tree =  QTreeView(self.view.frame_29)
        self.v_layout.addWidget(self.output_file_tree)
        #self.output_file_tree.setAlternatingRowColors(True)
        self.view.verticalLayout_4.addWidget(self.view.frame_29)

    
    def data_conversion_on_close_run(self):

        
        self.assign_output_file_format()
        
        if self.assign_file_or_folder():
            file_info = self.batch_input_file_name
        else:
            file_info = self.view.DC_InputLE.text()
            
        self.my_obj.write_data_to_template( previous_data = {'output_folder_path':self.view.DC_OutputLE.text(), 'input_file_path': file_info,\
             'output_data_format':self.selected_output_file_format, 'data_base_type':self.selected_data_base, 'is_file': self.assign_file_or_folder(), 'Qflag_status':self.assign_qflag_type()}, file_name = 'cnv_converter.json')
        self.view.close()

    def data_conversion_on_open_run(self):
        try:
            with open('temp_files\\cnv_converter.json', 'r') as file:
                content = json.load(file)
            for key in list(content.keys()):
                if key == 'output_folder_path':
                    if content[key] == 'nil':
                        pass
                    else:
                        self.view.DC_OutputLE.setText(content[key])
                        self.output_dir_path = content[key]
                        self.set_output_file_system_viewer()

                elif key == 'input_file_path':
                    input_file_name  = content[key]
                    if content[key] == 'nil':
                        self.view.DC_MultiRB.setChecked(True)
                        self.cnv_folder_window_resize()
                    else:
                        if content['is_file']:
                            self.view.DC_SingleRB.setChecked(True)
                            for file in input_file_name:
                                self.add_full_file_path(file)     
                            self.view.DC_InputLE.setText(str(self.bacth_of_file))
                            self.set_input_file_to_line_edit()
                            self.cnv_file_window_resize()
                            
                        else:
                            self.cnv_folder_window_resize()
                            self.view.DC_MultiRB.setChecked(True)
                            self.view.DC_InputLE.setText(content[key])
                            self.input_file_name = input_file_name
                            self.cnv_model.setRootPath(input_file_name)
                            self.cnv_tree.setModel(self.cnv_model)
                            self.cnv_tree.setRootIndex(self.cnv_model.index(input_file_name))
                        
                elif key == 'output_data_format':
                    if content[key] == 'nil':
                        self.view.txt_rb.setChecked(True)
                        self.assign_output_file_format()
                    else:
                        self.file_type_rb[content[key]].setChecked(True)
                        self.assign_output_file_format()
                    
                elif key == 'data_base_type':
                    if content[key] == 'nil':
                        self.view.pangaerb.setChecked(True)
                        self.assign_database_type()
                        self.get_column_attribute()
                    else:
                        self.data_base_rb[content[key]].setChecked(True)
                        self.assign_database_type()
                        self.get_column_attribute()

                elif key == 'Qflag_status':
                    try:
                        self.quality_falg_rb[content[key]].setChecked(True) 
                    except:
                        self.view.QFlag_batch_of_file.setChecked(True) 
            
            self.view.show()
            self.view.app.exec_()
        except FileNotFoundError:
            self.view.show()
            self.view.app.exec_()
        

    def set_input_file_to_line_edit(self):
        self.file_list_tree.clear()
        [self.file_list_tree.append(i) for i in self.batch_input_file_name]

    def assign_output_file_format(self):
        self.selected_output_file_format = [key for key in self.file_type_rb if self.file_type_rb[key].isChecked()][0]
        self.get_output_file_format()

    def assign_file_or_folder(self):
        if [key for key in self.file_or_folder if self.file_or_folder[key].isChecked()][0] == 'file':
            self.cnv_file_window_resize()
            return True
        else:
            self.cnv_folder_window_resize()
            return False
        
    def set_output_file_system_viewer(self):
        self.output_file_model.setRootPath(self.output_dir_path)
        self.output_file_tree.setModel(self.output_file_model)
        self.output_file_tree.setRootIndex(self.output_file_model.index(self.output_dir_path))

    def assign_database_type(self):
        self.selected_data_base = [key for key in self.data_base_rb if self.data_base_rb[key].isChecked()][0]
        self.get_column_attribute()

    def assign_qflag_type(self)->str:
        '''method retruns the selected quality file option'''
        return [key for key in self.quality_falg_rb if self.quality_falg_rb[key].isChecked()][0]

    def batch_of_file_conversion_with_same_qflag(self, temp_attribut:dict)->None:
        self.p_value = 0
        file_list = self.get_file_list()

        my_dialog_obj = QFlagWindow(self.output_file_type.attribute_write, file_list[0], self.output_dir_path, self.output_file_formatting['Meta_data'].string_check, self.output_file_type.data_writer, True, temp_attribut)                   
        my_dialog_obj.exec()
        new_index = my_dialog_obj.new_index

        self.batch_file_thread = BatchFileThread(column_attributes = self.column_attribute.get_attribute, selected_data_base=self.selected_data_base,\
             files= file_list, attribute_receiver=self.output_file_formatting['Meta_data'].get_index_from_file, writer_class=self.output_file_type,\
                  string_check=self.output_file_formatting['Meta_data'].string_check, Qflag = my_dialog_obj.flag_values, addQflage=True, selected_flag = new_index)
        
        self.batch_file_thread.start()
        self.batch_file_thread.signal_to_update_progress_bar.connect(self.update_progressbar)

    def get_file_list(self):
        try:
            if self.assign_file_or_folder():
                return self.batch_input_file_name
            else:
                return [self.input_file_name+"/"+ x for x in os.listdir(self.input_file_name) if x.endswith('.cnv')]
        except FileNotFoundError:
            pass
            #self.start_condition_check()

    def file_conversion_with_no_qflag(self ):
        self.p_value = 0
        file_list = self.get_file_list()
        self.batch_file_thread = BatchFileThread(column_attributes = self.column_attribute.get_attribute, selected_data_base=self.selected_data_base,\
             files= file_list, attribute_receiver=self.output_file_formatting['Meta_data'].get_index_from_file, writer_class=self.output_file_type,\
                  string_check=self.output_file_formatting['Meta_data'].string_check, Qflag = None, addQflage=False, selected_flag = list())
        
        self.batch_file_thread.start()
        self.batch_file_thread.signal_to_update_progress_bar.connect(self.update_progressbar)

    def add_distinct_qflag(self, temp_attribut):
        file_list = self.get_file_list()
        for file, n in zip(file_list, range(len(file_list))):
            val = 100/len(file_list) * (n+1) 
            my_dialog_obj = QFlagWindow(self.output_file_type.attribute_write, file, self.output_dir_path, self.output_file_formatting['Meta_data'].string_check, self.output_file_type.data_writer,False, temp_attribut.get())                   
            my_dialog_obj.exec()
            self.update_progress_handler(val)

class BatchFileThread(QThread):
    signal_to_update_progress_bar = pyqtSignal(float)
    def __init__(self, column_attributes:Callable[[], dict or str], selected_data_base:str, files:list, attribute_receiver:Callable[[Callable, str, str], list],\
        writer_class:Callable,  string_check, Qflag, addQflage, selected_flag):
        super().__init__()
        self.column_attributes = column_attributes
        self.selected_data_base = selected_data_base
        self.files = files 
        self.attribute_receiver = attribute_receiver
        self.attribute_writer_method = writer_class.attribute_write
        self.data_writer_method = writer_class.data_writer
        self.string_check = string_check
        self.Qflag = Qflag
        self.addQflage = addQflage 
        self.selected_flag = selected_flag

    def run(self):
        for file in self.files:
            status = self.attribute_writer(self.get_column_attributes(file)+ self.selected_flag, file)
            print(status)
            if status:
                self.data_writer(file)
                self.signal_to_update_progress_bar.emit(math.ceil(100/len(self.files)))
    def get_column_attributes(self, file):
        return self.attribute_receiver(self.column_attributes, file, self.selected_data_base)
    
    def attribute_writer(self, attribute, file):
        return self.attribute_writer_method(attribute, file)

    def data_writer(self, file):
        self.data_writer_method(self.string_check, file, self.Qflag, self.addQflage)
        
