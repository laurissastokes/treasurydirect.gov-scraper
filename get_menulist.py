from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

driver=webdriver.Chrome()
driver.get('https://www.treasurydirect.gov/govt/reports/fip/investments-distribution-query/report.html')

tag = driver.find_elements_by_tag_name('mat-option')
for i in range(len(tag)):
    print(tag[i].text)
