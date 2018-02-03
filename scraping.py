import time
from bs4 import BeautifulSoup
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import Request, urlopen

driver = webdriver.Chrome() #Can be changed

#url2 = 'https://www.linkedin.com/jobs/search/?keywords=Software%20Developer&location=Worldwide&locationId=OTHERS.worldwide'
url ='https://www.glassdoor.com/Job/software-developer-jobs-SRCH_KO0,18.htm'
driver.get(url)
time.sleep(2)
infor = 0

#create a new file in the current directory called job.txt
f = open('job.txt', 'w')

driver.find_element_by_link_text(2).click()
time.sleep(3)
driver.find_element_by_xpath("//button[@type='button' and @class='mfp-close']").click()
#this is the function to scroll down the screen, you can try to adjust the sleeping time if too slow, time is the total scroll time
'''
def execute_times(times):
    for i in range(2, times + 1):
        driver.find_element_by_link_text(str(i)).click()
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        
        #record the number of job discreption into infor (further we will need to record more metadata, so later we will apply numpy
        #but first check wether the number is correct)
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser') #lxml
        for text in soup.find_all('div',{"class":"jobDescriptionContent desc"}):
            infor += 1
            f.write(text.text)

execute_times(10)

f.write("data size is: " + str(infor))
f.close()
#req = Request(url2, headers={('User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36)}

#webpage = urlopen(req).read()

#print(webpage)
'''