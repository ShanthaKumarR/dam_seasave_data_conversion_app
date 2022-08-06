from abc import ABC, abstractclassmethod
import os
import json

class SaveHistory(ABC):
    @abstractclassmethod
    def write_data_to_template(self):
        pass
    @abstractclassmethod
    def create_default_template(self):
        pass


class PreviousData(SaveHistory):
    def __init__(self, dir_path = "temp_files"):
        self.temp_folder_path = dir_path
        file_names_list = ["instrument_config.json", "cnv_converter.json"]
        keys = [['setup_file_path', 'instrument_config_file_path', 'archive_folder_path', 'output_data_folder_path', 'system_file_path',\
        'instrument_type', 'cast_type', 'cast_number'], ['is_file', 'output_folder_path', 'input_file_path', 'output_data_format', 'data_base_type', 'Qflag_status']]

        if os.path.isdir(self.temp_folder_path):
            for key_list, file_name in zip(keys, file_names_list):
                if not os.path.isfile(self.temp_folder_path+'\\'+file_name):
                    self.create_default_template(key_list =  key_list, file_name = file_name)
        else:
            os.mkdir(self.temp_folder_path)
            for key_list, file_name in zip(keys, file_names_list):
                self.create_default_template(key_list = key_list, file_name = file_name)
 
    def write_data_to_template(self, previous_data:dict, file_name:str):

        with open(self.temp_folder_path+'\\'+file_name, 'r') as json_file:
            data = json.load(json_file)
        keys = list(data.keys())

        for key in keys:
            data[key] = previous_data[key]
              
        with open(self.temp_folder_path+'\\'+file_name, 'w') as file:
            json.dump(data, file, indent=4)

    def create_default_template(self, key_list:list, file_name:str):
        template = {}
        for k in key_list:
            if k == 'bottle_number':
                template[k] = 0
            else:
                template[k] = "nil"

        with open(self.temp_folder_path+'\\'+file_name, 'w') as file:
            json.dump(template, file, indent=4)


class Previous_Bottle_data(SaveHistory,):    
    def __init__(self):
        if os.path.isdir("temp_files"):
            if os.path.isfile("temp_files\\bottle.json"):
                pass
            else:
                self.create_default_template()
        else:
            os.mkdir("temp_files")
            self.create_default_template()

    def create_default_template(self):
        template = dict()
        template['Number of bottles'] =0
        template['Bottles'] = list()

        with open("temp_files\\bottle.json", 'w') as file:
                json.dump(template, file, indent=4)        


    def write_data_to_template(self, bottle_number, pressure):
        self.create_default_template()
        with open("temp_files\\bottle.json", 'r') as file:
            my_temp_data = json.load(file)
        my_temp_data['Number of bottles'] = bottle_number

        for bottle, bottle_pressure in zip(range(bottle_number), pressure):
            my_temp_data['Bottles'].append({'bottle'+str(bottle+1): bottle_pressure})
            #data['bottle'+str(bottle+1)] = bottle_pressure
        
        with open("temp_files\\bottle.json", 'w') as file:
                json.dump(my_temp_data, file, indent=4)