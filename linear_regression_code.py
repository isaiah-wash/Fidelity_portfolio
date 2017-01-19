# numpy and matplotlib needed 

#Allows for linear regression	
reg = np.polyfit(date_list, stock_price, deg = 1)
ry = np.polyval(reg, date_list)

#plot linear regression
plt.plot(date_list, ry, 'b-', label = 'regression')