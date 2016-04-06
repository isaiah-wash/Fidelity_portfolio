import xlrd
import matplotlib.pyplot as plt
file_location = "fidelity_portfolio.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(1)



date_list = []
date_list2 = []
stock_price = []

for row in range(sheet.nrows):
	
	date_list.append(sheet.cell_value(row,0))
	stock_price.append(sheet.cell_value(row, 1))
	date_list2.append(xlrd.xldate_as_tuple(sheet.cell_value(row,0),0))
	

date_string_list = []
for i in date_list2:

	date_string_list.append('%g/%g/%g' %(i[0], i[1], i[2]))

month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


	
	

plt.fill_between(date_list, stock_price, color = "pink")
plt.plot(date_list, stock_price, color = "blue")
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('1 year INGN Stock')
plt.xticks(date_list, date_string_list)
plt.show()


