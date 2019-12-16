from bs4 import BeautifulSoup
import requests

#the task is to get the planning permissions request for westminster
url="https://idoxpa.westminster.gov.uk/online-applications/pagedSearchResults.do?action=page&searchCriteria.page=1"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
search_results = soup.find_all(class_='sr-only')
print(search_results)
