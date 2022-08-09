from queue import Queue
from typing import Callable
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QDialog, QDialogButtonBox, QLabel, QSpinBox, QCheckBox, QGridLayout
from PyQt5 import QtCore
import csv
import os
from threading import Thread, Lock

from PyQt5.QtCore import pyqtSignal


class QFlagWindow(QDialog):
    attribute_signal = pyqtSignal(list)
    data_writer_signal = pyqtSignal()
    data_writer_lock = Lock()
    
    def __init__(self, index_writer:Callable, file_name, output_file_name, string_check, data_writer, isBatch_file = False,  attribute_list= None):
        super().__init__()
        self.attribute_queue = Queue()
        self.isBatch_file = isBatch_file
        self.attribute_list = attribute_list
        self.index_writer = index_writer
        self.file_name = file_name
        self.output_dir_path = output_file_name
        self.string_check= string_check
        self.data_writer = data_writer
        self.first_frame = QFrame(self)
        self.vbox_layout_1 = QVBoxLayout(self)
        self.title_label = QLabel(self.first_frame)
        self.title_label.setText(self.file_name)
        self.grid_layout= QGridLayout(self.first_frame)
        self.control_button = QDialogButtonBox(self.first_frame)
        self.control_button.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.control_button.setOrientation(QtCore.Qt.Horizontal)
        self.control_button.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.Qflag_labels = [QLabel(self.first_frame ) for _ in range(len(self.attribute_list))]
        [my_lb.setObjectName(u"self.lb_"+str(i)) for i, my_lb in  zip(range(len(self.Qflag_labels)), self.Qflag_labels)]
        [label.setText(attribute) for label, attribute in zip(self.Qflag_labels, self.attribute_list)]
        self.Qflag_spbox = [QSpinBox(self.first_frame ) for _ in range(len(self.attribute_list))]
        self.Qflag_checkbox = [QCheckBox(self.first_frame ) for _ in range(len(self.attribute_list))]
        [my_chb.setObjectName(u"self.chb_"+str(i)) for i, my_chb in  zip(range(len(self.Qflag_checkbox)), self.Qflag_checkbox)]
        
        for i, l, cb, ch in zip(range(len(attribute_list)), self.Qflag_labels, self.Qflag_spbox, self.Qflag_checkbox):
            self.grid_layout.addWidget(l, i, 0, 1, 1)
            self.grid_layout.addWidget(cb, i, 1, 1, 1)
            self.grid_layout.addWidget(ch, i, 2, 1, 1)

        self.control_button.accepted.connect(self.get_qfalgs)
        
        self.vbox_layout_1.addWidget(self.title_label, 0, QtCore.Qt.AlignHCenter)
        self.vbox_layout_1.addWidget(self.first_frame)
        self.vbox_layout_1.addWidget(self.control_button)
        self.index_writer_lock = Lock()
        
        self.my_index_writer_thread = Thread(target=self.index_writer_thread, args=(self.attribute_queue, self.index_writer_lock), daemon=True)
        self.my_index_writer_thread.start()

        self.attribute_signal.connect(self.data_writer_thread_handler)


    def get_qfalgs(self):
        self.obtained_Qflag = [(attribute, spb.value()) for chb, spb, attribute in zip(self.Qflag_checkbox, self.Qflag_spbox, self.attribute_list) if chb.isChecked()]
        self.flag_values = list()
        self.new_index = list()

        for i in self.obtained_Qflag:
            att, flag = i
            self.new_index.append(att+' Qflag')
            self.flag_values.append(str(flag))
        print('I am here')
        if not self.isBatch_file:
            self.attribute_list = self.attribute_list+ self.new_index
            self.attribute_queue.put(self.attribute_list)
            self.attribute_signal.emit(self.flag_values)
        else:
            self.accept()
        
    
    def data_writer_thread_handler(self, flag_values):
        lk = Lock()
        with lk:
            self.data_writer_thread = Thread(target=self.data_writer_thread, args=(flag_values,lk), daemon=True)
            self.data_writer_thread.start()
            self.accept()

    def index_writer_thread(self, q, lk):
        with lk:
            new_attribute = q.get()
            self.index_writer(new_attribute, self.file_name)
            

    def data_writer_thread(self, flag_values, lk):
        with lk:
            self.data_writer(self.string_check, self.file_name, flag_values, True)
            self.data_writer_signal.emit()
            