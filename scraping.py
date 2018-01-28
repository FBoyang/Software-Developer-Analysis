from bs4 import BeautifulSoup
import random
from selenium import webdriver
from urllib.request import Request, urlopen

driver = webdriver.Firefox()

#url2 = 'https://www.linkedin.com/jobs/search/?keywords=Software%20Developer&location=Worldwide&locationId=OTHERS.worldwide'
url ='https://www.google.com/search?client=ubuntu&hs=Y4q&channel=fs&ei=zeNtWvuuDIW2zwKK45-IDA&q=linkedin+software+developer+jobs&oq=linkedin+software+developer+jo&gs_l=psy-ab.1.0.0j0i22i30k1l3.7626.12395.0.14246.13.13.0.0.0.0.169.1500.5j8.13.0....0...1c.1.64.psy-ab..0.13.1493...0i67k1.0.pdDGaoWhWPI&ibp=htl;jobs&sa=X&ved=0ahUKEwiI57bR9PrYAhXE2lMKHVIsAxQQiYsCCFUoAQ#fpstate=tldetail&htidocid=cL_9ZSLGsMxLkEJbAAAAAA%3D%3D&htivrt=jobs'
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
print(soup.find_all('div'))
#req = Request(url2, headers={('User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36)}

#webpage = urlopen(req).read()

#print(webpage)