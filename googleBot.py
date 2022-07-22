from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


what_am_i_searching = input("enter your web search: ")
my_content = input("enter you website domain: ")


driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.get("https://google.com")


searchbox = driver.find_element(By.CLASS_NAME, "gLFyf")
print(searchbox)
searchbox.send_keys(what_am_i_searching)
searchbox.send_keys(Keys.ENTER)


for i in range(10):
    results = driver.find_elements_by_class_name("LC20lb")
    websites = driver.find_elements(By.TAG_NAME, "cite")
    search_res = 0
    for result in results:
        if my_content in websites[search_res].text:
            print(str(i*10+search_res) + " :  " + str(result.text))
        search_res = search_res+1

    try:
        next = driver.find_element(By.ID, "pnnext")
        next.click()
    except:
        print("done")
        break
