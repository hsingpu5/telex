from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()

web.get('http://www.lagou.com')

el = web.find_element(by=By.XPATH, value='//*[@id="changeCityBox"]/p[1]/a')
el.click()
web.find_element(by=By.XPATH, value='//*[@id="search_input"]').send_keys('python', Keys.ENTER)
#print(web.title)

li_list = web.find_elements(by=By.XPATH, value='//*[@id="jobList"]/div[1]/div')
for li in li_list:
    #print(li)
    job_name = li.find_elements(by=By.TAG_NAME, value='a')
    print(job_name[0].text)
    job_price=li.find_element(by=By.XPATH,value='./div[1]/div/div[2]/span').text
    print(job_price)
time.sleep(3)
web.close()
