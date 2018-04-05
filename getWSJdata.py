from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#stock = input("Enter the stock ticker you would like to search for: ")

def get_wsj_data(ticker):
	my_url = 'http://quotes.wsj.com/' + ticker
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")
	return page_soup

def get_open(page_soup):
	return page_soup.find(class_='cr_compare_data').find(class_='data_data').get_text()

def get_closing(page_soup):
	return page_soup.find(id='quote_val').get_text()

def get_closing_change(page_soup):
	return page_soup.find(id='quote_change').get_text()

def get_closing_percent(page_soup):
	return page_soup.find(id='quote_changePer').get_text()

def get_volume(page_soup):
	return page_soup.find(id='quote_volume').get_text()

def get_65day_avg_volume(page_soup):
	return page_soup.find(class_='cr_data_collection cr_charts_info').find_all(class_='data_data')[1].get_text()

def get_1day_range(page_soup):
	return page_soup.find(class_='cr_data_collection cr_charts_info').find_all(class_='data_data')[2].get_text()

def get_52wk_range(page_soup):
	return page_soup.find(class_='cr_data_collection cr_charts_info').find_all(class_='data_data')[3].get_text()



tsla = get_wsj_data('TSLA')

print(get_open(tsla))