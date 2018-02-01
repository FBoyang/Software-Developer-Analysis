import time
from bs4 import BeautifulSoup
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import Request, urlopen

driver = webdriver.Chrome() #Can be changed

#url2 = 'https://www.linkedin.com/jobs/search/?keywords=Software%20Developer&location=Worldwide&locationId=OTHERS.worldwide'
url ='https://www.google.com/search?client=ubuntu&hs=Y4q&channel=fs&ei=zeNtWvuuDIW2zwKK45-IDA&q=linkedin+software+developer+jobs&oq=linkedin+software+developer+jo&gs_l=psy-ab.1.0.0j0i22i30k1l3.7626.12395.0.14246.13.13.0.0.0.0.169.1500.5j8.13.0....0...1c.1.64.psy-ab..0.13.1493...0i67k1.0.pdDGaoWhWPI&ibp=htl;jobs&sa=X&ved=0ahUKEwiI57bR9PrYAhXE2lMKHVIsAxQQiYsCCFUoAQ#fpstate=tldetail&htidocid=cL_9ZSLGsMxLkEJbAAAAAA%3D%3D&htivrt=jobs'
driver.get(url)
time.sleep(5)

#this is the function to scroll down the screen, you can try to adjust the sleeping time if too slow, time is the total scroll time 
def execute_times(times):
    for i in range(times + 1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)

execute_times(500)
html = driver.page_source
soup = BeautifulSoup(html,'html.parser') #lxml


#create a new file in the current directory called job.txt
f = open('job.txt', 'w')


#record the number of job discreption into infor (further we will need to record more metadata, so later we will apply numpy
#but first check wether the number is correct)
infor = 0
for text in soup.find_all('span',{"class":"_zMk"}):
    infor += 1
    f.write(text.text)

f.write("data size is: ", infor)
f.close()
#req = Request(url2, headers={('User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36)}

#webpage = urlopen(req).read()

#print(webpage)
