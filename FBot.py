from selenium import webdriver

driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.get("https://facebook.com")

# login
email = driver.find_element_by_id("email")
email.send_keys('mymail@gmail.com')

pswrd = driver.find_element_by_id("pass")
pswrd.send_keys("mypass")

login_btn = driver.find_element_by_tag_name("button")
login_btn.click()
