

# -*- coding: utf-8 -*-
import os
import sys
import traceback
import configparser

from apscheduler.schedulers.blocking import BlockingScheduler



from flask import Flask

from .task import task1
from .model import config_db
from .handler import config_hd



def main(argv):
	print(f"""
		##########################
		# - ACME - Tasks Robot - #
		# - v 1.0 - 2020-07-28 - #
		##########################
		
		Press Crtl+{'Break' if os.name == 'nt' else 'C'} to exit! 
	""")
	
	
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:123mudar@127.0.0.1:5432/bot_db'

	config_db(app)
	config_hd(app)
	scheduler = BlockingScheduler()
	
	
	config = configparser.ConfigParser()
	config.read('/tmp/bot/settings/config.ini')
	
	var1 = int(config.get('scheduler','IntervalInMinutes'))
	app.logger.warning(f'Intervalo entre as execucoes do processo: {va1}')
	
	task1_instance = scheduler.add_job(task1(app.db), 'interval', id='task1_job', minutes=var1)
	
	try:
		scheduler.start()
	except(KeyboardInterrupt, SystemExit):
		print('bye')
	
	print('job executed!')



if __name__ == '__main__':
	main(sys.argv)