from bs4 import BeautifulSoup
import requests
import random

#the task is to get the planning permissions request for westminster
url="https://idoxpa.westminster.gov.uk/online-applications/weeklyListResults.do?action=firstPage"
UAS = ("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
       "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
       "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       )

ua = UAS[random.randrange(len(UAS))]

headers = {'user-agent': ua}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
f = open("index.html", "w")
f.write(soup.prettify())
f.close()
