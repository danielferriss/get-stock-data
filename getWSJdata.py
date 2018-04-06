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

def get_Qestimate_current(page_soup):
	return page_soup.find(id='quarterlyEstimateTbl').find_all(class_='valueCell')[0].get_text()

def get_Qestimate_1mnth(page_soup):
	return page_soup.find(id='quarterlyEstimateTbl').find_all(class_='valueCell')[1].get_text()

def get_Qestimate_3mnth(page_soup):
	return page_soup.find(id='quarterlyEstimateTbl').find_all(class_='valueCell')[2].get_text()

def get_nxtQestimate_current(page_soup):
	return page_soup.find(class_='cr_dataTable cr_dataTable-plain crTable-trends').find_all(class_='valueCell')[0].get_text()

def get_nxtQestimate_1mnth(page_soup):
	return page_soup.find(class_='cr_dataTable cr_dataTable-plain crTable-trends').find_all(class_='valueCell')[1].get_text()

def get_nxtQestimate_3mnth(page_soup):
	return page_soup.find(class_='cr_dataTable cr_dataTable-plain crTable-trends').find_all(class_='valueCell')[2].get_text()

def get_Qincome_growth(page_soup):
	return page_soup.find(class_='cr_financials_table').find(class_='data_data').get_text()

def get_Qsales(page_soup):
	return page_soup.find(class_='cr_financials_table').find_all(class_='data_data')[1].get_text()

def get_Qsales_growth(page_soup):
	return page_soup.find(class_='cr_financials_table').find_all(class_='data_data')[2].get_text()

def get_QEBITDA(page_soup):
	return page_soup.find(class_='cr_financials_table').find_all(class_='data_data')[3].get_text()

def get_Aincome_growth(page_soup):
	return page_soup.find(class_='cr_financials_table').find_all(class_='data_data')[4].get_text()

def get_Asales(page_soup):
	return page_soup.find(class_='cr_financials_table').find_all(class_='data_data')[5].get_text()

def get_Asales_growth(page_soup):
	return page_soup.find(class_='cr_financials_table').find_all(class_='data_data')[6].get_text()

def get_AEBITDA(page_soup):
	return page_soup.find(class_='cr_financials_table').find_all(class_='data_data')[7].get_text()





tsla = get_wsj_data('TSLA')

print(get_closing(tsla))