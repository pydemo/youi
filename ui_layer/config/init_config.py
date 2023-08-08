from ui_layer.config.AppConfig import AppConfig

def init(**kwargs):
	global apc

	apc = AppConfig(**kwargs)