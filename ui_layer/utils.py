import sys
import importlib
from ui_layer.common import *
from os.path import isfile, isdir, join, basename, dirname
from pprint import pprint as pp

def import_module(file_path):
	#if not apc.quiet: print(file_path)
	bn=basename(file_path)
	
	mod_name,file_ext = os.path.splitext(os.path.split(file_path)[-1])
	spec = importlib.util.spec_from_file_location(mod_name, file_path)
	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)
	if 1:
		sys.modules[mod_name] = module
	
	return module
		
		
class dict2(dict):                                                              

	def __init__(self, **kwargs):                                               
		super(dict2, self).__init__(kwargs)                                     

	def __setattr__(self, key, value):                                          
		self[key] = value                                                       

	def __dir__(self):                                                          
		return self.keys()                                                      

	def __getattr__(self, key):                                                 
		try:                                                                    
			return self[key]                                                    
		except KeyError:                                                        
			raise AttributeError(key)                                           

	def __setstate__(self, state):                                              
		pass 
def d2d2(d):
	out=dict2()
	for k, v in d.items():
		if type(v) in [dict]:
			out[k]= d2d2(v)
		else:
			out[k]=v
	return out
	
if is_nt:


	def cli_exception(func):
		def wrapper(*args, **kwargs):

			#manual test only
			from ui_layer.app import  headless_ui
			from ui_layer.common import  format_stacktrace
			
			#from ui_layer.common import error
			import ui_layer.dialog.ErrDlg as ED
			#import ui_layer.config.ui_config as ui_config 
			#import cli_layer.config.app_config as app_config 
			

			app=headless_ui()
			try:

				original_return_val = func(*args, **kwargs)
			except:

				#pp(kwargs)
				import ui_layer.config.init_config as init_config  
				#init_config.init(**kwargs)
				
				apc = init_config.apc
				
				#apc.validate().load() 
				
				stacktrace = format_stacktrace()
				#error(stacktrace)
				if 1:
					ED.show(stacktrace)
				app.MainLoop()
				original_return_val=1
			return original_return_val
		return wrapper

else:


	def cli_exception(func):
		def wrapper(*args, **kwargs):

			original_return_val = func(*args, **kwargs)
			return original_return_val
		return wrapper
	