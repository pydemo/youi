import wx
import os, sys, logging
sys.path.append('youi')
from os.path import join, isdir, split, basename
from wxasync import AsyncBind, WxAsyncApp, StartCoroutine
import asyncio
from asyncio.events import get_event_loop
import time
from pprint import pprint as pp
import wx.lib.agw.aui as aui

import click
click.disable_unicode_literals_warning = True
home=os.path.dirname(sys.argv[0])
if not home :
	home=os.path.dirname(os.path.abspath(__file__))
e=sys.exit

bnf=basename(__file__)

nop_opt=sys.argv[1]

if nop_opt.strip() in ['-nop']: #'Arguments must start with "Total pipeline params count [-nop]"'
	nop=str(sys.argv[2])
	assert nop.isdigit(), '-nop must be count of procedure params (got "%s").' % nop
else:
	nop=None
#
class MainFrame(wx.Frame):
	def __init__(self, parent=None):
		super(MainFrame, self).__init__(parent, title='Gmail parser', size=(600,900), pos=(800,300))
		vbox = wx.BoxSizer(wx.VERTICAL)
		from ui_layer.LoaderPanel import LoaderPanel
		panel=LoaderPanel(self)
		if 1:
			self.mgr = aui.AuiManager()
			self.mgr.SetManagedWindow(self)
			self.allowAuiFloating = False
			#self.refs=defaultdict(dict)
			
			self.mgr.AddPane(panel,aui.AuiPaneInfo().Center().Layer(1).
			BestSize(wx.Size(200,150)).MinSize(wx.Size(200,150)).
			CloseButton(False).Name("MainPanel").CaptionVisible(False))


#from ui_layer.utils import  cli_exception



@click.command()
@click.option('-nop','--num_of_params', default = None,	help="ParmsConfig", type=int, required=False)
@click.option('-r',  '--runtime',	default = 'DEV',help = 'Runtime.') # DEV/UAT/PROD
@click.option('-p',  '--pipeline',  default = None,	help = 'ETL pipeline name',	required=True )
@click.option('-pa', '--params', 	nargs=int(nop) if nop else 0, help="Pipeline params", type=str, required=False)
@click.option('-la', '--ui_layout',	type=str, default='default', required=False, help="Open manual test ui.")
@click.option('-o' , '--open',      is_flag=True, help="Open pipeline file and exit.")
#@cli_exception
def main(**kwargs):
	global log
	pp(kwargs)
	if 1:
		if 1:
			
			import ui_layer.config.init_config as init_config  
			init_config.init(**kwargs)
			
			apc = init_config.apc
			
			apc.validate().load_ui_cfg() 
			
		if 0:
			from ui_layer.common import UI_TMP_DIR, UI_CFG_FN

			import ui_layer.config.ui_config as ui_config 
			ui_config.init(**kwargs)
			uic = ui_config.uic
			import ui_layer.config.ui_layout as ui_layout 
			
			ui_layout.init(**kwargs)
			uil = ui_layout.uil
	if 1:
		app = WxAsyncApp()
		frame = MainFrame()
		frame.Show()
		app.SetTopWindow(frame)
		loop = get_event_loop()
		loop.run_until_complete(app.MainLoop())
if __name__=="__main__":
	main()
