import os, sys
import subprocess
from pathlib import Path
from os.path import join, isfile

def edit_file( fn):
	EDITOR=getEditor()
	assert isfile(fn), fn
	if 1:
		subprocess.call([EDITOR, fn])
		
def getEditor(apc=None):
	if not apc:
		APP_ROOT=os.getcwd()
	else:
		APP_ROOT=apc.home
	floc=Path(join('..\\','Notepad++', 'notepad++.exe'))
	
	assert isfile(floc), str(floc.resolve())
	return str(floc.resolve())
def open_editor(fn, ln=0, win=None, cdir=None):
	
	EDITOR= getEditor()

	try:
		if cdir: os.chdir(cdir)
		assert os.path.isfile(fn), 'Cannot open file "%s" [%s]' % (fn, os.getcwd())

		
		#info('Editing 1 "%s"' % fn)
		if ln:
			#https://www.autohotkey.com/
			subprocess.call([EDITOR, #'-multiInst'  --//reset editor if line number does not work
			fn, '-n%d' % ln])
		else:
			subprocess.call([EDITOR, fn])
	except:
		raise
		if 0:
			import inspect
			#pp (traceback.format_stack(limit=500))
			frm = inspect.trace()
			#pp(frm)
			mod = inspect.getmodule(frm[0])
			modname = mod.__name__ if mod else frm[1]
			#print ('Thrown from', modname)
		
		if 1:
			print(format_stacktrace())
		if 0:
			exc_type, exc_value, exc_traceback = sys.exc_info()
			print ("*** print_tb:")
			traceback.print_tb(exc_traceback, limit=50, file=sys.stdout)
			print ("*** print_exception:")
			traceback.print_exception(exc_type, exc_value, exc_traceback,
									  limit=50, file=sys.stdout)
		if 0:
			exc_type, exc_value, exc_traceback = sys.exc_info()
			print ("*** print_exc:")
			traceback.print_exc()
			print ("*** format_exc, first and last line:")
			formatted_lines = traceback.format_exc().splitlines()
			print (formatted_lines[0])
			print (formatted_lines[-1])
			print ("*** format_exception:")
			print (repr(traceback.format_exception(exc_type, exc_value,
												  exc_traceback)))
			print ("*** extract_tb:")
			print (repr(traceback.extract_tb(exc_traceback)))
			print ("*** format_tb:")
			print (repr(traceback.format_tb(exc_traceback)))
			print ("*** tb_lineno:", exc_traceback.tb_lineno)
	
		if 0:
			stacktrace = format_stacktrace()
			error(stacktrace)

			if 1:
				import dialog.ErrDlg as ED
				ED.show(stacktrace, win)
			if 0:
				dlg = wx.MessageDialog(win, stacktrace,
					'Cannot open file',
					wx.OK | wx.ICON_INFORMATION
					#wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
					)
				dlg.ShowModal()
				dlg.Destroy()
		
		
		