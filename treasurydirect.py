from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait       
import time
from time import sleep
import random

driver=webdriver.Chrome()
driver.get('https://www.treasurydirect.gov/govt/reports/fip/investments-distribution-query/report.html')
driver.implicitly_wait(8)
sleepTimes = [2.1, 2.8, 3.2]


box = driver.find_element_by_xpath('//*[@id="appContainer"]/app-report-form/form/div[1]/mat-form-field')
tag = driver.find_elements_by_tag_name('mat-option')

for i in range(len(tag)):
    # if i > 269 and i < 284: #I used if statements to go back and get specific ranges of options after internet issue stopped program script completed and also to skip groups of options I didn't want.
        tag[i].click()    
        sleep(random.choice(sleepTimes))
        select_all = driver.find_element_by_xpath('//*[@id="appContainer"]/app-report-form/form/div[3]/button[1]')
        select_all.click() 
        sleep(random.choice(sleepTimes))
        generate_report = driver.find_element_by_xpath('//*[@id="appContainer"]/app-report-form/form/div[4]/button')
        generate_report.click()
        time.sleep(3)
        download_csv = driver.find_element_by_xpath('//*[@id="csv-button"]')
        download_csv.click() 
        sleep(random.choice(sleepTimes))
        back = driver.find_element_by_xpath('//*[@id="back"]') 
        back.click()
        sleep(random.choice(sleepTimes))
        box = driver.find_element_by_xpath('//*[@id="appContainer"]/app-report-form/form/div[1]/mat-form-field')
        box.click()
        sleep(random.choice(sleepTimes))
        tag = driver.find_elements_by_tag_name('mat-option')
