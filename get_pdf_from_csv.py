from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://ww2.eagle.org/en/rules-and-resources/rules-and-guides.html#/content/dam/eagle/rules-and-guides/current/generic/list_of_ABS_notations_and_symbols')
links = driver.find_elements_by_xpath('.//span[@class="file"]/a')

for link in links:
    link.get_attribute('href')