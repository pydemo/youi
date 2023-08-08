import wx
#from ui_layer.common import * 
#from ui_layer.common import ex, exception
from pprint import pprint as pp
import ui_layer.config.init_config as init_config
apc = init_config.apc

#from ui_layer.utils import ex
class StartFrame(wx.Frame):#, Base):
	#@exception
	def __init__(self, parent, headless):
		#pp(apc.cfg)
		wx.Frame.__init__(self, parent)
		self.Show(False)
		
		#self.Freeze()
		
		if not headless:
			from ui_layer.DataFrame import DataFrame
			self.frame = frame= DataFrame(self, 'GH UI')

		#self.Thaw()

