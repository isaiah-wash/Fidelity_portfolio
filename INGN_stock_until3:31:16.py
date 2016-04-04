import xlrd
import matplotlib.pyplot as plt
file_location = "fidelity_portfolio.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(1)


#import matplotlib.pyplot as plt
date_list = []
stock_price = []

for row in range(sheet.nrows):
	date_list.append(sheet.cell_value(row,0))
	stock_price.append(sheet.cell_value(row, 1))
#print date_list
	
	

plt.fill_between(date_list, stock_price, color = "pink")
plt.plot(date_list, stock_price, color = "blue")
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('1 year INGN Stock')
plt.show()



