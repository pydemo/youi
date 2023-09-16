import wx
from wxasync import AsyncBind, WxAsyncApp, StartCoroutine
import asyncio
from asyncio.events import get_event_loop
import time
import wx.lib.newevent
SomeNewEvent, EVT_SOME_NEW_EVENT = wx.lib.newevent.NewEvent()
SomeNewEventAsync, EVT_SOME_NEW_EVENT_ASYNC = wx.lib.newevent.NewEvent()

import ui_layer.config.init_config as init_config
apc = init_config.apc

#import ui_layer.config.ui_config as ui_config
#uic = ui_config.uic

from ui_layer.Base import reciever, Base

#from  ui_layer.SubPanel import TestSubPanel

from ui_layer.common import exception
#from ui_layer.utils import load_pipeline_module

#MainPanel= apc.load_pipeline_module( 'MainPanel')
from ui_layer.module.MainPanel import MainPanel

from ui_layer.module.controller.LoaderPanel_Controller import LoaderPanel_Controller as Controller

class LoaderPanel(wx.Panel, Controller):
	def __init__(self, parent=None):
		super(LoaderPanel, self).__init__(parent)

		if 1:
			vbox = wx.BoxSizer(wx.VERTICAL)
			
			panel = MainPanel(parent=self)
		vbox.Add(panel, 1, wx.EXPAND|wx.ALL)
		if 0:
			
			if 1:
				self.flog = wx.TextCtrl(self, wx.ID_ANY, "", wx.DefaultPosition, (-1,130),
										  wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_LEFT | wx.TE_BESTWRAP | wx.BORDER_NONE)
			if 1:
				self.nlog = wx.TextCtrl(self, wx.ID_ANY, "", wx.DefaultPosition, (-1,130),
										  wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_LEFT | wx.TE_BESTWRAP | wx.BORDER_NONE)
			
			hbox = wx.BoxSizer(wx.HORIZONTAL)
			hbox.Add(self.flog, 1, wx.EXPAND)
			hbox.Add(self.nlog, 1, wx.EXPAND)
			vbox.Add(hbox, 0, wx.EXPAND)
		self.SetSizer(vbox)
		self.Layout()
		self.sub('navlog')
		self.sub('filterlog')
