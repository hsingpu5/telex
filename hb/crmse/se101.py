from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 标签切换演示

web = Chrome()

web.get('http://www.lagou.com')

el = web.find_element(by=By.XPATH, value='//*[@id="changeCityBox"]/p[1]/a')
el.click()
web.find_element(by=By.XPATH, value='//*[@id="search_input"]').send_keys('python', Keys.ENTER)
# print(web.title)
web.find_element(by=By.XPATH, value='//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()

web.switch_to.window(web.window_handles[-1])
job_detail = web.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]').text
print(job_detail)
web.close()
web.switch_to.window(web.window_handles[0])
# 切换iframe; 切回.
# web.switch_to.frame()
# web.switch_to.default_content()
time.sleep(3)
web.close()
