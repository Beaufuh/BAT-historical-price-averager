from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import statistics 

#Python 3.9.1 
#Selenium 3.141.0

#!TODO: Allow class objects to work for any coinmarketcap crypot url. Currently only BAT tested. 
bat_url = r'https://coinmarketcap.com/currencies/basic-attention-token/historical-data/'

#Print purpse of script and receive data input
print('This script opens CoinMarketCap and will retrieve 30 days worth of hisotrical data for $BAT.\n')
days = input('Selecting a number between 1 and 30, How many days back do you want to examine?:\n')
days = int(days)
	

class Crypto_Asset:
	def __init__(self, url, asset_name="BAT"):
		driver = webdriver.Firefox()
		driver.get(url)
		table = heading1 = driver.find_element_by_tag_name('table')
		table_data = table.text
		self.table_data = table_data
		self.asset_name = asset_name
		driver.quit()

	def historical_dictionary(self):
		table_rows = self.table_data.split('\n')
		historical_dictionary = {
			"Date" : [],
			"Open" : [],
			"High" : [],
			"Low" : [],
			"Volume" : [],
			"Market Cap" : []
		}
		for row in table_rows[1:]:
			x = row.split("$")
			for i in range(len(x)):
				x[i] = x[i].strip()

			historical_dictionary['Date'].append(x[0])
			historical_dictionary['Open'].append(float(x[1]))
			historical_dictionary['High'].append(float(x[2]))
			historical_dictionary['Low'].append(float(x[3]))
			historical_dictionary['Volume'].append(float(x[4]))
			historical_dictionary['Market Cap'].append(x[5])

		self.historical_dictionary = historical_dictionary

	def day_period_for_analytics(self, days):
			
		if days > 1:
			self.day_range_selection_as_string = self.historical_dictionary['Date'][days]
			self.average_open = statistics.mean(self.historical_dictionary['Open'][:days])
			self.average_high = statistics.mean(self.historical_dictionary['High'][:days])
			self.average_low = statistics.mean(self.historical_dictionary['Low'][:days])
		else:
			self.day_range_selection_as_string = self.historical_dictionary['Date'][days]
			self.average_open = self.historical_dictionary['Open'][days]
			self.average_high = self.historical_dictionary['High'][days]
			self.average_low = self.historical_dictionary['Low'][days]

	def string_summary(self):
		string = f'\n\nSince {self.day_range_selection_as_string}, {self.asset_name} has had an average openening price of ${round(self.average_open, 3)}, a average high price of ${round(self.average_high, 3)} and an average low price of ${round(self.average_low, 3)}.\n\n Happy Trading!'
		print(string) 

BAT = Crypto_Asset(bat_url)
BAT.historical_dictionary()
BAT.day_period_for_analytics(days)
BAT.string_summary()


