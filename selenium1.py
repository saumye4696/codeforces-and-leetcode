from selenium import webdriver

path = "/home/saumye/Documents/chromedriver"
driver = webdriver.Chrome(path)

driver.get("http://www.google.com")
print(driver.title)
driver.quit()
