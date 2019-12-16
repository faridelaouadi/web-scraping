from bs4 import BeautifulSoup
import requests

#the task is to get the planning permissions request for westminster
url="https://idoxpa.westminster.gov.uk/online-applications/pagedSearchResults.do?action=page&searchCriteria.page=1"
page = requests.get(url)
print(page.status_code)
