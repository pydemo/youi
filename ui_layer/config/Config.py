import os, sys, json, codecs, shutil
import re
from datetime import datetime

from os.path import join, isdir
from os.path import isfile, isdir, join, basename
from pprint import pprint as pp
from ui_layer.utils import d2d2
from ui_layer.common import TMP_DIR, PIPELINE_DIR, RUNTIME, UI_DEFAULTS_FN

e=sys.exit


class Config(object): 
	print('INIT:',__file__)
	def __init__(self, **kwargs):


		#self.cfg_root = cfg_root= self.getCfgRoot()		
		#if not isdir(cfg_root): os.makedirs(cfg_root)

		self.root= self.getRoot()
		self.env=RUNTIME
		self.pipeline     = pipeline = kwargs['pipeline'].strip()
		if '\\' in pipeline:
			self.dotted_pipeline=pipeline.replace('\\','.')
		else:
			self.dotted_pipeline=pipeline.replace('/','.')
		
		
		self.pipeline_dir = join(PIPELINE_DIR, self.dotted_pipeline.replace('.', os.sep))
		assert self.pipeline_dir
		self.home=None

	def getConfigName(self):
		return self.config_name
	def getRoot(self):
		return os.getcwd()
	def getBuildRoot(self):
		return join(os.getcwd(), '_build')
	def getTemplateRoot(self):
		return join(self.getBuildRoot(), '_template')		
	def getCfgRoot(self):
		return join(TMP_DIR,'ui_config')
		

	def validate(self):
		#if not  os.path.isdir(self.cfg_root):
		#	raise Exception('Cfg root does not exists at " %s "' % ( self.cfg_root))
		if not isfile(self.apc_path):
			print('ERROR: App config does not exists at \n%s' % self.apc_path)
			
		return self

		
	def LoadConfig(self, config_path, quiet=False):
		
		with codecs.open(config_path, encoding="utf-8") as stream:
			data=stream.read()
			cfg = json.loads(data)
		
		out =d2d2(cfg)
		if not quiet:
			print('-'*80)
		return out

		
	def getHome(self):
		home=self.home
		assert home
		assert isdir(home)
		return home
		
		  

	def saveConfig(self):
		
		#assert hasattr(self, 'cfg')
		assert isfile(self.apc_path)
		
		with open(self.apc_path, 'w') as fp:
			dump = json.dumps(self.cfg, indent='\t', separators=(',', ': '))
		   
			new_data= re.sub('"\n[\t]+},', '"},', dump)

			fp.write(dump)
	def initCfgFile(self,path):
		assert isfile(UI_DEFAULTS_FN), UI_DEFAULTS_FN
		assert not isfile(path), f'Destination exists: {path}'
		shutil.copy(UI_DEFAULTS_FN, path)
		
		if 0:
			ts='{:%Y%b%d_%H%M%S_%f}'.format(datetime.now())
			if not isfile(path):
					
				with open(path,'w') as fh:
					fh.write('{"ts":"%s"}' % ts)

		
		
			
	def getPythonHome(self):
		cfg=self.cfg
		assert 'Python' in cfg
		assert 'home' in cfg['Python']
		return cfg['Python']['home']





	def getAppName(self, layout_loc=None):
		if not layout_loc: return self.app_name
		else:
			return os.path.splitext(os.path.basename(layout_loc))[0]
