import os, sys, traceback
from os.path import join, isdir, isfile
home=os.path.dirname(sys.argv[0])
if not home :
	home=os.path.dirname(os.path.abspath(__file__))
print(home)
APP_NAME    	= 'youi'
LAYER_DIR   	= 'ui_layer'
PIPELINE_DIR	= 'pipeline'
UI_DEFAULTS_FN  = join(home, 'ui_defaults.json')
_START_SIZE  = (550, 550)
_START_POS	= (350,150)

if os.name == "nt":
    UI_TMP_DIR=join('C:\\','tmp',APP_NAME)
else:
    UI_TMP_DIR=join('/tmp',APP_NAME)


RUNTIME = os.environ.get('ZZZ_RUNTIME_ENV__')
assert RUNTIME in ['DEV','QA','PROD'], 'Undefined env: "set ZZZ_RUNTIME_ENV__="'

APP_NAME = os.environ.get('ZZZ_APP_NAME__')
assert APP_NAME, 'Undefined env: "set ZZZ_APP_NAME__="'
assert len(APP_NAME.split('.'))==2, 'ZZZ_APP_NAME__ format: XX.xxxxx"'

is_nt=False
if os.name == "nt":
    is_nt=True
    TMP_DIR=join('C:\\','tmp',APP_NAME)
	
else:
    TMP_DIR=join('/tmp',APP_NAME)


def exception(func):
    def wrapper(*args, **kwargs):
        
        try:
            original_return_val = func(*args, **kwargs)
        except:
            ex()
        
        return original_return_val
    return wrapper
def ex(win=None,_exit=False):

    stacktrace = format_stacktrace()
    #error(stacktrace)
    if 1:
        ED.show(stacktrace)
    if _exit:
        raise
    else:
        return False	
		
def format_stacktrace():
    parts = ["Traceback (most recent call last):\n"]
    parts.extend(traceback.format_stack(limit=50)[:-2])
    parts.extend(traceback.format_exception(*sys.exc_info())[1:])
    return "".join(parts)		