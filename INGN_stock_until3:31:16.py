import xlrd
import matplotlib.pyplot as plt
file_location = "fidelity_portfolio.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(1)


'''if sheet.cell(1,1).ctype == 3:
	ms_date_number = sheet.cell_value(1,1)
	ms_date_number = sheet.cell(1,1).cell_value

	year, month, day'''

date_list = []
stock_price = []

for row in range(sheet.nrows):
	date_list.append(xlrd.xldate_as_tuple(sheet.cell_value(row,0),0))
#	date_list.append(sheet.cell_value(row,0))
	stock_price.append(sheet.cell_value(row, 1))
print date_list
#print xlrd.xldate_as_tuple(sheet.cell_value(row,0),0)
	
	

plt.fill_between(date_list, stock_price, color = "pink")
plt.plot(date_list, stock_price, color = "blue")
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('1 year INGN Stock')
#plt.show()



