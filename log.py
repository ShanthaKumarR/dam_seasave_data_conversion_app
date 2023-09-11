from PyQt5.QtWidgets import QMessageBox

def log_writer(msg):
    with open('log\\log.txt', 'a') as log_file:
        log_file.write(msg+'\n')



def empty_field_alert(msg = 'Empty field alert'):
    alert_dialog_box = QMessageBox()
    alert_dialog_box.setWindowTitle('Hey wait !!!!')
    alert_dialog_box.setIcon(QMessageBox.Warning)
    alert_dialog_box.setText(msg)
    alert_dialog_box.exec_()



class NOtOutputFolder(Exception):
    pass

class NoConfigFile(Exception):
    pass

class NotArchiveFolder(Exception):
    pass

class NoExcecuatble(Exception):
    pass

class NoSystemFile(Exception):
    pass

class SeasaveProcessRunning(Exception):
    pass

class DamCtdSysFileNotFound(Exception):
    pass