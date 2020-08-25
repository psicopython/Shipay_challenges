
import logging
from logging.handlers import RotatingFileHandler

def config_hd(app):
	handler = RotatingFileHandler('bot.log', maxBytes=10000, backupCount=1)
	handler.setLevel(logging.INFO)
	app.logger.addHandler(handler)
	