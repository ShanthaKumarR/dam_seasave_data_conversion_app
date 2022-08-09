import sys
from view.view import View
from seasave_data_conversion.cnv_converter import  PangaeaColumnAttribute, PangaeaTypeDataBase, ExtractMetaData, CsvWriter, SingleOrBatch, DefaultColumnAttribute, DefaultDataBaseType, TextWriter
from utils.previousData import PreviousData
from controller.data_conversion_controller import DataConversionController

class Model:
    def __init__(self):
        self.view = View()
        data_conversion_object = dict()
        output_file_formatting = {'output_format':[],'Meta_data':ExtractMetaData}
        data_conversion_object['view'] = self.view.data_converstion_ui
        data_base_options = {'column_attribute':[], 'database_type':[]}
        data_base_options['column_attribute'].append({'pangaea':PangaeaColumnAttribute})
        data_base_options['database_type'].append({'pangaea':PangaeaTypeDataBase})
        data_base_options['database_type'].append({'default':DefaultDataBaseType})
        data_base_options['column_attribute'].append({'default': DefaultColumnAttribute})
        output_file_formatting['output_format'].append({'csv':CsvWriter})
        output_file_formatting['output_format'].append({'txt':TextWriter})
        data_conversion_object['previous_data_class'] = PreviousData
        self.controller = DataConversionController(data_conversion_object, data_base_options, output_file_formatting)
        self.view.data_conversion_controls(self.controller)
        

if __name__ == '__main__':
    model_obj = Model()
    model_obj.controller.data_conversion_on_open_run()
    