import os
import xlsxwriter

from datetime import datetime


def task1(db):
	
	file_name = 'data_export_{0}.xlsx'.format(datetime.now().strftime("%d/%m/%d as %H:%M:%S"))
	file_path = os.path.join(os.path.curdir, file_name)
	
	workbook = xlsxwriter.Workbook(file_path)
	worksheet = workbook.add_worksheet()
	
	orders = db.session.execute('SELECT * FROM users;')
	
	index = 1

	worksheet.write('A1','Id')
	worksheet.write('B2','Name')
	worksheet.write('C3',' Email')
	worksheet.write('D4','Password')
	worksheet.write('E5','Role Id')
	worksheet.write('F6','Created At')
	worksheet.write('G7','Updated At')



	for order in orders:
		index += 1
		print(f"""
		Id: {order[0]}
		Name: {order[1]}
		Email: {order[2]}
		Password: {order[3]}
		Role Id: {order[4]}
		Created At: {order[5]}
		Updated At: {order[6]""")
		
		worksheet.write('A{0}'.format(index),order[0])
		worksheet.write('B{0}'.format(index),order[1])
		worksheet.write('C{0}'.format(index),order[2])
		worksheet.write('D{0}'.format(index),order[3])
		worksheet.write('E{0}'.format(index),order[4])
		worksheet.write('F{0}'.format(index),order[5])
		worksheet.write('G{0}'.format(index),order[6])
		
	workbook.close()