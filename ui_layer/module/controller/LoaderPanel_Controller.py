import wx
import os
from os.path import isfile, dirname, join
import subprocess
from pprint import pprint as pp
from ui_layer.log_init import log, info, debug
from ui_layer.Base import reciever


from ui_layer.common import exception
from pathlib import Path
from ui_layer.Base import reciever, Base
from ui_layer.dialog.ErrDlg import open_editor



#---------------------------------------------------------------------------
class LoaderPanel_Controller(Base):
    def __init__(self):
       pass

    
    @reciever
    def filterlog(self,message, arg2=None, **kwargs):
        msg=message
        self.flog.AppendText(msg)
        self.flog.AppendText("\n")
    @reciever
    def navlog(self,message, arg2=None, **kwargs):
        msg=message
        self.nlog.AppendText(msg)
        self.nlog.AppendText("\n")
        