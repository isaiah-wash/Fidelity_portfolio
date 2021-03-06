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

month_list = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar']

graph_list = [date_list[0], date_list[21], date_list[41], date_list[63], date_list[85], date_list[106], date_list[127], date_list[149], date_list[169], date_list[191], date_list[210], date_list[230]]
	
	

plt.fill_between(date_list, stock_price, color = "pink")
plt.plot(date_list, stock_price, color = "blue")
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('1 year INGN Stock')
plt.xticks(graph_list, month_list)
#plt.xticks(date_list, date_string_list)
plt.show()


